#Exercicio1:

numero= int(input('Digite sua idade:'))
if numero < 12 :
    print('É uma criança')


if numero >= 12 and numero <=17 :
        print('É um adolescente')


elif numero >= 18 :
        print ('É um adulto')

#Exercio2:

numero1= int(input('Digite um numero:'))
print(f'{numero1} é o maior numero')




if numero2 > numero1:  
    print(f'{numero2} é o maior numero')
   
    if numero1 == numero2:  
        print('Os numeros são iguais')

#Exercicio3:

letraescolhida= string = input('Digite uma letra:')
letraescolhida = letraescolhida.lower()
   
   
if letraescolhida in ('a', 'e', 'i', 'o', 'u'):
        print ('É uma vogal')


elif letraescolhida in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
     print ('É uma consoante')

#Exercicio4:

senha = int(input('Digite uma senha:'))
digitesenha= int (input ('Digite novamente a senha:'))


if senha == digitesenha:
    print('Acesso permitido')


elif senha!= digitesenha:
 print ('Senhas não coincidem')

#Exercicio5:

nota1= int(input('Digite a primeira nota:'))
nota2= int(input('Digite a segunda nota:'))
nota3=int(input('Digite a terceira nota:'))


soma= nota1 + nota2 + nota3
media= soma/3


if media>= 7:
    print(f' A média é {media} você esta aprovado')


elif media<7:
    print(f'A média é {media} você esta reprovado')

#Exercicio6:

numero1 = int(imput('Digite o primeiro número: '))
numero2 = int(imput('Digite o segundo número: '))
numero3 = int(imput('Digite o terceiro número: '))

ListaDeNumeros = [numero1, numero2, numero3]

Print('Os números em ordem decrescente são:{sorted(ListaDeNumeros reverse true)}')

#Exercicio7:

tempo= int (imput('Digite o tempo em horas: '))
velocidade= int (imput('Digite a velocidade em Km/h : '))


distancia= tempo * velocidade
LitrosUsados= distancia /12

print (f'A velocidade média é de: {velociade} Km/h \n Tempo gato na viagem foi de: {tempo} horas \n A distância percorrida foi de: {distancia} Km \n A quantiade de litros usados foi de: {LitrosUsados} L')
