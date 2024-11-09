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
        # TODO: make this a nice string
        print(self.items)
        print("All Pending Ice Cream Orders:")
        for i in self.items:
            print("Customer:", i["customer"], " -- flavor: ",
                  i["flavor"], ", scoops: ", i["scoops"])


#####

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()
        
    def take_order(self, customer, flavor, scoops):
        try:
            # verify flavor available
            if flavor not in self.flavors:
                raise ValueError("❌ Sorry, we don't have that flavor.")
            # validate scoops
            scoops = int(scoops)
            if scoops < 1 or scoops > 3:
                raise ValueError("❌ Sorry, I can only take an order for 1, 2, or 3 scoops.")
        except ValueError as e:
            print(e)
            return
        # enqueue order if no errors in try/except
        else:
            new_order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(new_order)
            print('Order created!')
    
    def show_all_orders(self):
        self.orders.show_queue()
    
    def next_order(self):
        order_up = self.orders.dequeue()
        if order_up:
            print(f"🍨 Order up for: \033[1m{order_up['customer']}\033[0m: {order_up['scoops']} scoop(s) of {order_up['flavor']}")
        else:
            print("No more orders!")


##### TESTING

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)  # Pass
shop.take_order("Marcy", "mint chip", 1)    # Pass
shop.take_order("Leopold", "vanilla", 2)    # Fail on flavor verification
shop.take_order("Bruce", "rocky road", 0)   # Fail on scoops validation
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()