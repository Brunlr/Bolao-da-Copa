def ciano(txt):
    print (f'\033[1;36m{txt}\033[m')


def azul(txt):
    print (f'\033[1;34m{txt}\033[m')


def verde(txt):
    print (f'\033[0;32m{txt}\033[m')



def vermelho(txt):
    print(f'\033[1;31m{txt}\033[m')


def arquivoExiste(nome):

    #verifica se o arquivo existe

    try:
        a = open(nome)
        a.close()

    except:
        print('Arquivo não encontrado! ')
    else:
        print(f'Arquivo {nome} encontrado com sucesso! ')
        return True


def criarArquivo(nome):

    #cria o arquivo se o mesmo não existir

    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print('Erro ao criar arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')


def cadastro(arquivo, nomecompalpite):
    #Cadastro de pessoas
    try:
        a = open(arquivo,'at')
    except:
        vermelho('Houve um ERRO ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nomecompalpite[0]} ; {nomecompalpite[1]}; {nomecompalpite[2]}\n')
        except:
            vermelho('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'{nomecompalpite[0]}, seu palpite foi adicionado!')


def lerArquivo(nome,times):
    try:
        a = open(nome, 'rt')
    except:
        print ('Erro ao ler arquivo')
    else:
        print(f'\033[1;32m')
        print('{:<12} {:<10} {:<10}'.format('Usuario', times[0], times[1]))
        for linha in a:
            linha.split()
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            dado[2] = dado[2].replace('\n', '')
            print (f'\033[1;33m{dado[0]:<10}\033[m \033[1;32m|\033[m \033[1;33m{dado[1]:<8}\033[m \033[1;32m|\033[m\033[1;33m {dado[2]}\033[m')
            print()




def inicio():
    print(f'\033[1;34m')
    print("_" * 30)
    print("BOLÃO DA COPA".center(30))
    print("_" * 30)



