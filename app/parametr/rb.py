class RBParameter:
    def __init__(self, parameter_id: int | None = None,
                 is_positive: bool | None = None,
                 weight: float | None = None):
        self.id = parameter_id
        self.is_positive = is_positive
        self.weight = weight

    def to_dict(self) -> dict:
        data = {'id': self.id, 'is_positive': self.is_positive, 'weight': self.weight}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data

