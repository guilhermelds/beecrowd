from re import split

a = input()
b = a.split()
A = int(b[0])
B = int(b[1])
C = int(b[2])

maiorab = int((A + B + abs(A-B))/2)
maior = int((maiorab + C + abs(maiorab - C))/2)
print(maior,"eh maior")