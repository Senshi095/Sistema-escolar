usuarios = {
            'Admin':'40028922',
            'Professor':'12345678',
            'Senshi':'Iasserde12'
}



print('=== Sistema de login ===')
while True:
  usuario = input('Usuário:')
  senha = input('Senha:')

  if usuario in usuarios and usuarios[usuario] == senha:
    print (f'\n✅ Bem-vindo, {usuario}!\n')
    break
  else:
    print('❌ Usuário ou senha inválidos. Tente novamente.\n')


materias = ['português','matemática','geografia','ciencias','ingles','fisica']

alunos = ['Matheus', 'João', 'Marcos', 'Pedro', 'Senshi']

notas = {
  'Matheus':{'Matemática': 8,'Português': 7, 'Geografia': 7, 'Ciências': 8, 'Ingles': 9, 'Física': 10 },
  'João': {'Matemática': 6, 'Português': 8, 'Geografia': 4, 'Ciências': 9, 'Inglês': 8, 'Física': 9},
  'Marcos': {'Matemática': 8,'Português': 9, 'Geografia': 5, 'Ciências': 7, 'Ingles': 2, 'Física': 1 },
  'Pedro' : {'Matemática': 4,'Português': 9, 'Geografia': 7, 'Ciências': 3, 'Ingles': 1, 'Física': 9},
  'Senshi' : {'Matemática': 10,'Português': 10, 'Geografia': 10, 'Ciências': 10, 'Ingles': 10, 'Física': 10},
  }

for aluno in alunos:
  print(aluno)



aluno_digitado = input('Escreva o nome de um aluno:')
if aluno_digitado in alunos:
  print(aluno_digitado)
else:
  print('Aluno não encontrado ou não registrado no sistema.')



for materia in materias:
  print(materia)



while True:
  materia = input('Digite uma matéria (ou sair para encerrar): ')
  if materia =='sair':
    break
  if materia in notas [aluno_digitado]:
    print('Nota:',notas[aluno_digitado][materia])
  else:
    print('Matéria não encontrada.')

