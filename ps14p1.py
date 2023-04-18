class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b

empl1 = Employee('Konnor', 'Del Mar', 90000.00)

print(f"Email: {empl1.email}")
print(f"First name: {empl1.first}")
print(f"Last name: {empl1.last}")
print(f"Pay: {empl1.pay}")

bonus_rate1 = 0.10
bonus_rate2 = 0.20
bonus1 = empl1.bonus(bonus_rate1)
bonus2 = empl1.bonus(bonus_rate2)

print(f"Bonus for rate {bonus_rate1 * 100}%: {bonus1}")
print(f"Bonus for rate {bonus_rate2 * 100}%: {bonus2}")
