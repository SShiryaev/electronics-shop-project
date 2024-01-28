from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def item_fixture():
    """Фикстура инициализирующая экземпляр класса Item"""
    return Item('TV', 80000, 3)


@pytest.fixture
def phone_fixture():
    """Фикстура инициализирующая экземпляр класса Phone"""
    return Phone('iPhone 15', 120000, 10, 2)


def test_calculate_total_price(phone_fixture):
    assert phone_fixture.calculate_total_price() == 1200000


def test_apply_discount(phone_fixture):
    Phone.pay_rate = 0.5
    phone_fixture.apply_discount()
    assert phone_fixture.price == 60000


def test__repr__method(phone_fixture):
    assert repr(phone_fixture) == "Phone('iPhone 15', 120000, 10, 2)"


def test__str__method(phone_fixture):
    assert str(phone_fixture) == 'iPhone 15'


def test__add__method(phone_fixture, item_fixture):
    assert phone_fixture + phone_fixture == 20
    assert item_fixture + phone_fixture == 13
    assert phone_fixture + item_fixture == 13
