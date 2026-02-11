class Item:
    def __init__(self, name, price, category):
        if price <= 0:
            raise ValueError("Invalid value for price, got {}".format(price))
        self.name = name
        self.price = price
        self.category = category

    def get_detail(self):
        return "{}@{}-{}".format(self.name, self.price, self.category)