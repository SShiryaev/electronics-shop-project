from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard1_fixture():
    """Фикстура инициализирующая экземпляр класса Keyboard"""
    return Keyboard('Logitech K120', 2000, 15)


def test__str__(keyboard1_fixture):
    assert str(keyboard1_fixture) == "Logitech K120"
    assert str(keyboard1_fixture.language) == "EN"
    keyboard1_fixture.change_lang()
    assert str(keyboard1_fixture.language) == "RU"
    keyboard1_fixture.change_lang()
    assert str(keyboard1_fixture.language) == "EN"
