code1, units1, price1 = input().split()
code2, units2, price2 = input().split()
code1 = int(code1)
units1 = int(units1)
price1 = float(price1)
code2 = int(code2)
units2 = int(units2)
price2 = float(price2)
product1Cost = units1*price1
product2Cost = units2*price2
total = product1Cost+product2Cost
print(f"VALOR A PAGAR: R$ {total:.2f}")