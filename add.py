class Cart:
   def __init__(self):
       self.items = {}
   def add_item(self, item_name,quantity):
       self.items[item_name] = quantity
   def display_items(self):
       print(self.items) # {'book': 3}

a = Cart()
a.add_item("book", 3)
a.display_items()