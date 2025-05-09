#Peça ao usuário para digitar 5 números e mostre a soma deles ao final.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))
numero3 = int(input('Digite um terceiro número: '))
numero4 = int(input('Digite um quarto número: '))
numero5 = int(input('Digite um quinto número: '))

soma= numero1 + numero2 + numero3 + numero4 + numero5

print('A soma dos números da ' f'{soma}')

#Peça ao usuário para digitar 4 números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))
numero3 = int(input('Digite um terceiro número: '))
numero4 = int(input('Digite um quarto número: '))

listaDeNumeros = [numero1, numero2, numero3, numero4]

listaDeNumeros.sort(reverse=False)

print(f"O menor número da lista é {listaDeNumeros[0]}\nO maior número da lista é {listaDeNumeros[-1]}")


#Peça ao usuário uma palavra e mostre quantas vogais ela tem.

#Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados.
#Solicite as notas de 4 provas e mostre a média.
#Peça ao usuário um número e mostre a tabuada desse número de 1 a 10.
#Peça um número N ao usuário e mostre todos os números de 1 até N.
#Peça ao usuário uma palavra e mostre ela ao contrário.
#Peça um número ao usuário e diga se ele é múltiplo de 3.
#Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética.
