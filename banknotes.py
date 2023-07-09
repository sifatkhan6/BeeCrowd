N = int(input())
print(N)
print("{} nota(s) de R$ 100,00".format(int(N / 100)))
temp = N % 100
print("{} nota(s) de R$ 50,00".format(int(temp / 50)))
temp = temp % 50
print("{} nota(s) de R$ 20,00".format(int(temp / 20)))
temp = temp % 20
print("{} nota(s) de R$ 10,00".format(int(temp / 10)))
temp = temp % 10
print("{} nota(s) de R$ 5,00".format(int(temp / 5)))
temp = temp % 5
print("{} nota(s) de R$ 2,00".format(int(temp / 2)))
temp = temp % 2
print("{} nota(s) de R$ 1,00".format(int(temp / 1)))