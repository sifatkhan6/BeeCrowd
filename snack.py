X, Y = input().split()
X = int(X)
Y = int(Y)
if X==1:
    total = Y*4
    print(f"Total: R$ {total:.2f}")
elif X==2:
    total = Y*4.5
    print(f"Total: R$ {total:.2f}")
elif X==3:
    total = Y*5
    print(f"Total: R$ {total:.2f}")
elif X==4:
    total = Y*2
    print(f"Total: R$ {total:.2f}")
elif X==5:
    total = Y*1.5
    print(f"Total: R$ {total:.2f}")