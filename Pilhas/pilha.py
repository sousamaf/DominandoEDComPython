class No:
    """
    Classe No: Representa um nó em uma estrutura de dados do tipo Pilha.
    Cada nó tem um valor associado e um ponteiro para o próximo nó na pilha.
    """
    def __init__(self, valor):
        """
        Inicializa o nó com um valor fornecido e o próximo nó como None.
        :param valor: O valor a ser armazenado no nó.
        """
        self.valor = valor
        self.proximo = None

class Pilha:
    """
    Classe Pilha: Implementa uma estrutura de dados do tipo pilha utilizando uma
    abordagem de lista encadeada. Suporta operações básicas de pilha como push (empilhar),
    pop (desempilhar), peek (observar o topo) e is_empty (verificar se está vazia).
    """
    def __init__(self):
        """
        Inicializa a pilha sem nenhum elemento.
        """
        self.topo = None

    def push(self, valor):
        """
        Adiciona um elemento no topo da pilha.
        :param valor: O valor a ser empilhado.
        """
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self):
        """
        Remove e retorna o elemento do topo da pilha.
        :return: O valor do elemento removido do topo da pilha.
        :raises Exception: Se a pilha estiver vazia.
        """
        if self.topo is not None:
            removido = self.topo
            self.topo = self.topo.proximo
            return removido.valor
        else:
            raise Exception("Pilha vazia.")

    def peek(self):
        """
        Retorna o valor do elemento no topo da pilha sem remover.
        :return: O valor do elemento no topo da pilha.
        :raises Exception: Se a pilha estiver vazia.
        """
        if self.topo is not None:
            return self.topo.valor
        else:
            raise Exception("Pilha vazia.")

    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        :return: True se a pilha estiver vazia, False caso contrário.
        """
        return self.topo is None
