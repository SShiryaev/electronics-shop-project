from src.item import Item
import pytest


@pytest.fixture
def item1_fixture():
    """Фикстура инициализирующая экземпляр класса Item"""
    return Item('TV', 80000, 3)


def test_calculate_total_price(item1_fixture):
    assert item1_fixture.calculate_total_price() == 240000


def test_apply_discount(item1_fixture):
    Item.pay_rate = 0.5
    item1_fixture.apply_discount()
    assert item1_fixture.price == 40000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'
    assert item1.price == 1000
    assert item1.quantity == 3


def test_string_to_number():
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('2.0') == 2
    assert Item.string_to_number('3.9') == 3


def test_repr_method(item1_fixture):
    assert repr(item1_fixture) == "Item('TV', 80000, 3)"


def test_str_method(item1_fixture):
    assert str(item1_fixture) == 'TV'
