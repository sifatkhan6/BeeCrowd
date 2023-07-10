N = float(input())
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(N / 100)))
temp = N % 100
print("{} nota(s) de R$ 50.00".format(int(temp / 50)))
temp %= 50
print("{} nota(s) de R$ 20.00".format(int(temp / 20)))
temp %= 20
print("{} nota(s) de R$ 10.00".format(int(temp / 10)))
temp %= 10
print("{} nota(s) de R$ 5.00".format(int(temp / 5)))
temp %= 5
print("{} nota(s) de R$ 2.00".format(int(temp / 2)))
temp %= 2
print("MOEDAS:")
temp *= 100
print("{} moeda(s) de R$ 1.00".format(int(temp / 100)))
temp %= 100
print("{} moeda(s) de R$ 0.50".format(int(temp / 50)))
temp %= 50
print("{} moeda(s) de R$ 0.25".format(int(temp / 25)))
temp %= 25
print("{} moeda(s) de R$ 0.10".format(int(temp / 10)))
temp %= 10
print("{} moeda(s) de R$ 0.05".format(int(temp / 5)))
temp %= 5
print("{} moeda(s) de R$ 0.01".format(int(temp / 1)))