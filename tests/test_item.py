import pytest
import csv
from src.config import VALID_CSV, EMPTY_PATH, DAMAGE_CSV
from src.item import Item
from src.phone import Phone
from src.instantiatecsverror import InstantiateCSVError


@pytest.fixture
def item_fixture():
    """Фикстура инициализирующая экземпляр класса Item"""
    return Item('TV', 80000, 3)


@pytest.fixture
def phone_fixture():
    """Фикстура инициализирующая экземпляр класса Phone"""
    return Phone('IPhone10', 5000, 7, 2)


def test_calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 240000


def test_apply_discount(item_fixture):
    Item.pay_rate = 0.5
    item_fixture.apply_discount()
    assert item_fixture.price == 40000


def test_instantiate_from_csv():
    Item.instantiate_from_csv(VALID_CSV)
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'
    assert item1.price == 1000
    assert item1.quantity == 3


def test_string_to_number():
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('2.0') == 2
    assert Item.string_to_number('3.9') == 3


def test__repr__method(item_fixture):
    assert repr(item_fixture) == "Item('TV', 80000, 3)"


def test__str__method(item_fixture):
    assert str(item_fixture) == 'TV'


def test__add__method(item_fixture, phone_fixture):
    assert item_fixture + item_fixture == 6
    assert item_fixture + phone_fixture == 10
    assert phone_fixture + item_fixture == 10


def test_csv_not_found():
    file_name = EMPTY_PATH
    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        Item.instantiate_from_csv(EMPTY_PATH)
        with open(file_name, encoding='cp1251') as file:
            csv.DictReader(file)


def test_csv_damaged():
    file_name = DAMAGE_CSV
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        Item.instantiate_from_csv(DAMAGE_CSV)
        with open(file_name, encoding='cp1251') as file:
            csv.DictReader(file)
