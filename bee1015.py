from re import split
import math
a = input()
b = input()
ponto1 = a.split()
ponto2 = b.split()

x1 = float(ponto1[0])
y1 = float(ponto1[1])
x2 = float(ponto2[0])
y2 = float(ponto2[1])

distancia = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
print(f"{distancia:.4f}")