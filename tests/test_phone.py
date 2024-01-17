from src.phone import Phone
import pytest


@pytest.fixture
def phone1_fixture():
    """Фикстура инициализирующая экземпляр класса Phone"""
    return Phone('iPhone 15', 120000, 10, 2)


def test_calculate_total_price(phone1_fixture):
    assert phone1_fixture.calculate_total_price() == 1200000


def test_apply_discount(phone1_fixture):
    Phone.pay_rate = 0.5
    phone1_fixture.apply_discount()
    assert phone1_fixture.price == 60000


def test__repr__method(phone1_fixture):
    assert repr(phone1_fixture) == "Phone('iPhone 15', 120000, 10, 2)"


def test__str__method(phone1_fixture):
    assert str(phone1_fixture) == 'iPhone 15'


def test__add__method(phone1_fixture):
    assert phone1_fixture + phone1_fixture == 20
    assert phone1_fixture + 3 is None
