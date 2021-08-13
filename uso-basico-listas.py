idades = [38, 4, 36, 1]
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
# Verificar se um elemento está dentro da lista
# 45 in idades
if 45 in idades:
    idades.remove(45)
print(idades)

# Adicionar um elemento em uma posição determinada
idades.insert(0, 27)
print(idades)

# Adiciona multiplos elementos a partir de um iterável, assim como o append, adiiciona no final
idades.extend([10, 19, 22])
print(idades)

# iterar por diversos elementos de um iterável, aplicando filtros e transformações, em "uma linha só"
# List comprehensions

idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem)
idades_maior_21 = [idade for idade in idades if idade > 21]
print(idades_maior_21)
