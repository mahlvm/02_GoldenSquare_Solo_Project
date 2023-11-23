class Order:


    def __init__(self, list):
        self.list_ordered = []
        self.list = list
    
    def order_meal(self, number):
        self.list_ordered.append(number)

    def return_list(self):
        return self.list_ordered
    
    def recipt(self):
        total = 0
        for i in self.list_ordered:
            for j in self.list.check_list():
                if i == j.number:
                    value = (j.price)
                    total += value
        return total



