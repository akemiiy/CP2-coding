alunos = []

for i in range(5):
    nome = input(f"Nome do aluno {i + 1}: ").strip()
    while True:
        try:
            nota = float(input(f"Nota de {nome}: "))
            if nota < 0 or nota > 10:
                raise ValueError("A nota deve estar entre 0 e 10!")
        except ValueError as e:
            print(f"Erro: {e}")
        else:
            break
    alunos.append((nome, nota))

maior_nome, maior_nota = alunos[0]
menor_nome, menor_nota = alunos[0]
soma = 0

for nome, nota in alunos:
    if nota > maior_nota:
        maior_nome = nome
        maior_nota = nota
    if nota < menor_nota:
        menor_nome = nome
        menor_nota = nota
    soma += nota

media = soma / len(alunos)

print("\n=== Relatório de Notas ===")
print(f"Maior nota: {maior_nome} - {maior_nota}")
print(f"Menor nota: {menor_nome} - {menor_nota}")
print(f"Média da turma: {media:.1f}")
print("\nAlunos acima da média:")
for nome, nota in alunos:
    if nota > media:
        print(f"- {nome}: {nota}")
