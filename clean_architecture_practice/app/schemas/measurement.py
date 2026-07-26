from pydantic import BaseModel, Field, validator
from datetime import datetime

class MeasurementCreate(BaseModel):
    user_id: int
    weight: float = Field(gt=0, le=500, description="Вес в килограммах (от 0 до 500)")
    height: float = Field(gt=0, le=3, description="Рост в метрах (от 0 до 3)")

    @validator('height')
    def validate_height(cls, v):
        if v < 0.5:
            raise ValueError('Рост не может быть меньше 0.5 метра')
        if v > 3.0:
            raise ValueError('Рост не может быть больше 3 метров')
        return v

    @validator('weight')
    def validate_weight(cls, v):
        if v < 1:
            raise ValueError('Вес не может быть меньше 1 кг')
        if v > 500:
            raise ValueError('Вес не может быть больше 500 кг')
        return v

class MeasurementResponse(BaseModel):
    id: int
    user_id: int
    weight: float
    height: float
    imt: float
    created_at: datetime

    class Config:
        from_attributes = True