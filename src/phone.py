from src.item import Item


class Phone(Item):
    """
    Класс для представления категории Телефон в магазине.
    """
    def __init__(self, name, price, quantity, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки."""

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
