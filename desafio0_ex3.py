n_de_alunos=int(input("insira o número de alunos da turma"))
melhor_nota=-1
número_aluno=-1
for i in range(n_de_alunos):
    nota=int(input("nota do aluno",{i+1}))
    if nota>melhor_nota:
        melhor_nota=nota
        número_aluno=i+1
print("a melhor nota foi do aluno")
