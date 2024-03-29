#Atividade 1: Calculadora no GitHub
#Nome: Arthur Rodrigues Pansera
#Turma: C

print(50*"-")
print("Menu Calculadora")
print(50*"-")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("0 - Sair")
print(50*"-")

operacao = input("Digite sua opção: ")
if operacao == "0":
    print(50*"-")
    print("Saindo...")
    print(50*"-")
elif operacao == "1" or operacao == "2" or operacao == "3" or operacao == "4":
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    if operacao == "1":
        nome = "soma"
        sinal = "+"
        resultado = numero1 + numero2
        print(50*"-")
        print(f"A operação foi {nome}: {numero1} {sinal} {numero2} = {resultado}")
        print(50*"-")
    elif operacao == "2":
        nome = "subtração"
        sinal = "-"
        resultado = numero1 - numero2
        print(50*"-")
        print(f"A operação foi {nome}: {numero1} {sinal} {numero2} = {resultado}")
        print(50*"-")
    elif operacao == "3":
        nome = "multiplicação"
        sinal = "*"
        resultado = numero1 * numero2
        print(50*"-")
        print(f"A operação foi {nome}: {numero1} {sinal} {numero2} = {resultado}")
        print(50*"-")
    else:
        nome = "divisão"
        sinal = "/"
        resultado = numero1 / numero2
        print(50*"-")
        print(f"A operação foi {nome}: {numero1} {sinal} {numero2} = {resultado}")
        print(50*"-")
else:
    print(50*"-")
    print("Operação inválida")
    print(50*"-")