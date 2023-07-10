A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
sum1 = A+B
sum2 = C+D
if(B > C and D > A) and (sum2 > sum1) and (C % 2 >= 0 and D % 2 >= 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")