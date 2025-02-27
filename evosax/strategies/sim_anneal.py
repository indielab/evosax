"""Simulated Annealing (Rere et al., 2015).

Reference: https://www.sciencedirect.com/science/article/pii/S1877050915035759
"""

from collections.abc import Callable

import jax
import jax.numpy as jnp
from flax import struct

from ..strategy import Params, State, Strategy, metrics_fn
from ..types import Fitness, Population, Solution


@struct.dataclass
class State(State):
    current_solution: Solution
    current_fitness: Fitness
    std: float
    temperature: float


@struct.dataclass
class Params(Params):
    std_init: float
    std_decay: float
    std_limit: float
    temperature_init: float
    temperature_limit: float
    temperature_decay: float
    boltzmann_constant: float


class SimAnneal(Strategy):
    """Simulated Annealing (SA)."""

    def __init__(
        self,
        population_size: int,
        solution: Solution,
        metrics_fn: Callable = metrics_fn,
        **fitness_kwargs: bool | int | float,
    ):
        """Initialize SA."""
        super().__init__(population_size, solution, metrics_fn, **fitness_kwargs)
        self.strategy_name = "SimAnneal"

    @property
    def _default_params(self) -> Params:
        return Params(
            std_init=1.0,
            std_decay=1.0,
            std_limit=0.0,
            temperature_init=1.0,
            temperature_limit=0.1,
            temperature_decay=0.999,
            boltzmann_constant=5.0,
        )

    def _init(self, key: jax.Array, params: Params) -> State:
        state = State(
            current_solution=jnp.full((self.num_dims,), jnp.nan),
            current_fitness=jnp.inf,
            std=params.std_init,
            temperature=params.temperature_init,
            best_solution=jnp.full((self.num_dims,), jnp.nan),
            best_fitness=jnp.inf,
            generation_counter=0,
        )
        return state

    def _ask(
        self,
        key: jax.Array,
        state: State,
        params: Params,
    ) -> tuple[Population, State]:
        z = jax.random.normal(key, (self.population_size, self.num_dims))
        population = state.current_solution + state.std * z
        return population, state

    def _tell(
        self,
        key: jax.Array,
        population: Population,
        fitness: Fitness,
        state: State,
        params: Params,
    ) -> State:
        best_idx = jnp.argmin(fitness)
        best_member, best_fitness = population[best_idx], fitness[best_idx]

        delta = best_fitness - state.current_fitness
        metropolis = jnp.exp(-delta / (params.boltzmann_constant * state.temperature))
        acceptance = jax.random.uniform(key)

        # Replace if improved or random metropolis acceptance
        replace = jnp.logical_or(delta < 0, acceptance < metropolis)

        # Note: We replace by best member in generation
        current_solution = jnp.where(replace, best_member, state.current_solution)
        current_fitness = jnp.where(replace, best_fitness, state.current_fitness)

        # Update std
        std = jnp.clip(state.std * params.std_decay, min=params.std_limit)

        # Update temperature
        temperature = jnp.clip(
            state.temperature * params.temperature_decay,
            min=params.temperature_limit,
        )

        return state.replace(
            current_solution=current_solution,
            current_fitness=current_fitness,
            std=std,
            temperature=temperature,
        )
