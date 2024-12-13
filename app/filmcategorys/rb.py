class RBFilmCategory:
    def __init__(self, category_id: int | None = None,
                 film_id: int | None = None
                 ):
        self.category_id = category_id
        self.film_id = film_id

        
    def to_dict(self) -> dict:
        data = {'film_id': self.film_id, 'category_id': self.category_id}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data