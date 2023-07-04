import math
p1 = input().split()
p2 = input().split()
x1, y1 = p1
x2, y2 = p2
x = float(x2) - float(x1)
y = float(y2) - float(y1)
finalX = x*x
finalY = y*y
distance = finalX + finalY
finalDistance = math.sqrt(distance)
print(f"{finalDistance:.4f}")
