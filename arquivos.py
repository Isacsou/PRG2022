#r: somente leitura
#w: escrita, pode alterar o conteúdo do arquivo
#a: adicionar algo a arquivo já existente
arquivo = open('cadastro.dat','w')
arquivo.write('Linha 1\n') 
arquivo.write('Linha 2\n')
arquivo.write('Linha 3\n')
arquivo.write('Linha 4\n')
arquivo.write('Linha 5\n')
arquivo.write('Linha 6\n')
arquivo.write('Linha 7\n')
arquivo.close()

arquivo = open('cadastro.dat','r')
for linha in arquivo:
    print(linha.strip())
arquivo.close()

with open ('cadastro.dat', 'a') as arquivo:
    for linha in arquivo:
        	print(linha.strip(0))