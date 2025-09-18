from datetime import datetime


class RBStatistic:
    def __init__(self, statistic_id: int | None = None,
                 date: datetime | None = None,
                 parameter_id: int | None = None,
                 value: int | None = None,
                 work_id: int | None = None,
                 operator_id: int | None = None,):
        self.id = statistic_id
        self.date = date
        self.parameter_id = parameter_id
        self.value = value
        self.work_id = work_id
        self.operator_id = operator_id

    def to_dict(self) -> dict:
        data = {'id': self.id, 'date': self.date, 'parameter_id': self.parameter_id,
                'value': self.value, 'work_id': self.work_id, 'operator_id': self.operator_id}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data

