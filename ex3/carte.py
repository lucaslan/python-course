import math
xa = int(input("digite Xa: "))
ya = int(input("digite Ya: "))
xb = int(input("digite Xb: "))
yb = int(input("digite Yb: "))

dist = math.sqrt(((xb - xa)**2) + ((yb - ya)**2))

if dist >= 10:
    print("longe")
else:
    print("perto")
