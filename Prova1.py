 '''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2022/2
Mensagem:   NOME COMPLETO DO ESTUDANTE
Anexo:      prova1.py
'''

def main():
    '''
    Executa todass as questões
    '''

    #1. Faça um programa que leia o valor de um produto, o percentual
    #   do desconto desejado e imprima o valor do desconto e o valor
    #   do produto subtraindo o desconto. (2,0pt)
v = int(input('Digite o valor do produto: '))
d = float(input('Digite seu percentual de desconto: '))
print(f'O valor do desconto é de {d}%, e o valor final do produto é {v - d}')
          
    #2. Faça um programa que leia 3 números e imprima o maior deles. (2,0pt)
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
if n1 > n2:
	print(f'O primeiro número é maior!')
elif n2 > n3:
    print(f'O segundo número é maior!')
else:
    print(f'O terceiro número é maior!')
    
    #3. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
    #   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
    #   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
    #   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
    #   reprovação e as demais em prova final). (2,0pt)

nome = input('Aluno: ')
np1 = float(input('Insira a nota da prova 1: '))
np2 = float(input('Insira a nota da prova 2: '))
media = (np1 + np2)/2
print(f'A média do aluno é {media}!')
if media >= 7:
    print(f'APROVADO!')
elif media < 3:
    print(f'REPROVADO!')
else:
    print(f'PROVA FINAL!')

    #4. Faça um programa que apresente um menu com 4 opções:
    #   [1] - Cadastrar
    #   [2] - Excluir
    #   [3] - Pesquisar
    #   [0] - Sair
    #   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
    #   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
    #   escolhida for zero (0). (2,0pt)
[1] - Cadastrar
[2] - Excluir
[3] - Pesquisar
[0] - Sair

op = -1
while op != 0:
    print(menu)
op = int(input('Escolha uma opção: '))
if op == 0:
    break

    #5. Faça um programa que calcule o retorno de um investimento. (2,0pt)
    #   O programa deve solicitar do usuário o:
    #   - valor que será investido;
    #   - prazo do investimento (meses);
    #   - juros mensal.
valor = float(input('Digite o valor do investimento: '))
prazo = int(input('Prazo do investimento em meses: '))
juros = float(input('Insira o percentual de juros mensal: ')
valorFinal = prazo * juros
for valor in range(prazo_juros):
	print(valor final)
print(f'O investimento de R${valor}, terá um retorno de {valorFinal}')

main()