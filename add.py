class Mobile:
  def __init__(self, model, price):
      self.model = model
      self.price = price

mobile1 = Mobile("iPhone 17 Pro", 120000)
mobile2 = Mobile("Samsung Galaxy S25", 80000)

print(mobile1.model)  # iPhone 17 Pro
print(mobile1.price)  # 120000

print(mobile2.model)  # Samsung Galaxy S25
print(mobile2.price)  # 80000
