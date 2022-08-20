x = int(input())
if x < 0 or x > 1000000:
    while x < 0 or x > 1000000:
        print("valor invalido")
        x = int(input())     
divisao1 = x//100
resto1 = x%100
divisao2 = resto1//50
resto2 = resto1%50
divisao3 = resto2//20
resto3 = resto2%20
divisao4 = resto3//10
resto4 = resto3%10
divisao5 = resto4//5
resto5 = resto4%5
divisao6 = resto5//2
resto6 = resto5%2
divisao7 = resto6//1
resto7 = resto6%1
print(x)
print(divisao1, "nota(s) de R$ 100,00")
print(divisao2, "nota(s) de R$ 50,00")
print(divisao3, "nota(s) de R$ 20,00")
print(divisao4, "nota(s) de R$ 10,00")
print(divisao5, "nota(s) de R$ 5,00")
print(divisao6, "nota(s) de R$ 2,00")
print(divisao7, "nota(s) de R$ 1,00")