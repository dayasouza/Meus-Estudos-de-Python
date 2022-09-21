notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#alternativa a encontre quantos alunos tiraram nota 7
print(notas.count(7))

#alterar a ultima nota para 4

notas[-1] = 4
print(notas)

#Encontre a maior nota
max_notas = max(notas)
print('Maior nota:', max_notas)

#Ordenar lista de notas
notas.sort()
print(notas)

#média das notas
media = sum(notas) / len(notas)
print(media)

#alternativa usando bibliotecas
import statistics

media_s = statistics.mean(notas)
print(media_s)


