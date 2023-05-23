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
