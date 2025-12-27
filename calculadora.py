# Vamos solicitar como entrada dois números e depois vamos realizar operações matemáticas básicas com eles.
while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")

operacao = input("Digite a operação (+, -, *, /): ").strip()

def calcular(num1, num2, operacao):
    match operacao:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return None
            return num1 / num2
        case _:
            return None

resultado = calcular(num1, num2, operacao)

if resultado is None:
    print("Erro: Operação inválida ou divisão por zero.")
else:
    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
