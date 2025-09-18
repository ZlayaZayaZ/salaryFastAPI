from datetime import datetime


class RBWork:
    def __init__(self, work_id: int | None = None,
                 operator_id: int | None = None,
                 start_date: datetime | None = None,
                 end_date: datetime | None = None):
        self.id = work_id
        self.operator_id = operator_id
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self) -> dict:
        data = {'id': self.id, 'operator_id': self.operator_id, 'start_date': self.start_date, 'end_date': self.end_date}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data


class RBBreak:
    def __init__(self, break_id: int | None = None,
                 operator_id: int | None = None,
                 start_time: datetime | None = None,
                 end_time: datetime | None = None):
        self.id = break_id
        self.operator_id = operator_id
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self) -> dict:
        data = {'id': self.id, 'operator_id': self.operator_id, 'start_time': self.start_time, 'end_time': self.end_time}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
