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

palavra= input('Digite uma palavra: ')
vogais = ['a', 'e', 'i', 'o', 'u']
contadordevogais= 0

for letra in palavra: 
  for vogal in vogais: 
    if (letra==vogal):
      contadordevogais += 1
      
print (f'A quantidade de vogais na palavra {palavra} é de {contadordevogais} ')

#Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um segundo número: '))
numero3 = int(input('Digite um terceiro número: '))
numero4 = int(input('Digite um quarto número: '))
numero5 = int(input('Digite um quinto número: '))
numero6 = int(input('Digite um sexto número: '))

if numero1 % 2 == 0 :
 print(f'{numero1} é um número par')


if numero2 % 2 == 0 :
 print(f'{numero2} é um número par')

if numero3 % 2 == 0 :
 print(f'{numero3} é um número par')

if numero4 % 2 == 0 :
 print(f'{numero4} é um número par')

if numero5 % 2 == 0 :
 print(f'{numero5} é um número par')

if numero6 % 2 == 0 :
 print(f'{numero6} é um número par')
 
#Solicite as notas de 4 provas e mostre a média.

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceiro nota: '))
nota4 = int(input('Digite a quarta nota: '))

soma= nota1 + nota2 + nota3 + nota4
media= soma/4

print (f'A média é {media}')

#Peça ao usuário um número e mostre a tabuada desse número de 1 a 10.
numero= int(input('Digite um número: '))

print("Tabuada do ", numero)

for numero2 in range(1,11):
        print(numero, "x", numero2, " = ", numero * numero2)

#Peça um número N ao usuário e mostre todos os números de 1 até N.

#Peça ao usuário uma palavra e mostre ela ao contrário.
#Peça um número ao usuário e diga se ele é múltiplo de 3.
#Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética.
