idades =[38, 4, 36, 1]
print(idades)

# A lista é um iterável
for idade in idades:
    print(idade, end=' ')
print('\n')

# Removendo um elemento pelo seu valor
idades.remove(36)
# O remove, elimina apenas a primeira aparição daquele valor.
print(idades)
#adicionando um elemento ao final da lista
idades.append(45)
print(idades)
