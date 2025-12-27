# Vamos receber um número inteiro do usuário e verificar se ele é par ou ímpar.
while True:
    try:
        num = int(input("Digite um número inteiro: "))
        if num % 2 == 0:
            print(f"O número {num} é par.")
        else:
            print(f"O número {num} é ímpar.")
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        
