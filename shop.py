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