>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>> 1. Describe the Problem:
()
As a customer
So that I can check if I want to 
### order something
I would like 
### to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able 
### to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like 
### to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too. \/
As a customer
So that I am reassured that my order will be delivered on time
I would like 
### to receive a text such as >>> "Thank you! Your order was placed and will be delivered before 18:52" 
### after I have ordered.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




>>> 2. Design the Function Signature:
()
# def check_dishes():
>>> Return: List of dishes: 
>>> >>>> number dish, name dish, price dish

# def order_meal():
>>> Input: number dish
>>> Return: nothing

# def recipt():
>>> recive number dish from @order_meal()
>>> acess @check_dishes() e colect price dish

# def order_manage(): >>> https://www.twilio.com/docs/messaging/quickstart/python
>>> Input: phone numer
>>> Return: mensage 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




>>> 3. Create Examples as Tests
# def test_check_dishes(): 
    Call @check_dishes to list dishes e return list with names and prices

## def test_order_meal():
    Given a dish number, return list item of it given number

# def test_recipt():
    Given a dish number to @order_meal(), call @recipt() and return each item with a sum of prices

# def test_order_manage():
    Order meal with @order_meal and call @order_manage wich recive phone and return text mesager
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




>>> 4. Implement the Behaviour (Contain Mistakes - >>>CHECK<<<)
()
# def test_check_dishes():
    class = Class()
    result = class.check_dishes()
    assert = return == [
        (1 - Dish_1: $10)
        (2 - Dish_2: $20)
        (3 - Dish_3: $30)
        (4 - Dish_4: $40)
        (5 - Dish_5: $50)
    ]

# def test_order_meal():
    class = Class()
    result = class.order_meal(2)
    assert = result == (2 - Dish_2: $20)


# def test_recipt():
    class = Class()
    class.order_meal(2)
    class.order_meal(3)
    result = class.recipt()
    assert = result == [
        (2 - Dish_2: $20)
        (3 - Dish_3: $30)
        (Total = $50)
    ]

# def test_order_manage():
    text_sender = Mock()
    text_sender.send_text.return_value = true
    class = Class()
    class.send_text(text_sender) # "injetando" nossa dependência aqui
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-