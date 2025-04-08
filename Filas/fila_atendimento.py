class No:
    def __init__(self, valor, tempo_atendimento):
        self.valor = valor  # Identificador do cliente
        self.tempo_atendimento = tempo_atendimento  # Tempo necessário para atender o cliente
        self.proximo = None  # Próximo nó na fila

class FilaAtendimento:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
    
    # Método de adicionar um valor à fila
    def enqueue(self, valor, tempo_atendimento):
        novo_no = No(valor, tempo_atendimento)
        if self.cauda is not None:
            self.cauda.proximo = novo_no
        self.cauda = novo_no
        if self.cabeca is None:
            self.cabeca = novo_no

    # Método de remover um valor da fila
    def dequeue(self):
        if self.cabeca is not None:
            removido = self.cabeca
            self.cabeca = self.cabeca.proximo
            if self.cabeca is None:
                self.cauda = None
            return removido.valor, removido.tempo_atendimento
        raise Exception("Fila vazia")

