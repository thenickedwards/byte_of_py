class Queue:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

#####

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
        
    def take_order(self, customer, flavor, scoops):
        # verify flavor available
        if flavor not in self.flavors:
            raise ValueError("Sorry, we don't have that flavor.")
            # print("Sorry, we don't have that flavor.")
        # validate scoops
        try:
            scoops = int(scoops)
        except ValueError:
            raise ValueError("Please enter a valid number of scoops.")
            # print("Please enter a valid number of scoops.")
        if scoops < 1 or scoops > 3:
            raise ValueError("Sorry, I can only take an order for 1, 2, or 3 scoops.")
            # print("Sorry, I can only take an order for 1, 2, or 3 scoops.")
        # enqueue order
        else:
            print('Order created!')
    
    def show_all_orders():
        pass
    
    def next_order():
        pass

#####

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
# shop.show_all_orders()
# shop.next_order()
# shop.show_all_orders()