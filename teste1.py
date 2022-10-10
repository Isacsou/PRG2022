funcionarios = []
def cadastrar_funcionario():
    print('CADASTRO DE FUNCIONARIO')
    funcionario = {}
    funcionario['nome'] = input('Nome:')
    funcionario['salario_bruto'] = float(input('Salário Bruto: '))
    return funcionario

def menu():
    tela = '''
        [1] - Cadastrar
        [0] - sair
    '''
    opcao = -1
    while (opcao!=0):
        print(tela)
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            funcionario = cadastrar_funcionario()
            funcionarios.append(funcionario)
        else:
            if opcao!=0:
                print('Opção Inválida! Tente novamente.')

def reajustar_salarios(pessoas, reajuste):
    for pessoa in pessoas:
        pessoa['salario_bruto'] = round(pessoa['salario_bruto'] * (1+reajuste/100),2)

def exibir_salarios(pessoas):
    for pessoa in pessoas:
        print(f"{pessoa['nome']}\t{pessoa['salario_bruto']}")

menu()
print('Salários antes do Reajuste')
exibir_salarios(funcionarios)
reajustar_salarios(funcionarios,8)
print('Salários após o Reajuste')
exibir_salarios(funcionarios)
