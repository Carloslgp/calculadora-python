print("********************************")
print("*         CALCULADORA          *")
print("*      1-   ADIÇÃO             *")
print("*      2-  SUBTRAÇÃO           *")
print("*      3-   DIVISÃO            *")
print("*      4- MULTIPLICAÇÃO        *")
print("*      5-    SAÍDA             *")
print("********************************")
tipo = int(input("Digite o número da operação desejada ou saída:"))
n1 = int(input("Digite o primeiro número?"))
n2 = int(input("Digite o segundo número?"))

if tipo == 1:
    resposta = n1 + n2
    print(resposta)
elif tipo == 2:
    resposta = n1 - n2
    print(resposta)
elif tipo == 3:
    resposta = n1/n2
    print(resposta)
elif tipo == 4:
    resposta = n1*n2
    print(resposta)
else:
    print("Obrigado por usar")
