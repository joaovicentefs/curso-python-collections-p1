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


#Sempre tomar cuidado com lista e objetos que são mutáveis, aula 1 video 4


#AULA 2.2 - Listas com objetos de classes próprias
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'[>>Código {self.codigo}, Saldo {self.saldo}<<]'

conta_do_joao = ContaCorrente(15)
print(conta_do_joao)

conta_do_joao.deposita(500)
print(conta_do_joao)