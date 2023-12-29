import os
import csv


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
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_path):
        correct_file_path = '../' + file_path
        cls.all.clear()
        with open(os.path.join(correct_file_path), encoding='cp1251') as file:
            data_csv = csv.DictReader(file)
            for attribute in data_csv:
                name = attribute['name']
                price = float(attribute['price'])
                quantity = int(attribute['quantity'])
                object_from_cvs = cls(name, price, quantity)
            return object_from_cvs

    @staticmethod
    def string_to_number(string):
        float_number = float(string)
        return int(float_number)
