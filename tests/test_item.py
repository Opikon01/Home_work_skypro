from src.item import Item


def test_item_creation():
    item = Item("Смартфон", 1.0, 10)
    assert item.name == "Смартфон"
    assert item.price == 1.0
    assert item.quantity == 10


def test_calculate_total_price():
    item = Item("Смартфон", 1.0, 10)
    assert item.calculate_total_price() == 10.0


def test_apply_discount():
    item = Item("Смартфон", 1.0, 10)
    item.pay_rate = 0.9
    assert item.apply_discount() == 0.9
    assert item.price == 0.9
