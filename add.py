class Cart:
   flat_discount = 0
   @classmethod
   def update_flat_discount(cls, new_flat_discount):
       cls.flat_discount = new_flat_discount

Cart.update_flat_discount(25)
print(Cart.flat_discount) # 25