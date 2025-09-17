class RBEmployee:
    def __init__(self, employee_id: int | None = None,
                 salary: int | None = None):
        self.id = employee_id
        self.salary = salary

    def to_dict(self) -> dict:
        data = {'id': self.id, 'salary': self.salary}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data

