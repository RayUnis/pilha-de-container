"""
modulo: Simula pilha de container
objetivo: Demonstrar o conceito de pilha na disciplina estrutura de dados
autor: Rayane Carvalho da Silva Marques
email: rayane.marques1@alunos.unis.edu.br
"""

### Exemplo de pilha com limite de 3 containers por barco.

pilha = []

def cria_nomeContainer(nome):
    return {
        "nome": nome, 
    }

def embarca(container):
    print(f"{container['nome']}")
    pilha.append(container)

def desembarca(container):
    print(f"O {container['nome']} desembarcou")

container_a1 = cria_nomeContainer("container A1")
container_a2 = cria_nomeContainer("container A2")
container_a3 = cria_nomeContainer("container A3")

print(f"Status de embarque... ")

embarca(container_a1)
embarca(container_a2)
embarca(container_a3)

print(f"Status de desembarque... ")

while len(pilha):
    proximo_da_pilha = pilha.pop()
    desembarca(proximo_da_pilha)


