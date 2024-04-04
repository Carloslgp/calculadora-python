op = ''
print("--------Bem Vindo a Calculadora--------")
while op != 0:
    print("1 - soma \n2 - subtração \n3 - multiplicação \n4- divisão \n0 - sair")
    op = int(input("Qual operação você deseja fazer?"))
    if op == 0:
        break
    if op < 0 or op > 5:
        continue
    n1 = float(input("Qual o primeiro número?"))
    n2 = float(input("Qual o segundo numero número?"))
    if op == 1:
        r = n1 +n2
        print(r)
    elif op == 2:
        r = n1-n2
        print(r)
    elif op == 3:
        r = n1*n2
        print(r)
    elif op == 4:
        r = n1/n2
        print(r)
print("Obrigado por utilizar!!!")
