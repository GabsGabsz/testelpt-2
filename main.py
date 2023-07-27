def soma(valor1,valor2):
    return valor1+valor2
def subtrai(valor1,valor2):
    return valor1-valor2
def multiplica(valor1,valor2):
    return valor1*valor2
def divide(valor1,valor2):
    return valor1/valor2
def menu():
    print("1. Soma")
    print("2. Subtrai")
    print("3. Multiplica")
    print("4. Divide")
    print("5. Sair")

while(True):
    menu()
    valor1 = float(input("Qual o valor1?"))
    valor2 = float(input("Qual o valor2?"))
    opcao = input("Digite o valor da operação que você deseja realizar:")
    if opcao ==  '1':
        resultado = soma(valor1,valor2)
        print(f'O resultado da soma é:{resultado}')
    elif opcao == '2':
        resultado = subtrai(valor1,valor2)
        print(f'O resultado da subtração é:{resultado}')
    elif opcao == '3':
        resultado = multiplica(valor1,valor2)
        print(f'O resultado da multiplicação é:{resultado}')
    elif opcao == '4':
        resultado = divide(valor1,valor2)
        print(f'O resultado da divisão é:{resultado}')
    elif opcao == '5':
        break
    else:
        print("Opção inválida!")