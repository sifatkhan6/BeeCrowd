A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
triangle = (A*C) / 2
circle = C*C*3.14159
trapezium = ((A+B) / 2) * C
square = B*B
rectangle = A*B
print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")