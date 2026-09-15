class Customer: 
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0
    def add_points(self, amount):
        self.points += int(amount * 0.05)
    def get_discount_rate(self):
        if self.grade == 'vip':
            return 0.10
        return 0.03
    def summary(self):
        return f"[{self.grade}] {self.name} (포인트: {self.points:,})"
        
    
c1 = Customer("김서강", "vip")
c1.add_points(45000)
c2 = Customer("이알바")

print(c1.summary())
print(c2.summary())

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer 
        self.items = items 
        
    def add_item(self, name, price):
        self.items.append((name, price))
        
    def total_price(self):
        subtotal = sum(price for _, price in self.items) 
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))
    
    def pay(self):
        amount = self.total_price()
        self.customer.add_points(amount)
        return amount
c1 = Customer("김서강", "vip")
order = Order("A-1001", c1, [("라떼", 5500), ("크루아상", 4200)])
print(f"{order.customer.name}님의 결제 금액: {order.total_price():,}원")

vip_customer = Customer("백설기", "vip")
basic_customer = Customer("김절편")

order1 = Order("A-1", vip_customer, [("쑥절미", 8000), ("꿀호떡", 5000)])
order2 = Order("A-2", basic_customer, [("가래떡", 7000)])
order3 = Order("B-1", vip_customer, [("송편", 10000)])

for order in (order1, order2, order3):
    paid_amount = order.pay()
    print(f"[{order.order_id}] {order.customer.name}님 결제 금액: {paid_amount:,}원")
    
print(vip_customer.summary())
print(basic_customer.summary())