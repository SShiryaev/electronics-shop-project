from src.item import Item
import pytest


@pytest.fixture
def item1_fixture():
    return Item('TV', 80000, 3)


def test_calculate_total_price(item1_fixture):
    assert item1_fixture.calculate_total_price() == 240000


def test_apply_discount(item1_fixture):
    Item.pay_rate = 0.5
    item1_fixture.apply_discount()
    assert item1_fixture.price == 40000
