from lib.item import Item
from lib.list import List
from lib.order import Order
from lib.message import Message


def test_menu():
    itens = [
        Item(1, "Dish_1", 10),
        Item(2, "Dish_2", 20),
        Item(3, "Dish_3", 30),
        Item(4, "Dish_4", 40),
        Item(5, "Dish_5", 50)
    ]
    list = List(itens)
    assert list.check_list() == itens
    

def test_make_order():
    itens = [
        Item(1, "Dish_1", 10),
        Item(2, "Dish_2", 20),
        Item(3, "Dish_3", 30),
        Item(4, "Dish_4", 40),
        Item(5, "Dish_5", 50)
    ]
    list = List(itens)
    order = Order(list)
    order.order_meal(2)
    assert order.return_list() == [2]

def test_recipt():
    itens = [
        Item(1, "Dish_1", 10),
        Item(2, "Dish_2", 20),
        Item(3, "Dish_3", 30),
        Item(4, "Dish_4", 40),
        Item(5, "Dish_5", 50)
    ]
    list = List(itens)
    order = Order(list)
    order.order_meal(2)
    order.order_meal(3)
    result = order.recipt()
    assert result == 50
    
