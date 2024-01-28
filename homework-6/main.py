from src.item import Item
from src.config import VALID_CSV, DAMAGE_CSV, EMPTY_PATH

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(EMPTY_PATH)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(DAMAGE_CSV)
    # InstantiateCSVError: Файл item.csv поврежден
