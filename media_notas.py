# Vamos calcular a média de três notas fornecidas pelo usuário e determinar se o aluno foi aprovado ou reprovado.

notas = []
for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")
status = "aprovado" if media >= 7 else "reprovado"
print(f"O aluno foi {status}.")
