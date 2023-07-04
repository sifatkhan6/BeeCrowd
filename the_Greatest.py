A, B, C = input().split(" ")
if int(A) < int(B) or int(A) < int(C):
    if int(B) < int(C):
        greatest = int(C)
    else:
        greatest = int(B)
else:
    greatest = int(A)
print(greatest, "eh o maior")