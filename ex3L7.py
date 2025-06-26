alunos = []
i = 0

while i < 5:
    print(f"\nAluno {i+1}:")
    notas = []
    j = 0

    while j < 4:
        nota = int(input(f"Digite a {j+1}ª nota: "))
        notas.append(nota)
        j += 1

    alunos.append(notas)
    i += 1

print("\nResultados:")
i = 0
while i < 5:
    notas = alunos[i]
    soma = 0
    j = 0
    while j < 4:
        soma += notas[j]
        j += 1
    media = soma / 4
    print(f"Aluno {i+1} - Notas: {notas} - Média: {media:.2f}")
    i += 1
