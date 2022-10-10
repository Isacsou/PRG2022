'''
Lista de Exercícios referentes a estruturas de iteração (repetição)
'''
def main():
    '''
    Executa todos os exercícios resolvidos
    '''
    #Exemplo de uso do while
    menu = '''
        [1] - Cadastrar
        [2] - Excluir
        [3] - Buscar

        [0] - Sair
    '''
    opcao = -1
    while opcao != 0:
        print(menu)
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 0: #não é necessário
            break # quebra o laço de repetição ou estrutura de iteração

    #1.Faça um programa que imprima todos os números de 1 até 100.
    for cont in range(1, 101):
        if cont == 10: # a título de exemplo de como pular uma iteração
            continue #salta para a próxima iteração e não deve imprimir o número 10
        print(cont, end=' ')

    #2. Faça um programa que imprima todos os números pares de 100 até 1.
    print('\n\n')
    for cont in range(100, 0, -2):
        print(cont, end=' ')

    #3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.
    print('\n\n')
    for cont in range(0, 5, 5):
        print(cont, end=' ')

    #4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
    #pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
    #e tiver mais de 21 anos.
    print('\n\n')
    for pessoa in range(20):
        nome = input(f"Nome {pessoa+1}: ")
        if nome == 'sair':
            break
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").upper()[0]
        if sexo == "M" and idade >= 21:
            print(nome)

    #5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
    #sucessivas, crie um programa que calcule o produto de dois números inteiros
    #lidos. Suponha que os números lidos sejam positivos.
    print('\n\n')
    multiplicando = int(input('multiplicando: '))
    multiplicador = int(input('multiplicador: '))
    resultado = 0
    for cont in range(multiplicador):
        resultado += multiplicando
    print(f'{multiplicando} * {multiplicador} = {resultado}')

    #6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
    #Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
    #a partir da soma dos anteriores. Exemplo:
    #• 1 + 1 = 2, terceiro termo;
    #• 1 + 2 = 3, quarto termo, etc.
    print('\n\n')
    anterior = 1
    proximo = 1
    print(anterior, end=' ')
    for cont in range(19):
        print(proximo, end=' ')
        novo_anterior = proximo
        proximo = anterior + proximo
        anterior = novo_anterior

    #7. Crie um programa que permita entrar com o nome, a nota da
    #prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
    #nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
    #imprimir a média geral da turma.
    print('\n\n')
    lista = 'NOME\tN1\tN2\tMEDIA\n'
    total_alunos = int(input('Qtde de alunos: '))
    media_geral = 0
    for aluno in range(total_alunos):
        nome = input('Nome: ')
        n1 = int(input('Nota 1: '))
        n2 = int(input('Nota 2: '))
        media = round((n1+n2)/2, 2)
        media_geral += media
        lista += f'{nome}\t{n1}\t{n2}\t{media}\n'
    media_geral = round(media_geral/total_alunos, 2)
    lista += f'\nMédia Geral: {media_geral}'
    print(lista)

    #8. Faça umprograma que permita entrar com o nome e o salário bruto de 10 pessoas.
    #Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
    #calculado conforme a tabela a seguir:
    #Salário IRRF
    #Salário menor que R$1300,00 Isento
    #Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
    #Salário maior ou igual a R$2300,00 15% do salário bruto
    print('\n\n')
    lista = 'NOME\tSALARIO\tIR\n'
    total_pessoas = int(input('Qtde de pessoas: '))
    for pessoa in range(total_pessoas):
        nome = input('Nome: ')
        salario_bruto = round(float(input('Salário Bruto: ')), 2)
        imposto_renda = 0.0
        if salario_bruto < 1300:
            imposto_renda = 0.0
        elif salario_bruto < 2300:
            imposto_renda = round(salario_bruto*0.1, 2)
        else:
            imposto_renda = round(salario_bruto*0.15, 2)
        lista += f'{nome}\tR$ {salario_bruto}\tR$ {imposto_renda}\n'
    print(lista)

    #9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
    #uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
    #a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
    #excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
    #opinião de 20 espectadores, calcule e imprima:
    #• A média das idades das pessoas que responderam excelente;
    #• A quantidade de pessoas que responderam regular;
    #• A percentagem de pessoas que responderam bom entre todos os expectadores
    #analisados.
    print('\n\n')
    qtde_pessoas = int(input('Qtde de Pessoas: '))
    soma_idade_excelente = 0
    qtde_pessoas_excelente = 0
    qtde_pessoas_regular = 0
    qtde_pessoas_bom = 0
    for cont in range(qtde_pessoas):
        idade = int(input('Idade: '))
        opiniao = int(input('excelente, bom, regular (3, 2, 1): '))
        soma_idade_excelente += idade if opiniao == 3 else 0
        qtde_pessoas_excelente += 1 if opiniao == 3 else 0
        qtde_pessoas_bom += 1 if opiniao == 2 else 0
        qtde_pessoas_regular += 1 if opiniao == 1 else 0
    print(f'Média da idade das pessoas que responderam excelente: {soma_idade_excelente/qtde_pessoas_excelente}')
    print(f'Qtde de pessoas que responderam regular: {qtde_pessoas_regular}')
    print(f'Percentual de pessoas que responderam bom: {qtde_pessoas_bom/qtde_pessoas*100}%')

    #10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
    #que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
    #jogadores, crie um programa que apresente as seguintes informações:
    #
    #• O peso médio e a idade média de cada um dos times;
    #• O atleta mais pesado de cada time;
    #• O atleta mais jovem de cada time;
    #• O peso médio e a idade média de todos os participantes.
    qtde_paises = int(input('Qtde de países: '))
    qtde_atletas = int(input('Qtde de atletas por país: '))
    peso_soma_geral = 0
    idade_soma_geral = 0
    for pais in range(qtde_paises):
        peso_soma_pais = 0
        idade_soma_pais = 0
        maior_peso = 0
        menor_idade = 100
        for atleta in range(qtde_atletas):
            idade = int(input('Idade: '))
            peso = int(input('Peso: '))
            peso_soma_pais += peso
            peso_soma_geral += peso
            idade_soma_pais += idade
            idade_soma_geral += idade
            if peso > maior_peso: maior_peso = peso
            if idade < menor_idade: menor_idade = idade
        print(f'Peso médio: {peso_soma_pais / qtde_atletas}')
        print(f'Idade média: {idade_soma_pais / qtde_atletas}')
        print(f'Atleta mais pesado: {maior_peso} Kg')
        print(f'Atleta mais jovem: {menor_idade} anos')
    print(f'Peso médio geral: {peso_soma_geral / (qtde_paises * qtde_atletas)}')
    print(f'Idade média geral: {idade_soma_geral / (qtde_paises * qtde_atletas)}')        
        
    #11. Construa um programa que leia vários números e informe quantos números
    #entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
    #deverá cessar sua execução.
    numero = -1
    qtde_numeros_entre_100_200 = 0
    while numero != 0:
        numero = int(input('Número: '))
        qtde_numeros_entre_100_200 +=1 if numero >= 100 and numero <= 200 else 0
    print(f'Números entre 100 e 200: {qtde_numeros_entre_100_200}')

    #12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
    #ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
    #ano, fazer um programa que calcule e imprima o tempo necessário para que a
    #população do país A ultrapasse a população do país B.
    pais_a = 5_000_000
    nat_a = 1.03
    pais_b = 7_000_000
    nat_b = 1.02
    tempo = 0
    while (pais_a <= pais_b):
        pais_a *= nat_a
        pais_b *= nat_b
        tempo+=1
    print(f'Em {tempo} anos o país A terá uma maior população que a do país B')

    #13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
    #de consumo. Para cada consumidor, são digitados os seguintes dados:
    #• número do consumidor
    #• quantidade de kWh consumidos durante o mês
    #• tipo (código) do consumidor
    #1-residencial, preço em reais por kWh = 0,3
    #2-comercial, preço em reais por kWh = 0,5
    #3-industrial, preço em reais por kWh = 0,7
    #Os dados devem ser lidos até que seja encontrado o consumidor com número 0
    #(zero). O programa deve calcular e imprimir:
    #• O custo total para cada consumidor
    #• O total de consumo para os três tipos de consumidor
    #• Amédia de consumo dos tipos 1 e 2

    #14. Faça umprograma que leia vários números inteiros e apresente o fatorial de cada
    #número. O algoritmo encerra quando se digita um número menor do que 1.

    #15. Faça um programa que permita entrar com a idade de várias pessoas e
    #imprima:
    #• total de pessoas com menos de 21 anos
    #• total de pessoas com mais de 50 anos

    #16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
    #sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
    #números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
    #até que o resultado seja menor do que o divisor. O número de subtrações
    #realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
    #ao resto. Suponha que os números lidos sejam positivos e que o dividendo
    #seja maior do que o divisor.

    #17. Crie um programa que possa ler um conjunto de pedidos de compra e
    #calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
    #• número de pedido
    #72 Aula 3. Estruturas de Iteração
    #• data do pedido (dia, mês, ano)
    #• preço unitário
    #• quantidade
    #O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
    #como número do pedido.

    #18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
    #serviços diários de:
    #• R$15,00, se o número de dias for menor que 10;
    #• R$8,00, se o número de dias for maior ou igual a 10;
    #Faça umprograma que imprima o nome, a conta e o número da conta de cada
    #cliente e ao final o total faturado pela pousada.
    #O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
    #número da conta.

    #19. Emuma Universidade, os alunos das turmas de informática fizeram uma prova
    #de algoritmos. Cada turma possui um número de alunos. Criar um programa que
    #imprima:
    #• quantidade de alunos aprovados;
    #• média de cada turma;
    #• percentual de reprovados.
    #Obs.: Considere aprovado comnota >= 7.0

    #20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
    #• Qual o seu time de coração?
    #1-Fluminense;
    #2-Botafogo;
    #3-Vasco;
    #4-Flamengo;
    #5-Outros
    #• Onde você mora?
    #1-RJ;
    #2-Niterói;
    #3-Outros
    #• Qual o seu salário?
    #Faça um programa que imprima:
    #• o número de torcedores por clube;
    #• a média salarial dos torcedores do Botafogo;
    #• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
    #clubes;
    #• o número de pessoas de Niterói torcedoras do Fluminense
    #3.12. Exercícios da Aula 73
    #Obs.: O programa encerra quando se digita 0 para o time.

    #21. Emuma universidade cada aluno possui os seguintes dados:
    #• Renda pessoal;
    #• Renda familiar;
    #• Total gasto com alimentação;
    #• Total gasto com outras despesas;
    #Faça um programa que imprima a porcentagem dos alunos que gasta acima de
    #R$200,00 com outras despesas. O número de alunos com renda pessoal maior
    #que a renda familiar e a porcentagem gasta com alimentação e outras despesas
    #em relação às rendas pessoal e familiar.
    #Obs.: O programa encerra quando se digita 0 para a renda pessoal.

    #22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
    #arrecadados com a aplicação de multas de trânsito.
    #O algoritmo deve ler as seguintes informações para cada motorista:
    #• número da carteira de motorista (de 1 a 4327);
    #• número demultas;
    #• valor de cada uma das multas.
    #Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
    #total de recursos arrecadados (somatório de todas as multas). O programa deverá
    #imprimir tambémo número da carteira domotorista que obteve o maior número
    #de multas.
    #Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

    #23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
    #e altura) dos atletas que participaram de uma olimpíada, e informar:
    #• a atleta do sexo feminino mais alta;
    #• o atleta do sexomasculinomais pesado;
    #• amédia de idade dos atletas.
    #Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
    #atleta.
    #Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
    #como comparação e atribuição de textos.

    #24. Faça um programa que calcule quantos litros de gasolina são usados em uma
    #viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
    #do carro e o período de tempo que viaja nesta velocidade para cada trecho do
    #percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
    #consumidos = distância / 10, o programa computará, para todos os valores nãonegativos
    #de velocidade, os litros de combustível consumidos. O programa deverá
    #imprimir a distância e o número de litros de combustível gastos naquele trecho.
    #Deverá imprimir também o total de litros gastos na viagem. O programa encerra
    #quando o usuário informar umvalor negativo de velocidade.
    #74 Aula 3. Estruturas de Iteração

    #25. Faça umprograma que calcule o imposto de renda de umgrupo de contribuintes,
    #considerando que:
    #a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
    #anual) serão fornecidos pelo usuário via teclado;
    #b) para cada contribuinte será feito umabatimento de R$600 por dependente;
    #c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
    #da renda bruta anual;
    #d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
    #a seguir:
    #Renda Líquida Imposto
    #até R$1000 Isento
    #de R$1001 a R$5000 15%
    #acima de R$5000 25%
    #e) o valor de CIC igual a zero indica final de dados;
    #f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
    #imposto a ser pago;
    #g) ao final o programa deverá imprimir o total do imposto arrecadado pela
    #Receita Federal e o número de contribuintes isentos;
    #h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

    #26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
    #certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
    #número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
    #naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
    #casa não entraria na pesquisa. Criar um programa que:
    #• Leia um número indeterminado de dados, isto é, o número do canal e o
    #número de pessoas que estavam assistindo;
    #• Calcule e imprima a porcentagem de audiência em cada canal.
    #Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

    #27. Crie um programa que calcule e imprima o CR do período para os alunos de
    #computação. Para cada aluno, o algoritmo deverá ler:
    #• número da matrícula;
    #• quantidade de disciplinas cursadas;
    #• notas em cada disciplina;
    #Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
    #alunos que cursaram5 ou mais disciplinas.
    #• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
    #válidas de 1 a 5000);
    #• CR do aluno é igual à média aritmética de suas notas.

    #28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
    #Calcule e imprima:
    #3.12. Exercícios da Aula 75
    #• a quantidade de pessoas com idade superior a 50 anos;
    #• amédia das alturas das pessoas com idade entre 10 e 20 anos;
    #• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
    #pessoas analisadas.

    #29. Construa um programa que receba o valor e o código de várias mercadorias
    #vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
    #L-limpeza
    #A-Alimentação
    #H-Higiene
    #Calcule e imprima:
    #• o total vendido naquele dia, com todos os códigos juntos;
    #• o total vendido naquele dia em cada um dos códigos.
    #Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

    #30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
    #e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
    #• a quantidade de pessoas casadas;
    #• a quantidade de pessoas solteiras;
    #• amédia das idades das pessoas viúvas;
    #• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
    #analisadas.
    #Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
    #idade.

main()
