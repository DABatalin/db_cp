class RBUser:
    def __init__(self, id: int | None = None):
        self.id = id

        
    def to_dict(self) -> dict:
        data = {'id': self.id}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data