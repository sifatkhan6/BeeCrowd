import math

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
root = B*B-4*A*C
if(A == 0 or root <= 0):
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(root)) / (2*A)
    R2 = (-B - math.sqrt(root)) / (2*A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")