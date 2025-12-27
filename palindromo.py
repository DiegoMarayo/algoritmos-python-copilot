# Vamos testar se uma palavra ou frase é palindroma ou não.

palavra = input("Digite uma palavra ou frase: ")
palavra = palavra.replace(" ", "").lower()
if palavra == palavra[::-1]:
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')
