from pydantic import BaseModel, Field, ConfigDict


class SParameter(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str = Field(..., min_length=1, max_length=50, description="Название параметра")
    description: str = Field(..., min_length=1, max_length=255, description="Описание")
    norm: int = Field(..., description="норма для идеального выполнения")
    base: int = Field(..., description="норма для базового выполнения")
    weight: float = Field(..., description="вес параметра от 0 до 1 относительно зарплаты")
    is_positive: bool = Field(..., description="положительный/отрицательный")
