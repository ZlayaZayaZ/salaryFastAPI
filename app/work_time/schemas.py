from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class SWork(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    start_date: datetime = Field(..., description="Дата начала работы")
    end_date: datetime = Field(..., description="Дата окончания работы")
    operator_id: int = Field(..., description="id оператора")


class SBreak(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    start_time: datetime = Field(..., description="Время начала перерыва")
    end_time: datetime = Field(..., description="Время окончания перерыва")
    operator_id: int = Field(..., description="id оператора")


class SWorkAdd(BaseModel):

    start_date: datetime = Field(..., description="Дата начала работы")
    end_date: datetime = Field(..., description="Дата окончания работы")
    operator_id: int = Field(..., description="id оператора")


class SBreakAdd(BaseModel):

    start_time: datetime = Field(..., description="Время начала перерыва")
    end_time: datetime = Field(..., description="Время окончания перерыва")
    operator_id: int = Field(..., description="id оператора")
