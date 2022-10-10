#Exercicio1
valor1 = int(input("Insira o valor 1: "))
valor2 = int(input("Insira o valor 2: "))
soma = valor1+valor2

if (valor1+valor2>10):
    print(f'O resultado é: {soma}.')
    
#Exercicio2    
n1 = int(input())
n2 = int(input())
if (n1 + n2)> 10:
    print(n1+n2)
else:
    print("O número não é maior que 10.")
    
#Exercicio3
n1 = int(input())
if (n1%3) == 0:
    print("O número é divisível por 3")
else:
    print("O número não é multiplo de 3")
    
#Exercicio4
n1 = int(input())
if (n1%5) == 0:
    print("O número é divisível por 5")
else:
    print("Não é divisível por 5")
    
#Exercicio5
n1 = int(input())
if (n1%3) == 0 and (n1%7) == 0:
    print("O número é divisível por 3 e 7.")
else:
    print("Não é divisível por 3 e 7.")
    
#Exercicio6
s = float(input("Digite o valor do salário:"))
p = float(input("Digite o valor da prestação:"))
if p > (s*30/100):
    print("Você não pode pegar a prestação.")
else:
    print("Você pode pegar a prestação.")
    
#Exercicio7
n = float(input())
if n >= 20 and n <= 50:
    print("Está dentro.")
else:
    print("Não está dentro")
    
#Exercicio8
n = float(input())
if n >= 20 and n <= 20:
    print("Maior que 20 ou igual a 20.")
else:
    print("Menor que 20.")
    
#Exercicio9
a = int(input("Insira o ano que você nasceu:"))
A = int(input("Insira o ano atual:"))
print(f'A sua ide de é {A-a}.')

#Exercicio10
n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))
if n1<n1<n3:
    print(n1,n2,n3)
elif n2<n1<n3:
    print(n2,n1,n3)
elif n3<n1<n2:
    print(n3,n1,n2)
elif n1<n3<n2:
    print(n1,n3,n2)
else:
    print(n3,n2,n1)
    
#Exercicio11
n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))
if n1>n2>n3:
    print(n1)
elif n2>n1>n3:
    print(n2)
elif n3>n1>n2:
    print(n3)
    
#Exercicio12
n1=int(input('Digite a sua idade:'))
if n1<18:
    print("Você é menor de idade.")
if n1>18:
    print("Você é maior de idade:")
if n1>65:
    print("Já é considerado velho.")
    
#Exercicio13
a=str(input("Digite seu nome:"))
n1=int(input("Digite a nota 1:"))
n2=int(input("Digite a nota 2:"))
m=(n1+n2/2)
print(a)
print(n1)
print(n2)
print(f'A média:{m}')
if m>7:
    print("Aprovado")
else:
    print("Reprovado")