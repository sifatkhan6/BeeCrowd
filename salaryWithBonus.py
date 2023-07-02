name = str(input())
salary = float(input())
sales = float(input())
bonus = (sales*15) / 100
totalSalary = salary + bonus
print(f"TOTAL = R$ {totalSalary:.2f}")