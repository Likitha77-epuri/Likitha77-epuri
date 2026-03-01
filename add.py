class Cart:
   flat_discount = 0
   min_bill = 100
   def print_min_bill(self):
       print(Cart.min_bill) # 200
a = Cart()
b = Cart()
Cart.min_bill = 200
b.print_min_bill() 