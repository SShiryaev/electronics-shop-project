import csv
from src.instantiatecsverror import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)
        super().__init__()

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки."""

        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Отображает информацию об объекте класса для пользователей."""

        return f"{self.name}"

    def __add__(self, other):
        """Проверяет что объект принадлежит классу и складывает экземпляры класса по количеству товара в магазине."""

        if isinstance(other, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError("Можно складывать только объекты классов Phone или Item")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """Делает атрибут name приватным и возвращает его"""
        return self.__name

    @name.setter
    def name(self, name):
        """Проверяет, что длина наименования товара не больше 10 символов. В противном случае, обрезает строку"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """Инициализирует экземпляры класса Item данными из файла src/items.csv"""

        try:
            cls.all.clear()
            with open(file_name, encoding='cp1251') as file:
                data_csv = csv.DictReader(file)
                for attribute in data_csv:
                    if len(attribute) < 3:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    else:
                        name = attribute['name']
                        price = float(attribute['price'])
                        quantity = cls.string_to_number(attribute['quantity'])
                        object_from_cvs = cls(name, price, quantity)
                return object_from_cvs
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """Возвращает число из числа-строки"""
        float_number = float(string)
        return int(float_number)
