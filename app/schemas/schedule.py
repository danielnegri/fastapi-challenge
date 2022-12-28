from pydantic import BaseModel


class ScheduleBase(BaseModel):
    pass


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleInDBBase(ScheduleBase):
    id: str
    loan_id: str

    class Config:
        orm_mode = True


class Schedule(ScheduleInDBBase):
    pass


class ScheduleInDB(ScheduleInDBBase):
    pass
