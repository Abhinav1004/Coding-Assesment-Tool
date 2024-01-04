from pydantic import BaseModel, Field
from typing import List, Dict, Union, Optional, Literal, Any
# from pydantic import BaseModel

class RequestModelPredictRating(BaseModel):
    tx_difficulty: float = 3.5
    total_correctness: float = 95.0
    total_compute: float = 1500.0
    total_robustness: float = 80.0
    total_memtotal: float = 2048.0
    compile_success: int = 1
    score_percentage: float = 90.0
    time_spent: float = 10.0
    nu_pgmr_comment_flux_all: float = 1.5
    nu_pgmr_cyclo_flux_all: float = 2.0
    nu_pgmr_filesize_flux_all: float = 0.8
    nu_pgmr_dac_flux_all: float = 1.2
    nu_loc_flux_source_all: float = 500.0
    nu_ce_models_units_all: float = 3.0
    nu_aberrant_ce_units_all: float = 0.5
    loc_submit: float = 200.0
    cyclo_submit: float = 1.8
    nom_submit: float = 2.0
    dac_submit: float = 1.0
    fanout_submit: float = 2.5
    ce_units_submit: float = 5.0
    aberrant_ce_units_submit: float = 0.8
    tx_file_type: str = 'cpp'
    correctness_norm: float = 0.9
    compute_norm: float = 0.95
    robustness_norm: float = 0.85
    memtotal_norm: float = 0.98

class ResponseModelPredictRating(BaseModel):
    status: Literal["success", "failure"]
    error: Optional[str] = Field(title="Error Reason")


