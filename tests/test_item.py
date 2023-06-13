"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_example():
    return Item("Человек", 30000, 15)


def test_item_vatiables(item_example):
    assert item_example.name == "Человек"
    assert item_example.price == 30000
    assert item_example.quantity == 15


def test_calculate_total_price(item_example):
    assert item_example.calculate_total_price() == 450000


def test_apply_discount(item_example):
    pay_rate = 0.3
    item_example.apply_discount()
    assert item_example.price == 30000.0


item1 = Item('NASJDAJSDKASDJASD', 300, 15)
assert item1.name == 'NASJDAJSDKASDJASD'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('513') == 513


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'
    assert item1.quantity == 3


def test_setter():
    item5 = Item("13123", 123, 132)
    item5.name = "3123"
    assert item5.name == "3123"
    try:
        item5.name = 'sdkaoskdasod'
    except ValueError:
        'Длина наименования товара превышает 10 символов'

def test_repr():
    item1 = Item('Oleg', 123, 132)
    assert str(item1) == 'Oleg'
    assert repr(item1) == "Item('Oleg', 123, 132)"
