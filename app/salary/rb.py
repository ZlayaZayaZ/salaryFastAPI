from datetime import datetime


class RBSalary:
    def __init__(self, salary_id: int | None = None,
                 operator_id: int | None = None,
                 calculation_date: datetime | None = None,
                 period_start: datetime | None = None,
                 period_end: datetime | None = None,
                 total_score: float | None = None,
                 final_salary: float | None = None):
        self.id = salary_id
        self.operator_id = operator_id
        self.calculation_date = calculation_date
        self.period_start = period_start
        self.period_end = period_end
        self.total_score = total_score
        self.final_salary = final_salary

    def to_dict(self) -> dict:
        data = {'id': self.id, 'operator_id': self.operator_id, 'calculation_date': self.calculation_date,
                'period_start': self.period_start, 'period_end': self.period_end, 'total_score': self.total_score,
                'final_salary': self.final_salary}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
