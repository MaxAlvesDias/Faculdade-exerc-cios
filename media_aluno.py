from itertools import count

class Disciplina:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, disciplina_prof, professor):
        self.disciplina_prof = disciplina_prof
        self.professor = professor
        self.alunos = []  # Lista para armazenar os alunos em ordem alfabética na turma
        self.notas = {}  # Dicionário para armazenar as notas dos alunos na turma

    def adicionar_aluno_ordem_alfabetica(self, aluno):
        index = 0
        for index, a in enumerate(self.alunos):
            if a.nome_aluno > aluno.nome_aluno:
                break
            index += 1
        self.alunos.insert(index, aluno)

class Aluno:
    contador_matricula = count(1)  # Inicializando um contador para matrículas sequenciais

    def __init__(self, nome_aluno):
        self.nome_aluno = nome_aluno
        self.matricula_aluno = next(self.contador_matricula)
        self.notas = {}  # Dicionário para armazenar notas do aluno em diferentes disciplinas


#Dicionário para armazenar dados
professores={}
alunos={}
disciplinas={}
turmas={}



def cadastro_professor():
    nome_prof=str(input('Digite o nome do professor: '))
    disciplina_prof=str(input('\nDigite o nome da disciplina: '))
    novo_professor={nome_prof:disciplina_prof}
    professores.update(novo_professor)
    disciplinas[disciplina_prof]= Disciplina(disciplina_prof)
    print(f'Cadastro do {nome_prof} realizado com sucesso!\n')

def cadastro_aluno():
    nome_aluno = input('\nDigite o nome do aluno: ')
    novo_aluno = Aluno(nome_aluno)
    alunos[novo_aluno.matricula_aluno] = novo_aluno
    print(f'Aluno {nome_aluno} cadastrado com sucesso!\n')



def cadastrar_turma():
    disciplina_nome = input('\nDigite o nome da disciplina da turma: ')
    if disciplina_nome not in disciplinas:
        print('Disciplina não encontrada.\n')
        return 
    
    professor_nome = input('\nDigite o nome do professor da turma: ')
    if professor_nome not in professores:
        print('Professor não encontrado.\n')
        return
    
    nova_turma = Turma(disciplinas[disciplina_nome], professor_nome)
    turmas[disciplina_nome] = nova_turma
    print(f'Turma de {disciplina_nome} cadastrada com sucesso!\n')

def adicionar_aluno_na_turma():
    disciplina_nome = input('\nDigite o nome da disciplina: ')
    if disciplina_nome not in turmas:
        print('Disciplina não encontrada.\n')
        return

    matricula = int(input('\nDigite a matrícula do aluno: '))
    if matricula not in alunos:
        print('Aluno não encontrado.')
        return

    aluno = alunos[matricula]
    turma = turmas[disciplina_nome]
    turma.adicionar_aluno_ordem_alfabetica(aluno)
    print(f'Aluno {aluno.nome_aluno} adicionado à turma de {disciplina_nome}.\n')

def cadastro_nota():
    matricula_aluno = int(input('\nDigite a matricula do aluno: '))
    if matricula_aluno not in alunos:
        print('Aluno não pertence a turma. Cadastro negado!')
        return
    disciplina_nome = input("\nDigite o nome da disciplina: ")
    if disciplina_nome not in turmas:
        print("Disciplina não encontrada.\n")
        return

    nota = float(input("Digite a nota: "))
    aluno = alunos[matricula_aluno]
    turma = turmas[disciplina_nome]
    if aluno.matricula_aluno in turma.notas:
        turma.notas[aluno.matricula_aluno][disciplina_nome] = (turma.notas[aluno.matricula][disciplina_nome] + nota) / 2
    else:
        turma.notas[aluno.matricula_aluno] = {disciplina_nome: nota}
    print("Nota cadastrada com sucesso!\n")
      

def exibir_boletim():
    print(f'\nBoletim dos alunos: ')
    print('{:<15} {:<15} {:<15} {:<10}'.format("Matrícula", "Nome", "Disciplina", "Nota"))
    for disciplina, turma in turmas.items():
        for matricula, notas in turma.notas.items():
            aluno = alunos[matricula]
            for disciplina, nota in notas.items():
                print('{:<15} {:<15} {:<15} {:<10.2f}'.format(matricula, aluno.nome_aluno, disciplina, nota))
    print()


def listar_alunos():
    print(f'\nLista de Alunos: ')
    for matricula, aluno in alunos.items():
        print(f'Matrícula: {matricula} - Nome: {aluno.nome_aluno}\n')
    print()


def listar_professores():
    print('\nLista de Professores: ')
    for professor in professores:
        print(f'Professor: {professor} - Disciplina: {professores[professor]}')
    print()


def alunos_na_turma():
    disciplina_nome = input('\nDigite o nome da disciplina da turma: ')
    if disciplina_nome in turmas:
        print(f'Alunos na turma de {disciplina_nome}: ')
        for aluno in turmas[disciplina_nome].alunos:
            print(f'\nMatrícula: {aluno.matricula_aluno} - Nome: {aluno.nome_aluno}')
    else:
        print('Turma não encontrada.\n')
    print()

#---------------------------------------------------------------------------#
# Menu principal
while True:
    print('\n###----MENU----###\n')
    print('1. Cadastrar Professor\n')
    print('2. Cadastrar Aluno\n')
    print('3. Cadastrar Turma\n')
    print('4. Adicionar Aluno na Turma\n')
    print('5. Cadastrar Nota\n')
    print('6. Exibir Boletim\n')
    print('7. Listar Alunos\n')
    print('8. Listar Professores\n')
    print('9. Alunos na Turma\n')
    print('10. Sair\n')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastro_professor()
    elif opcao == '2':
        cadastro_aluno()
    elif opcao == '3':
        cadastrar_turma()
    elif opcao == '4':
        adicionar_aluno_na_turma()
    elif opcao == '5':
        cadastro_nota()
    elif opcao == '6':
        exibir_boletim()
    elif opcao == '7':
        listar_alunos()
    elif opcao == '8':
        listar_professores()
    elif opcao == '9':
        alunos_na_turma()
    elif opcao == '10':
        print('Saindo do programa.\n')
        break
    else:
        print('Opção inválida. Tente novamente.\n')
