from re import split

pi = 3.14159
a = (input())
b = a.split()
A = float(b[0])
B = float(b[1])
C = float(b[2])
triangulo = (A*C)/2
areac = pi*C*C
tra = ((A+B)*C)/2
qua = B*B
ret = A*B
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {areac:.3f}")
print(f"TRAPEZIO: {tra:.3f}")
print(f"QUADRADO: {qua:.3f}")
print(f"RETANGULO: {ret:.3f}")
