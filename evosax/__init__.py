from .core import FitnessShaper
from .networks import NetworkMapper
from .problems import ProblemMapper
from .strategies import (
    ARS,
    ASEBO,
    BIPOP_CMA_ES,
    CMA_ES,
    CR_FM_NES,
    DE,
    DES,
    ESMC,
    GESMR_GA,
    GLD,
    IPOP_CMA_ES,
    LES,
    LGA,
    LM_MA_ES,
    MA_ES,
    MR15_GA,
    PES,
    PGPE,
    PSO,
    SAMR_GA,
    SNES,
    SV_CMA_ES,
    DiffusionEvolution,
    EvoTF_ES,
    GuidedES,
    HillClimber,
    NoiseReuseES,
    OpenES,
    RandomSearch,
    Rm_ES,
    Sep_CMA_ES,
    SimAnneal,
    SimpleES,
    SimpleGA,
    SV_OpenES,
    iAMaLGaM_Full,
    iAMaLGaM_Indep,
    xNES,
)
from .strategy import Params, State, Strategy

Strategies = {
    "SimpleGA": SimpleGA,
    "SimpleES": SimpleES,
    "CMA_ES": CMA_ES,
    "DE": DE,
    "PSO": PSO,
    "OpenES": OpenES,
    "PGPE": PGPE,
    "PES": PES,
    "ARS": ARS,
    "Sep_CMA_ES": Sep_CMA_ES,
    "BIPOP_CMA_ES": BIPOP_CMA_ES,
    "IPOP_CMA_ES": IPOP_CMA_ES,
    "iAMaLGaM_Full": iAMaLGaM_Full,
    "iAMaLGaM_Indep": iAMaLGaM_Indep,
    "MA_ES": MA_ES,
    "LM_MA_ES": LM_MA_ES,
    "Rm_ES": Rm_ES,
    "GLD": GLD,
    "SimAnneal": SimAnneal,
    "SNES": SNES,
    "xNES": xNES,
    "ESMC": ESMC,
    "DES": DES,
    "SAMR_GA": SAMR_GA,
    "GESMR_GA": GESMR_GA,
    "GuidedES": GuidedES,
    "ASEBO": ASEBO,
    "CR_FM_NES": CR_FM_NES,
    "MR15_GA": MR15_GA,
    "RandomSearch": RandomSearch,
    "LES": LES,
    "LGA": LGA,
    "NoiseReuseES": NoiseReuseES,
    "HillClimber": HillClimber,
    "EvoTF_ES": EvoTF_ES,
    "DiffusionEvolution": DiffusionEvolution,
    "SV_CMA_ES": SV_CMA_ES,
    "SV_OpenES": SV_OpenES,
}

__all__ = [
    "Strategies",
    "State",
    "Params",
    "FitnessShaper",
    "NetworkMapper",
    "ProblemMapper",
    "Strategy",
    "SimpleGA",
    "SimpleES",
    "CMA_ES",
    "DE",
    "PSO",
    "OpenES",
    "PGPE",
    "PES",
    "ARS",
    "Sep_CMA_ES",
    "BIPOP_CMA_ES",
    "IPOP_CMA_ES",
    "iAMaLGaM_Full",
    "iAMaLGaM_Indep",
    "MA_ES",
    "LM_MA_ES",
    "Rm_ES",
    "GLD",
    "SimAnneal",
    "SNES",
    "xNES",
    "ESMC",
    "DES",
    "SAMR_GA",
    "GESMR_GA",
    "GuidedES",
    "ASEBO",
    "CR_FM_NES",
    "MR15_GA",
    "RandomSearch",
    "LES",
    "LGA",
    "NoiseReuseES",
    "HillClimber",
    "EvoTF_ES",
    "DiffusionEvolution",
    "SV_CMA_ES",
    "SV_OpenES",
]
