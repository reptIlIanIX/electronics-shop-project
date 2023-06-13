from src.item import Item
from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("Смартфон", 10000, 20)


def test_attribute_phone():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_sum():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    try:
        item1 + 13
    except ValueError:
        "только итем и фоун"


def test_not_null():
    try:
        phone1.number_of_sim = 0
    except ValueError:
        "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
