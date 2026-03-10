class Product:
    def __init__(self, name):
       self.name = name
       self.deal_price = deal_price

    def display_product_details(self):
        print("Product: {}".format(self.name)) # Product: Milk
           
    def get_deal_price(self):
        return self.deal_price

class GroceryItem(Product):
    pass
   
class Order:
    def __init__(self):
         self.items_in_cart = []
     
    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            
milk = GroceryItem("Milk")
order.add_item(milk, 2)
order.display_order_details()