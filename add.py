class Product:
    def __init__(self, name):
       self.name = name
    def display_product_details(self):
       print("Product: {}".format(self.name)) # Product: TV

class ElectronicItem(Product):
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months
   
    def display_electronic_product_details(self):
        self.display_product_details()

e = ElectronicItem("TV")
e.display_electronic_product_details()