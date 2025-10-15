from sre_constants import OP_UNICODE_IGNORE


texto='2' #declaração de variável string
texto1= str(2) #declaração de variável do tipo string
numero=4.7 #declaração de variável numerica, podendo ser inteia ou real
numero1=int(9) #declaração de variável numerica, do tipo inteiro
numero2=float(5) #declaração de variável numerica, do tipo real
print(texto)
print(texto1)
print(numero)
print(numero1)
print(numero2)
#######################################################################################
#Operador de Divisão inteira
divisaointeira = n1 // n2

#Operador de potência
potencia = n1 ** n2

#Operador módulo
restodaDivisão = n1 % n2
#########################################################################################
#1) Faça um programa que leia um númro de 0 a 9999 e mostre na tela um dos dígitos separados.

#Atribui dados digitados pelo usuario e converte em numero inteiro.
numeroInteiro = int(input('Digite um numero Inteiro: '))

numero= int(input('Digite um número de 0 a 9999: '))
unidade= numero%10
dezena= (numero//10) % 10
centena= (numero//100) % 10
milhar= (numero//1000) % 10

print(f'unidade: {unidade}\n','dezena: {dezena}\n','centena: {centena}\n','milhar: {milhar}\n') 
#######################################################################################
#2) Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
cidade=input('Digite o nome de uma cidade:\n '.lower())
print('santo' in cidade[:5])
#######################################################################################
#3) Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome =input('Digite um nome:\n '.lower())
print('silva' in nome)
#######################################################################################
#4) Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
num= int(input('Digite um número: '))
if num % 2 == 0:
  print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')
  
  ou

num=int(input('Digite um número:')) 
print('par' if num % 2 == 0 else 'impar')

#######################################################################################
#5) Desenvolva um programa que pergunte a distância de uma
#viagem em Km. Calcule o preço da passagem cobrando R$
#0,50 por Km para viagens de até 200 Km e R$ 0,45 para
#viagens mais longas.

distancia= float(input('Digite a distancia de sua viagem em Km: '))
if distancia>200:
  print('O valor da passagem é de R${:,.2f}'.format(distancia*0.45))
else:
   print('O valor da passagem é de R${:,.2f}'.format(distancia*0.50))

#######################################################################################
#6)Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO. O ano bissexto ocorre a cada 4 anos (exceto em anos múltiplos de 100 que não são múltiplos de 400)

ano= int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano é bissexto')
else:
  print('O ano não é bissexto')

#######################################################################################
#7) Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
n3= int(input('Digite o terceiro número: '))
maior = n1
menor = n1
if (n2 > maior):
 maior = n2
if (n3 > maior):
  maior = n3
if (n2 < menor):
  menor = n2
if (n3 < menor):
  menor = n3
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')

Ou

print('DIGITE OS TRÊS NÚMEROS\n')
nums= [int(input('Digite o número: ')) for _  in range (3)]
print(f'maior número: {max(nums)}\nmenor número: {min(nums)}')
#######################################################################################
#8) Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#Condições Necessárias:
#a + b > c
#a + c > b
#b + c > a

rt1= float(input('Digite a primeira reta: '))
rt2= float(input('Digite a segunda reta: '))
rt3= float(input('Digite a terceira reta: '))
if rt1 < rt2 + rt3 and rt2 < rt1 + rt3 and rt3 < rt1 + rt2:
  print('As retas podem formar um triângulo')
else:
  print('As retas não podem formar um triângulo')
###########################################################
vl= float(input('Digite o valor da casa: '))
sl= float(input('Digite o salário do comprador: '))
anos= int(input('Digite em quantos anos deseja pagar: '))
anos *= 12
sl *= 0.3
vl /= anos
if vl > sl:
  print(f'Empréstimo negado!\n30% do salario: R${sl:,.}')
else:
  print(f'Empréstimo aprovado\n30% do salario: R${sl:,.2f}\n'f'parcela: {vl:,.2f}')
##########################################################
num= int(input('Digite um número: '))
opcao= int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
if opcao == 1:
  print(f'O número {num} em binário é {bin(num)[2:]}')
elif opcao == 2:
  print(f'O número {num} em octal é {oct(num)[2:]}')
else:
  print(f'O número {num} em hexadecimal é {hex(num)[2:]}')
##########################################################
n1= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
if (n1 > n2):
 print('O primeiro números é maior')
elif (n2 > n1):
 print('O segundo número é maior')
else:
 print('Os números são iguais')
 #########################################################
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos')
if idade < 18:
    print(f'falta(m) {18 - idade} ano(s) para você se alistar')
elif idade == 18:
    print('Você está na hora de se alistar')
else:
    print(f'Você já passou {idade - 18} ano(s) do tempo de alistamento ano(s) do tempo de alistamento')
##########################################################
nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
media= (nota1 + nota2) / 2
if media >= 7.0:
 print('Aprovado')
elif media >= 5.0:
  print('Recuperação')
else:
 print('Reprovado')
##########################################################
ano_nascimento= int(input('Digite o ano de nascimento: '))
ano_atual= int(input('Digite o ano atual: '))
idade= ano_atual - ano_nascimento
OU!!
idade=2024- int(input('Digite o ano de nascimento: '))

if idade <= 9:
  print(f'O atleta possui {idade} anos\nCategoria Mirim')
elif idade <= 14:
 print(f'O atleta possui {idade} anos\nCategoria Infantil')
elif idade <= 19:
  print(f'O atleta possui {idade} anos\nCategoria Junior')
elif idade <= 24:
 print(f'O atleta possui {idade} anos\nCategoria Sênior')
else:
  print(f'O atleta possui {idade} anos\nCategoria Master')
##########################################################
rt1= float(input('Digite a primeira reta: '))
rt2= float(input('Digite a segunda reta: '))
rt3= float(input('Digite a terceira reta: '))
if rt1 < rt2 + rt3 and rt2 < rt1 + rt3 and rt3 < rt1 + rt2:
  print('As retas podem formar um triângulo')
else:
  print('As retas não formam um triângulo')

if rt1 == rt2 == rt3:
  print('Triângulo equilátero')
elif rt1 == rt2 or rt1 == rt3 or rt2 == rt3:
  print('Triângulo isósceles')
else:
  print('Triângulo escaleno')
##########################################################
altura= float(input('Digite sua altura (m): '))  
peso= float(input('Digite seu peso (kg): '))
imc= peso / (altura * altura)
if imc < 18.5: 
  print('Você está abaixo do Peso')
elif imc <= 25: 
  print('Você está com o peso ideal')
elif imc <= 30: 
  print('Você está com sobrepeso')
elif imc <= 40: 
 print('Você está com obesidade')
else:
 print('Você está com obesidade Mórbida')
##########################################################
preco= float(input('Digite o preço do produto: '))
print('FORMAS DE PAGAMENTO\n[1] à vista dinheiro: 10% de desconto\n[2] à vista no cartão: 5% de desconto\n[3] 2x no cartão: preço normal\n[4] 3x ou mais no cartão: 20% de juros')
opcao= int(input('Digite a opção de pagamento: '))
if opcao == 1:
  print(f'O valor do produto com desconto é R${preco * 0.10}')
elif opcao == 2:
  print(f'O valor do produto com desconto é R${preco * 0.05}')
elif opcao == 3:
  print(f'O valor do produto parcelado em 2x é R${preco}')
else:
  print(f'O valor do produto parcelado em 3x ou mais é R${preco * 1.20}')
##########################################################
print('ESCOLHA UMA DAS OPÇÕES: pedra, papel, tesoura')
import random
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
jogador = input('Digite sua escolha: ').lower()
if jogador == pc:
  print('Empate')
elif (jogador != pc) % 3 == 0:
  print('Você venceu')
else:
  print('Você perdeu')

ou 

import random
print('ESCOLHA UMA DAS OPÇÕES: pedra, papel, tesoura')
pc= random.choice(['pedra', 'papel', 'tesoura'])
jogador = input('Digite sua escolha: ').lower()
if jogador == pc:
  print('Empate')
elif (jogador != pc) % 3 == 0:
  print('Você venceu')
else:
  print('Você perdeu')
##########################################################
#teste usando for in range  

inicio= int(input('Informe o primeiro número: '))
fim= int(input('Informe o número final: '))
salto= int(input('Informe o salto: '))
texto= 'Calculo: '
soma= 0
for numero in range(inicio, fim, salto):
    soma= soma + numero
    texto= texto + str(numero)
    if numero > 50:
        texto= texto + '\nPassou de 50'
        break
    if numero != fim-1:
        texto= texto + '+'
print(f'{texto}')
print(f'soma: {soma}')
##########################################################
for contagem in range (10,-1,-1):
  print(contagem)
########################################################
for pares in range (1,51):
  if pares % 2 == 0:
      print(pares)
else:
  print('Acabou')
########################################################
import time
for contagem in range (10,-1,-1):
  print(contagem)
  time.sleep(1)
#######################################################
soma2=0
for impares in range (1,501):
  if impares %2==1 and impares%3==0:
    soma2 += impares
print(f'A soma de todos o número é {soma2}')
#######################################################
numero= int(input('informe o número da tabuada que deseja ver:'))
for tabuada in range (1,11):
  print(f'{numero} x {tabuada} = {numero * tabuada}')
Ou 
for numero in range(11):
  for tabuada in range(11):
     print(f'{numero} x {tabuada} = {numero * tabuada}')
#######################################################
soma=0
for x in range(1,7):
  num=int(input(f'digite o {x} número: '))
  if num %2==0:
    soma=soma + num
print(f'Soma dos números',soma)
######################################################
primeiro_termo= int(input("Digite o primeiro termo da PA: "))
razao= int(input("Digite a razão da PA: "))

for x in range(10):
  termo = primeiro_termo + (x * razao)
  print(f"Termo {x+1}: {termo}")
######################################################
num= int(input('Digite um número: '))
primo = True
for i in range(2, int(num**0.5) + 1):
  if num % i == 0:
    primo = False
    break
    print(f"{num} não é um número primo.")
else:
  print(f"{num} é um número primo.")
#########################################################
frase= input('Digite uma frase: ').replace('','')
for x in range(len(frase)):
  if frase[x] != frase[-x-1]:
   print(f'A frase ({frase}) é um palíndromo')
   break
else:
  print(f'A frase ({frase}) não é um palíndromo')
Ou 
correta
frase= 'A TORRE DA DERROTA'.replace('','')
inverso=frase[::-1]
print('palindromo'if frase==inverso else 'Não é um palindromo')
#################################################################
from datetime import date
ano_atual = date.today().year
maior=0
menor=0
for _ in range(1,8):
    ano_nascimento= int(input('Digite o ano de nascimento: '))
    idade= ano_atual - ano_nascimento
    if idade >= 18:
        maior +=1
    else:
        menor +=1
print(f'Pessoas maiores de idade: {maior}')
print(f'Pessoas menores de idade: {menor}')
###################################################################
peso= [float(input('Digite o Peso Kg: ')) for _ in range(5)]
print(f'maior peso Kg: {max(peso):,.2f}\nmenor peso Kg: {min(peso):,.2f}')
####################################################################
media = 0
homemNome = ""
homemIdade = 0
mulheres_20 = 0
for x in range(1,5):
    nome = input(f'Digite o nome {x} pessoa: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').upper()
    media += idade
    if sexo == 'M' and (homemIdade == 0 or idade > homemIdade):
        homemNome = nome
        homemIdade = idade
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
idadeMedia = media / 4
print(f'A média de idade do grupo é {idadeMedia:.2f}')
if homemNome:
    print(f'O homem mais velho é o {homemNome} com {homemIdade} anos.')
else:
    print('Nenhum homem no grupo.')
print(f'Há {mulheres_20} mulheres com menos de 20 anos.')
####################################################################
while True:
  sexo= input('Qual o sexo? (M/F): ')
  if sexo in 'M/F':
    print('Sexo valido')
    break
  print('Digite novamente...')
  #ou sem braeak
  
fim=''
while fim!='m' and fim!='f':
  fim= input('Digite (M/F): ').lower()
  
####################################################################
import random

pc = random.randint(a=0, b=10)
tentativas=0
while True:
    jogador = int(input('Digite um número: '))
    tentativas +=1
    if pc == jogador:
        print('Acertou')
        print(f'tentativas {tentativas}')
        break
    print('Errou,continue tentando...')
######################################################
n1,n2=int(input('Digite o primeiro número: ')),int(input('Digite o segundo número: '))
print('Digite o que você deseja fazer com os números digitados')
while True:
  print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
  opcao= int(input('Digite a opção: '))
  if opcao == 1:
    print(f'A soma dos números é {soma}')
  elif opcao == 2:
    print(f'A multiplicação dos números é {n1*n2}')
  elif opcao == 3:
    print(f'O maior número é {maior}')
  elif opcao == 4:
    n1,n2=float(input('Digite o novo número: ')),float(input('Digite o novo número: '))
  elif opcao == 5:
    print('Finalizando...')
    break
  else:
    print('Erro,Tente novamente')
################################################################################################
n1, n2 = float(input('Digite o primeiro número: ')), float(input('Digite o segundo número: '))
print('Digite o que você deseja fazer com os números digitados')
while True:
  print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
  opcao = int(input('Digite a opção: '))
  if opcao == 1:
    print(f'A soma dos números é {n1 + n2}\n')
  elif opcao == 2:
    print(f'A multiplicação dos números é {n1 * n2}\n')
    if opcao == 3:
     print(f'O maior número é {n1}\n')
    else:
        print(f'O maior número é {n2}\n')
  elif opcao == 4:
      n1, n2 = float(input('Digite o novo número: ')), float(input('Digite o novo número: '))
  elif opcao == 5:
    print('Finalizando...')
     break
  else:
    print('Erro,Tente novamente')
#####################################################################################################
while True:
  num = int(input('Digite um número: '))
  if num == 0:
    print('saindo...')
    break
  fatorial=1
  x = num
  print(f'{num}! =', end='')
while x > 0:
  fatorial *= x
  print(f'{x}', end='x' if x > 1 else '=')
  x -= 1
print(f'O fatorial de {num} é {fatorial}')
    
#Ou 
    
fatorial=1
num = int(input('Digite um número: '))
print(f'{num}! = ',end='')
while num > 1:
  fatorial *= num
  print(num,end='x')
  num -= 1
print(f'1 = {fatorial}')
#####################################################################################################
primeiro_termo= int(input("Digite o primeiro termo da PA: "))
razao= int(input("Digite a razão da PA: "))
cont= 10
while cont <= 10:
  print(f'{primeiro_termo},end='->' if cont == 10: print(f'{primeiro_termo + (cont - 1) * razao}')
  termo = primeiro_termo + razao
  cont += 1
  print(f"Termo: {termo}")

primeiro_termo= int(input("Digite o primeiro termo da PA: "))
razao= int(input("Digite a razão da PA: "))
cont= 10
while cont <= 10:
  print(f'{primeiro_termo} ->', end='')
  termo = primeiro_termo + razao
  cont += 1
  print(f"Termo: {termo}")
  #terminar
###########################################################################
#Escreva um programa que leia um número n inteiro qualquer e mostre
#na tela os n primeiros elementos de uma sequência de Fibonacci.

num=int(input('Digite um número: '))
fib1=0
fib2=1
print(f'{fib1} -> {fib2}', end='')
cont=3
while cont <= num:
  fib= fib1 + fib2
  print(f' -> {fib}', end='')
  fib1=fib2
  fib2=fib
  cont += 1

#ou

num=0
cont=int(input('Digite quantos termos deseja ver: '))
resultado=0
numSeguinte=num+1
while cont > 0:
resultado=num+numSeguinte
print(f' {resultado} = {num} + \033[1:33:33m{numSeguinte}\033[m)
num=numSeguinte
numSeguinte=resultado
cont-=1
######################################################################
#Crie um programa que leia vários números inteiros pelo teclado. No
#final da execução, mostre a média entre todos os valores e qual foi o
#maior e o menor valores lidos.O programa deve perguntar ao usuário
#se ele quer ou não continuar a digitar valores

for x in range(1,5)
  num=(int(input(f'Digite o {x} número: '))
  media= x / 5
  print(f'A média dos números é: {media}')
  max=x
  min=x
  if x > max:
    print(f'O maior número é: {max}')
  else:  
    print(f'O menor número é: {min}')
while True:
  continuar= input('Deseja continuar? (S/N): ').upper()
  if continuar == 'S':
    print('carregando aguarde um momento...')
    else:
      print('Terminando programa...')
#arrumar codigo!!!
max=''
min=''
for x in range(1,5):
    num = (int(input(f'Digite o {x} número: '))
    media= num / 5
    print(f'A média dos números é: {media}')
    if x > max:
        print(f'O maior número é: {max}')
    else:
        print(f'O menor número é: {min}')
while True:
    continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar == 'S':
        print('carregando aguarde um momento...')
        else:
        print('Terminando programa...')
########################################################################################################
#68
#Faça um programa que jogue par ou impar com o computador. O jogo
#só será interrompido quando o jogador perder, mostrando o total de
#vitorias consecutivas que ele conquistou no final do jogo.
import random

While True:
    num1=radom.randint(a=0, b=10)
    num=int(input('Digite o numero: '))
    soma=num+num1
    menu= input('Par ou Impar\n\nEscolha:')
    if menu == 'par':
        if soma%2==0:
         placar = placar + 1
         print(f'Pc: {num1}')
         print('Par ganhou')
         print(f'Jogador ganhou {placar} vezes seguidas')
            
        else:
            print(f'Pc: {num1}')
            print('Impar ganhou')
            print(f'Jogador perdeu {placar} vezes seguidas')
            break

    else:
        if soma%2==0:
            print(f'Pc: {num1}')
            print('Pc ganhou par venceu')
            break
        else:
            placar +=1
            print(f'Pc:{num1}')
    print(f'Jogador ganhou {placar} vezes seguidas')
#####################################################################################################
#DESAFIO 69
#Crie um programa que leia a idade e o sexo de varias pessoas. A cada
#pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
#não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.anos.

pessoas=0
homens = 0
mulheres_20 = 0
idade = int(input('Digite a idade: '))
sexo = (input('Digite o sexo (M/F): ')).upper()

while True:
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    cont = (input('Deseja continuar S/N: ')).upper()
    if cont == 'S':
        break
print(f'No programa de cadastro possui {pessoas} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'No programa de cadastro possui {mulheres} mulheres com menos de 20 anos')
#####################################################################################################
#Crie um programa que leia o nome e o preço de vários produtos. O
#programa deverá perguntar se o usuário vai continuar. No final,
#mostre:
barato=0
preco=0
pBarato=''
produtos=0
total=0
while True:
    nome= input('Digite o nome do produto: ')
    preco= float(input(f'Digite o preço do produto: '))
    total+=preco
    if preco > 100:
        produtos+=1
    if barato == 0 or preco < barato:
        barato=preco
        pBarato=nome
        cont = (input('Deseja continuar S/N: '))
    if cont == 'N':
        break
print(f'O total gasto foi de: {round(total, 2)}')
print(f'{produtos} Custam mais de R$ 100,00 reais')
print(f'O produto mais barato foi ({pBarato}) que custa R$:{barato}')
####################################################################################################
#Crie um programa que simule o funcionamento de um caixa
#eletrônico. No início, pergunte ao usuário qual será o valor a ser
#sacado (número inteiro) e o programa vai informar quantas cédulas de
#cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
 
valor=int(input('Digite o valor a ser sacado R$: '))
total=valor
ced=50
totalced=0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            sair = input('Deseja sair? (S/N): ').lower()
        if sair == 'S':
            break
#Arrumar
##################################################################################################
#Exemplos de alguns comandos 
lista = [1,2,3,4,5]
print(lista)
lista.append(2)
print(lista)
lista.insert(2,-3)
print(lista)
lista.remove(4)
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)

#e
qtd = lista.count(5)
print(qtd)
exc = lista.pop()
print(lista)
print(exc)
del lista[2]
print(lista)
del lista[2:5]
print(lista)
lista.clear()
print(lista)

#e
novo = []
while True:
  num=int(input('Digite um número inteiro(0 para sair): '))
  if num == 0:
    break
    nova.append(num)
    print(nova)
    
#e
serieB=random.shuffle(serieB)  (embaralha a lista!!)
serieB=random.choice(serieB)   (vai sortear os times)
serieB.sort(reverse=True)
#################################################################################################
#DESAFIO 78
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
lista = []
while True:
  nums=int(input('Digite o número desejado para armazenar(digite 0 para sair): '))
  if nums==0:
    break
  lista.append(nums)
print(lista)
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
print(f'O maior número é: {max(lista)} e sua posição na lista é a:', lista.index(max(lista)))
print(f'O menor número é: {min(lista)} e sua posição na lista é a:',lista.index(min(lista)))

#ou
numero=list(int(input(f'Digite o {x+1} número: ')) for x in range(1,6))
print(f'O maior número é: {max(numero)}' numero.index(max(numero)))
print(f'O menor número é: {min(numero)}' numero.index(min(numero)))

#ou
numeros=[]
maior=0
menor=float('inf')

for x in range(1,6):
  num=int(input('Digite um número:'))
  numeros.append(num)
  if num < menor:
    menor=num
  if num > maior
    maior=num
    
print(f'O maior número é: {maior}' numero.index(maior))
print(f'O menor número é: {menor}' numero.index(menor))
#####################################################################################################
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
nums=0
lista = []
while True:
    nums= int(input('Digite o número desejado para armazenar(digite 0 para sair): '))
    if nums == 0:
        break
    # Caso o número já exista lá dentro, ele não será adicionado.
    if nums in lista:
        print(f'O número {nums} já foi adicionado tente outro...')
    else:
        print(f'O número {nums} foi adicionado')
    lista.append(nums)
# No final serão exibidos todos os valores únicos digitados, em ordem crescente.
    lista.sort()
print(lista)

#ou
nums=0
lista = []
while True:
    nums= int(input('Digite o número desejado para armazenar(digite 0 para sair): '))
    if nums == 0:
        break  
    if nums not in lista:
        lista.append(nums)
lista.sort()
  print(lista)
#ou
nums=0
lista = []
while True:
    nums=input('Digite o número desejado para armazenar(digite sair): ')
    if nums.lower == 'sair':
        break  
    if nums.isnumeric():
        nums=int(nums)
    if nums not in lista:
        lista.append(nums)
lista.sort()
  print(lista)
#####################################################################################################
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na sua posição correta de inserção (sem usar o sort()).
#No final mostre a lista ordenada na tela
numeros=[]
mum=0
for x in range(1,6):
    num=int(input(f'Digite 0 {x}'' numero:\n'))
    numeros.append(num)
for j in range(len(numeros)):
    for i in range (len(numeros)):
        if numeros[j] < numeros[i]:
            numeros[j],numeros[i] = numeros[i],numeros[j]
            print(numeros)
print(numeros)
#ou!! teste 
maior=0
menor=0
meio=0
lista = []
for x in range(1,6):
    nums = int(input('Digite o número desejado para armazenar: '))
    if x == 0:
        maior = menor = nums
        lista.append(nums)
    elif nums >= maior:
        maior = nums
        numeros.append(nums)
    elif nums <= menor:
        menor = nums
        lista.insert(0, nums)
    elif menor < nums < maior:
        if meio == 0:
            meio = nums
            lista.insert(menor < nums < maior, nums)
        elif meio <= nums:
            numeros.insert(meio < nums < maior, nums)
            meio = nums
        elif meio >= nums:
            lista.insert(menor < nums < meio, nums)
print(lista)
#####################################################################################################
# DESAFIO 81
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
nums=0
lista = []
contador=0
while True:
    nums =input('Digite o número desejado para armazenar(digite sair): ')
    if nums.isnumeric():
        nums = int(nums)
    contador += 1
    if nums == 'sair':
        break
    lista.append(nums)
# B) A lista de valores, ordenada de forma decrescente.
    lista.sort(reverse=True)
# C) Se o valor 5 foi digitado e esta ou não na lista.
print('O 5 está na lista' if 5 in lista else 'O 5 não está na lista')
# A) Quantos números foram digitados.
print(contador,len(lista))
print(lista)
#####################################################################################################
#Desafio 82
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e impares digitados.
#Ao final, mostre o conteúdo das três listas geradas.
nums=0
lista=[]
lista2=[]
lista3=[]
while True:
    nums=int(input('Digite um número (Ou digite 0 para encerrar): '))
    if nums % 2 == 0:
        lista2.append(nums)
    else:
        lista3.append(nums)
    if nums == 0:
        break
    lista.append(nums)
    lista.sort()
print(lista)
print(lista2)
print(lista3)
#ou
nums=0
lista=[]
lista2=[]
lista3=[]
while True:
    nums=input('Digite o número desejado para armazenar(digite sair): ')
    if nums.isnumeric():
        nums = int(nums)
    if nums == 'sair':
        break
    if nums % 2 == 0:
        lista2.append(nums)
    else:
        lista3.append(nums)
    lista.append(nums)                                                          
    lista.sort()
print(lista)
print(lista2)
print(lista3)
###################################################################################
import random

# simule o campeonato
nums = 0
lrio-PR',
          'Botafogo-SP', 'Brusque', 'Ypiranga-RS', 'América-RN', 'Amazonas', 'Águia de Marabá', 'Sousa-PB']ista = ["Flamengo", "Palmeiras", "São Paulo", "Athletico-PR", "Atlético-MG", "Corinthians", "Fluminense", "Grêmio",
         "Fortaleza", "Internacional", "Bahia", "Botafogo", "Red Bull Bragantino", "Atlético-GO", "Ceará", "Cuiabá"]
lista2 = ['Goiás', 'Vasco', 'Juventude', 'Sport', 'CRB', 'Vitória', 'Criciúma', 'Sampaio Corrêa', 'Operá
# A-sorteio dos jogos
print('======Copa Do Brasil======')
print('-----Lista De Times-----')
print(lista)
print(lista2)
print('====Sorteio Dos Jogos====')
print('---Jogos do 1° Turno---')
for x in range(0, 16):
    time1 = random.choice(lista)
    time2 = random.choice(lista2)
    print(f'{time1} x {time2}')
# B-listar os classificados por turno e #C-placares dos jogos
print('======Classificados======')


# D-Campeão
#terminar
#####################################################################################################
import random
import time

lista1=["Flamengo", "Palmeiras", "São Paulo", "Athletico-PR", "Atlético-MG" ,"Corinthians" ,"Fluminense", "Grêmio", "Fortaleza", "Internacional", "Bahia", "Botafogo", "Red Bull Bragantino", "Atlético-GO", "Ceará","Cuiabá"]
lista2=['Goiás', 'Vasco', 'Juventude', 'Sport', 'CRB', 'Vitória', 'Criciúma', 'Sampaio Corrêa' ,'Operário-PR' ,'Botafogo-SP', 'Brusque', 'Ypiranga-RS', 'América-RN', 'Amazonas', 'Águia de Marabá', 'Sousa-PB']
oitavas=[]
timeA=''
timeB=''
golsA=0
golsB=0
while len (lista1) > 0:
    timeA = random.choice(lista1)
    timeB = random.choice(lista2)
    golsA=random.randint(0,3)
    golsB=random.randint(0,3)
    if golsB != golsA:
        print(f'{timeA} {golsA} x {golsB} {timeB}')
    if golsB > golsA:
        lista1.remove(timeA)
        lista2.remove(timeB)
        oitavas.append(timeB)
    else:
        lista1.remove(timeA)
        lista2.remove(timeB)
        oitavas.append(timeA)
time.sleep(3)
print('\n\nOs classificados são:')
for pos, time in enumerate(oitavas):
    print(pos+1,time)

oitavas1=oitavas[:8]
oitavas2=oitavas[8:]
print(len(oitavas1))
print(len(oitavas2))
#terminar
#####################################################################################################
import time


#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
#Campeonato Brasileiro Serie B de Futebol, na ordem de colocação. Depois
#mostre:

serieB="América-MG", "Goiás", "Avaí", "Santos", "Sport", "Ceará", "Operário-PR", "Mirassol", "Coritiba" , "Vila Nova", "Novorizontino" ,"Amazonas", "Chapecoense" ,"Ponte Preta", "CRB" ,"Paysandu", "Botafogo-SP" ,"Ituano", "Brusque" ,"Guarani"
print('Os vinte colocados do campeonato\n')
for tabela in serieB:
    time.sleep(1)
    print(tabela)
time.sleep(2)
print('\n')
#A) Apenas os 5 primeiros colocados.
print('Os cinco primeiros são...\n')
for x, primeiros in enumerate(serieB[:5]):
    time.sleep(1)
    print(x+1 ,primeiros)
time.sleep(2)
print('\n')
#B) Os últimos 4 colocados da tabela.
print('Os quatro ultimos são...\n')
for pos, ultimos in enumerate(serieB[16:]):
    time.sleep(1)
    print(pos+17, ultimos)
#C) Uma lista com os times em ordem alfabética.
time.sleep(2)
print('\n')
print('Times da serieB em ordem alfabetica ')
print('\n')
for c, ordemAlfabetica in enumerate(sorted(serieB)):
    time.sleep(1)
    print(c+1, ordemAlfabetica)
time.sleep(2)
#D) Em qual posição na tabela está o time do Santos.
print('\n')
print('Posição do Santos no campeonato')
print(f'O santos esta na: {serieB.index("Santos")+1} posição')
#####################################################################################################
import random


#Crie um programa que vai gerar cinco números aleatórios e colocar
#em uma tupla.
numeros=[]
for x in range (5):
    num=random.randint(1,10)
    numeros.append(num)
#Depois disso, mostre a listagem de números gerados e também
tupla=tuple(numeros)
print(tupla)
print('\n')
#indique o menor e o maior valor que estão na Tupla.
print(f'O maior número na tupla é: {max(tupla)}\nO menor número na tupla é: {min(tupla)}')
####################################################################################################
#Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:
numeros=[]
num=0
for x in range(4):
    num=int(input(f'Digite um {x+1} numero: '))
    numeros.append(num)
tupla = tuple(numeros)
print(tupla)
print(f'O número 9 apareceu: {numeros.count(9)} vezes' if 9 in numeros else 'Não apareceu na tupla')
#terminar
####################################################################################################
#Crie um programa que tenha uma tupla com várias palavras (não usar
#acentos). Depois disso você deve mostrar, para cada palavra, quais são
#as suas vogais.
numeros=("zero", "um", " dois" ,"três" ,"quatro", "cinco", "seis", "sete",
" oito" ,"nove", "dez" ," onze" ," doze" ," treze", "quatorze ou catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")
vogais=["a", "e", "i", "o", "u"]
for palavras in numeros:
    print(palavras)
    for letras in vogais:
        if letras in vogais:
            print(letras)
####################################################################################################
estado={}
brasil=list()

for c in range(2):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
####################################################################################################
#Faça um programa que leia o nome e média de um aluno, guardando
#também a situação em um dicionário. No final mostre o conteúdo da
#estrutura na tela.
aluno={}
lista=[]
while True:
    aluno['nome']=input('Digite o nome do aluno: ')
    aluno['média']=float(input('Digite a media do aluno: '))
    if aluno['média'] < 5:
        aluno['situacao']='Reprovado'
    elif aluno['média'] >= 5 and aluno['média'] <= 6:
        aluno['situacao']=' Recuperação'
    else:
        aluno['situacao']='Aprovado'
    lista.append(aluno.copy())
    sair = input('Deseja sair? S/N: ')
    if sair == 'S':
        break
    for x in lista:
        for chave, valor in x.items():
            print(f'{chave} : {valor}')
#print(f'O aluno {aluno['nome']}, tirou nota {aluno['média']}, e ele {aluno['situacao']}')
####################################################################################################
#Crie um programa onde 4 jogadores joguem um dado e tenham
#resultado aleatórios. Guarde esses resultados em um dicionário . No
#final, coloque esse dicionário em ordem, sabendo que o vencedor
#tirou o maior numero no dado.
#dado=int(input("\nQuantas faces deseja que o dado virtual possua?"))
from random import randint
jogador={}
lista=[]

for x in range(1,5):
    jogador['nome']=input(f'Digite o nome do {x} jogador: ')
    jogador['jogada']=randint(1,6)
    lista.append(jogador.copy())
print(lista)

for j in range(len(lista)):
    for i in range(len(lista)):
        if (lista[j]['jogada']) < lista[i]['jogada']:
            lista[j]['jogada'], lista[i]['jogada'] = lista[i]['jogada'], lista[j]['jogada']
            lista[j]['nome'], lista[i]['nome'] = lista[i]['nome'], lista[j]['nome']
for x in lista:
    for k,v in x.items():
        print(f'{k},{v}')
        print('----------------')
#arrumar o codigo de baixo
        from random import randint
        jogador={}
        lista=[]

        for x in range(1,5):
            jogador['nome']=input(f'Digite o nome do {x} jogador: ')
            jogador['jogada']=randint(1,6)
            lista.append(jogador.copy())
        print('Os jogadores são: ')
        for name, lista in enumerate(lista[:]):
            print(name+1,lista)

        for j in range(len(lista)):
            for i in range(len(lista)):
                if (lista[j]['jogada']) < lista[i]['jogada']:
                    lista[j]['jogada'], lista[i]['jogada'] = lista[i]['jogada'], lista[j]['jogada']
                    lista[j]['nome'], lista[i]['nome'] = lista[i]['nome'], lista[j]['nome']
        for x in lista:
            for k,v in x.items():
                print(f'{k},{v}')
                print('----------------')
####################################################################################################
#Crie um programa que leia nome, ano de nascimento e carteira de
#trabalho e cadastre-os (com idade) em um dicionário se por acaso o
#CTPS for diferente de ZERO, o dicionário receberá também o ano de
#contratação e o salário. Calcule e acrescente, além da idade, com
#quantos anos a pessoa vai se aposentar.

#Sabendo que ele vai se aposentar após 35 anos de colaboração!!.

pessoa={}



pessoa['nome']=(input('Digite o nome da pessoa: '))
pessoa['anoNascimento']=int(input('Digite o ano de nascimento: '))
pessoa['anoAtual']=int(input('Digite o ano atual: '))
pessoa['idade']=pessoa['anoAtual']-pessoa['anoNascimento']
pessoa['ctps']=int(input('já trabalhou? se sim em quantos empregos: '))
pessoa['ctpstempo']=0
if pessoa['ctps'] != 0:
    for x in range(pessoa['ctps']):
        pessoa['salario'] = float(input(f'Digite o {x+1} sálario: '))
        pessoa['ctpstempo']= int(input('Tempo de serviço: '))
        if pessoa['ctpstempo'] == 35:
            print('Você já pode dar entrada na sua aposentadoria')
        if pessoa['ctpstempo'] > 35:
            print('Já passou do temo de se apossentar')

pessoa['aposentadoria']=(35-pessoa['ctpstempo'])+pessoa['idade']
print(pessoa['aposentadoria'])
####################################################################################################
#Crie um programa que gerencie o aproveitamento de um jogador de
#futebol. O programa vai ler o nome do jogador e quantas partidas
#ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total
#de gols feitos durante o campeonato.
jogador={}
lista=[]

jogador['nome']=input('Nome do jogador: ')
jogador['partidas']=int(input('quantidade de partidas jogadas: '))

for x in range(jogador['partidas']):
    jogador['gols']=int(input(f'Digite os gols da {x+1} partida: '))
    lista.append(jogador['gols'])
jogador['totalGols'] = sum(lista)
print(f'O total de gols do jogador é de: {jogador['totalGols']} gols')

#ou

jogador={}
lista=[]
jogador['nome']=input('Digite seu nome: ')
jogador['partidas']=int(input('Digite o numero de partidas: '))
for x in range(jogador['partidas']):
    jogador['partida']=x+1
    jogador['gols']=int(input(f'digite o numero de gols da {x+1}º partida:'))

    lista.append(jogador.copy())
jogador['total de gols']= 0
for j in range(len(lista)):
    jogador['total de gols']+=lista[j]['gols']

for r, t in jogador.items():
    if r =='nome' or r== 'partidas':
        print(f'{r}: {t}')
for z in lista:
    for k,v in z.items():
        if k !='nome' and k!= 'partidas':
            print(f'{k}: {v}')
for l,i in jogador.items():
    if l =='total de gols':
        print(f'{l}: {i}')
####################################################################################################
#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de casa pessoa em um dicionário e todos os
#dicionários em uma lista. No final, mostre:

#D) Uma lista com todas as pessoas com idade acima da média.
pessoa={}
listaM=[]
listaMed=[]
listaAll=[]
media=0
contador=0

while True:
    nome=input('Digite o nome: ')
    idade=int(input('Digite a idade: '))
    sexo=input('Digite o sexo: (H/M): ').lower
    #A) Quantas pessoas foram cadastradas.

    listaAll.append()
    contador+=1
    #C) Uma lista com todas as mulheres.

    if pessoa['sexo']=='m':
        listaM.append(pessoa.copy())
    #B) A média de idade do grupo.
    media+=pessoa['idade']
    sair=input('Deseja sair? (s/s)')
    if sair.lower()=='s':
        break
media/=contador
print(f'Pessoas cadastradas foram: {contador}')
print(f'Media dos cadastrados {media}')
for x in listaM:
    for k,v in x.items():
        print(f'{k}: {v}')
    print('-----------------')
print('Lista pessoas acima da média')
for x in listaMed:
    for k, v in x.items():
        print(f'{k}: {v}')
    print('-----------------')
for i in range(len(listaAll)):
    if listaAll[i]['idade'] > media:
        listaMed.append(listaAll[i].copy)
for x in listaAll:
    for k, v in x.items():
        print(f'{k}: {v}')
    print('-----------------')
####################################################################################################
#DESAFIO 95
#Aprimore o DESAFIO 93 para que ele funcione com vários
#jogadores, incluindo um sistema de visualização de detalhes do
#aproveitamento de cada jogador
import random


jogador={}
lista=[]
listaJ=[]
while True:
    jogador['nome']=input('Nome do jogador: ')
    jogador['partidas']=int(input('quantidade de partidas jogadas: '))
    listaJ.append(jogador['nome'])
    sair=input('Deseja sair? (S/N): ')
    if sair.lower() == 's':
        break
for x in range(jogador['partidas']):
    jogador['gols'] = random.randint(0, 3)
    lista.append(jogador['gols'])
jogador['totalGols'] = sum(lista)
print(f'Os jogadores: {listaJ} \nfizeram: { jogador['totalGols']} gol(s)')
aproveitamento=jogador['totalGols']/jogador['partidas']
print(f'Aproveitamento do jogador: {aproveitamento}')
#arrumar!!
####################################################################################################
#Crie um programa de votação com 3 candidatos.
#Faça o uso do laço while para sair quando a pessoa quiser.
#mostre os votos de cada candidato.
#mostre quem ganhou as eleiçôes.

#########################################################
#adicionar tres listas e criar um laço de repetição para votar quantas vezes desejar colocar break e se a resposta for não entrara em outra lista e se a resposta for não entrará em outra lista assim até os turnos desejados pelos usuários ao final mostrar os votos de cada candidato e quem ganhou.
import time

mario=0
luigi=0
peach=0
qtd=int(input('Digite quantos turnos terá a eleição:'))
for i in range(qtd):
  time.sleep(2)
  print('Escolha seu candidato: ')
  print('1-Mario')
  print('2-Luigi')
  print('3-Princesa Peach')
  voto=int(input('Digite seu voto: '))
  time.sleep(1)
  print('Seu voto foi computado')
  print('-------------')
  if voto == 1:
      time.sleep(1)
      print('Você votou no Mario')
      mario=mario+1
      print('-------------')
  elif voto == 2:
      time.sleep(1)
      print('Você votou no Luigi')
      luigi=luigi+1
      print('--------------')
  elif voto == 3:
      time.sleep(1)
      print('Você votou na Princesa Peach')
      peach=peach+1
  else:
      print('Voto invalido')
  time.sleep(2)
  if mario > luigi and mario > peach:
     print(f'Mario ganhou a eleição!!! (Com {mario} votos)')
  elif luigi > mario and luigi > peach:
     print(f'Luigi ganhou a eleição!!! (Com {luigi} votos)')
  elif peach > mario and peach > luigi:
     print(f'Princesa Peach ganhou a eleição!!! (Com {peach} votos)')
  if mario == luigi and mario == peach:
    print('Houve empate')

time.sleep(2)
print('--------------')
print(f'Mario teve {mario} votos')
print(f'Luigi teve {luigi} votos')
print(f'Princesa Peach teve {peach} votos')
##################################################################################################
#Crie um programa que leia a) média salarial da população; b)média do números de filhos; c)quantidade de pessoas com sálario até R$1500;

#Declaração das variaveis que serviram para as contas da média e as outras duas para o armazenamento e acrescentamento de valores que no caso são os sálarios.
mediaSalario=0
mediaFilhos=0
salarioAcima1500=0
salarioAte1500=0
for x in range(3):
    #a) média salarial da população.
    salario= float(input(f'Digite o sálario da {x+1} pessoa: '))
    mediaSalario+=salario
    #b)média do números de filhos.
    filhos= int(input(f'Digite o número de filhos da {x+1} pessoa: '))
    mediaFilhos+=filhos
    print('-------')
    #c)quantidade de pessoas com sálario até R$1500 (e acima de R$1500)
    if salario <= 1500:
        salarioAte1500+=1
    else:
        salarioAcima1500+=1

print(f'Pessoas com sálario até R$1500: {salarioAte1500}')
print(f'Pessoas com sálario acima de R$1500: {salarioAcima1500}')
print(f'A média do salário da população é de: {mediaSalario/3:.2f}')
print(f'A média do número de filhos é de: {mediaFilhos/3:.2f}')
####################################################################################################
#crie um programa que leia o a)sexo, b)cor dos olhos (azuis, verdes ou castanhos), c)cor dos cabelos (loiros, castanhos ou pretos) e d)idade. Das pessoas de uma certa região.
idmedia=0
corO=0
sexoM=0
sexoF=0

for x in range(3):
    #d)idade
    idade=int(input(f'Digite a idade da {x+1} pessoa: ')
    idmedia+=idade
    #a)sexo
    sexo= input(f'Digite o sexo da () pessoa (M/F): ')
    if sexo == 'm':
        sexoM+=1
    else:
        sexoF+=1
    #b)cor dos olhos (azuis, verdes ou castanhos)
    print('Selecione abaixo a cor dos ohos da () pessoa: A=Azuis,V=Verdes,C=Castanhos')
    corOlhos= input(f'Digite a cor dos olhos (A/V/C): ')
    corO+=1
    #c)cor dos cabelos (loiros, castanhos ou pretos)
    print('Selecione abaixo a cor dos cabelos da () pessoa: L=Loiros,C=Castanhos,P=Pretos')
    corCabelos= input(f'Digite a cor dos cabelos (L/C/P): ')
    corC+=1
################################################################################################
#Algumas anotações do inicio do curso de python do Senai.

from typing_extensions import TypeAliasType


nome = 'Gabriel'  #texto obrigatório aspas ou aspas duplas
#variavel nome recebe gabriel
idade = 19
#variavel idade recebe 19
anoNascimento = 2005
curso = 'python'  #texto obrigatório aspas ou aspas duplas
#variavel curso recebe python
print('O nome do aluno/a é: ',nome)
print('A idade do',nome,' é: ',idade,'anos')
print('O ano de nascimento do',nome,' é: ',anoNascimento)
print('O curso que o',nome,'faz é: ',curso)


#Atribui dados digitados pelo usuario e converte em numero inteiro
numeroInteiro = int(input('Digite um numero Inteiro: '))

#Atribui dados digitados pelo usuario e converte em Numero Decimal
numerodecimal = float(input('Digite um numero Decimal: '))

#Atribui dados digitados pelo usuario e converte em Bool
booleano = bool(input('Digite um valor Boleano: '))

#Atribui dados digitados pelo usuario e converte em Texto
string = str(input('Digite um texto: '))


#variavel texto1 recebe um valor str do usuario
texto1 = str(input('Digite o primeiro texto: '))

#variavel texto2 recebe um valor str do usuario
texto2 = str(input('Digite o segundo texto: '))

print('O usuario digitou os caracteres',texto1,'e',texto2)




n2 = int(input('Digite o Número: '))

sucessor=n2 + 1
antecessor=n2 - 1
print('O sucessor do número',n2,'é',sucessor,'já o seu antecessor é igual a',antecessor)


n2 = int(input('Digite o Número: '))
print('O sucessor do número',n2,'é',n2+1,'já o seu antecessor é igual a',n2-1)

base=float(input('Digite o valor da base: '))
altura= float(input('Digite a altura: '))

perimetro = base + altura
area = base * altura

print('O perimetro do retangulo é igual a:',perimetro)
print('A area do retangulo é igual a: ',area)


V= float(input('Digite o valor da prestação: '))
T= float(input('Digite o valor da taxa: '))
temp= float(input('Digite o tempo de atraso em meses: '))

print(f'O valor da prestação em atraso é :',(V+(V*(T/100)*temp)))



texto=" Curso de Python "
print(texto[6])
print(texto[9:15])
print(texto[9:15:2])
print(texto[:5])
print(texto[9:])
print(len(texto))
print(texto.count('o'))
print(texto.find('Python'))
print('Python in', texto)
print(texto.replace('Python','JavaScript'))
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())
print('-'.join(texto))
print(texto.split())



test 
name= 'Gabriel Dos Santos Morais'
print(name.upper())
print(name.lower())
esp=(name.count(''))
tamanho=len(name)
print(tamanho-esp)
print(name.find(''))