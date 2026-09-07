from pydantic import BaseModel

class GlassInput(BaseModel):
    RI: float
    Na: float
    Mg: float
    Al: float
    Si: float
    K:  float
    Ca: float

    class Config:
        json_schema_extra = {
            "example": {
                "RI": 1.52101,
                "Na": 13.64,
                "Mg": 4.49,
                "Al": 1.10,
                "Si": 71.78,
                "K": 0.06,
                "Ca": 8.75
            }
        }

class PredictionResult(BaseModel):
    glass_type: str
    glass_type_number: int
    probability: float
    confidence_level: dict