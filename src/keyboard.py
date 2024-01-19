from src.item import Item


class MixinKeyboardLanguage:
    """
    Класс-миксин для хранения и изменения раскладки клавиатуры.
    """
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        """Делает атрибут name приватным и возвращает его"""
        return self.__language

    def change_lang(self):
        self.__language = "RU" if self.language == "EN" else "EN"


class Keyboard(Item, MixinKeyboardLanguage):
    """
    Класс для представления категории Телефон в магазине.
    """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
