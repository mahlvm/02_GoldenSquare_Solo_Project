from lib.order import Order
from unittest.mock import Mock

def test_fake_order_meal():
    fake_list = Mock()
    fake_list.list_ordered.return_value = [
        (1, "Dish_1", 10),
        (2, "Dish_2", 20),
        (3, "Dish_3", 30),
        (4, "Dish_4", 40),
        (5, "Dish_5", 50)
    ]
    order = Order(fake_list)
    order.order_meal(1)
    assert order.return_list() == [1]


#def test_fake_recipt():
#    
#    fake_item_2 = Mock()
#    fake_item_2.number.return_value = 2
#    fake_item_2.price.return_value = 20
#    fake_item_3 = Mock()
#    fake_item_3.number.return_value = 3
#    fake_item_3.price.return_value = 30
#    fake_list = Mock()
#    fake_list.check_list.return_value = [fake_item_2, fake_item_3]#

#    order = Order(fake_list)
#    order.order_meal(2)
#    order.order_meal(3)
#    result = order.recipt()
#    assert result == 50