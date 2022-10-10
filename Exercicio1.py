#Exercicio 1
print('Isac de Sousa Azevedo')

#Exercicio 2
res = 30*27
print(f'O produto dos valores é: {res}')

#Exercicio 3
media = (5+8+12)/3
print(f'A média aritmética é: {media}')

#Exercicio 4
numInt = int(input("Número inteiro: "))
print(f'O número inteiro é: {numInt}')

#Exercicio 5
num1 = float(input("Primeiro número real: "))
num2 = float(input("Segundo número real: "))
print(f'Os números reais são: {num1} e {num2} ')

#Exercicio 6
numInt = int(input("Insira um número inteiro: "))
ant = numInt -1
suc = numInt +1
print(f'O antecessor deste número é: {ant} e o seu sucessor é {suc}')

#Exercicio 7
nome = input("Nome: ")
end = input("Endereço: ")
tel = int(input("Telefone"))
print(f'Nome: {nome}')
print(f'Endereço: {end}')
print(f'Telefone: {tel}')

#Exercicio 8
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o seundo número: "))
subt = n1 - n2
print(f'O resultado da subtração é: {subt}')

#Exercicio 9 
numReal = float(input("Número real: "))
result = numReal/4
print(f'Um quarto deste número equivale a: {result}')

#Exercicio 10
nr1 = float(input("Insira o primeiro número real: "))
nr2 = float(input("Insira o segundo número real: "))
nr3 = float(input("Insira o terceiro número real: "))
med = (nr1+nr2+nr3)/3
print(f'A média aritmética é: {med}')

#Exercicio 11
nu1 = float(input("Digite um número real: "))
nu2 = float(input("Digite outro número real: "))
print(f'O resultado da soma é: {nu1+nu2}\n Subtração: {nu1-nu2}\n Multiplicação: {nu1*nu2}\n E divisão: {nu1/nu2}')

#Exercicio 12
nreal = float(input("Número real: "))
print(f'O quadrado deste número é: {nreal**2}')

#Exercicio 13
saldo = float(input("Valor do saldo: "))
reajuste = saldo+saldo*0.02
print(f'O novo slado é: {reajuste}')

#Exercicio 14
base = float(input("Base do retângulo: "))
alt = float(input("Altura do retângulo: "))
print(f'O perímetro é {base+alt} e a área é {base*alt} .')

#Exercicio 15
valProd = float(input("Valor do produto: R$"))
desc = float(input("Valor de desconto: "))
valDesc = (valProd*desc)/100
print(f'O valor do desconto é R${valDesc} e o valor do produto fica R${valProd-valDesc} ')

#Exercicio 16
salarioAtual = float(input("Insira o valor do seu salário: "))
reajuste = float(input("Percentual de reajuste: "))
print(f'O valor do novo salário é: {((salarioAtual*reajuste)/100)+salarioAtual}'
      
#Exercicio 17
C = float(input("Digite a temperatura: "))
conversao = (9*C+160)/5
print(f'A temperatura em Fahreiheints é: {conversao}')
      
#Exercicio 18
tempo = float(input("Tempo decorrido em minutos: "))
velMed = float(input("Velocida média em KM: "))
D = tempo*velMed
C = D/12
print(f'A distância percorrida foi de {D}km e a quantidade de combustível consumida foi {C} litros.')

#Exercicio 19
valor = float(input("Prestação vencida: R$ "))      
juros = float(input("Taxa de juros: "))
periodo = float(input("Período de atraso em dias: "))
total = valor + (valor*juros)/100*periodo
print(f'O valor da prestação é R${valor}, {periodo} dias de período de atraso, total de R${total} com juros.')
      
#Exercicio 20
valor = float(input("Valor em doláres: U$"))
cotacao = float(input("Cotação do dia: R$"))
print(f'Como a cota diária é de R${cotacao}, o valor da conversão é: R${valor*cotacao}.')
