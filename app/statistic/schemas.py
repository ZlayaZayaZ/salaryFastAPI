from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class SStatistic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date: datetime = Field(..., description="Дата события")
    parameter_id: int = Field(..., description="id параметра")
    value: int = Field(..., description="Значение параметра")
    operator_id: int = Field(..., description="id оператора")
    work_id: int = Field(..., description="id рабочей смены")

