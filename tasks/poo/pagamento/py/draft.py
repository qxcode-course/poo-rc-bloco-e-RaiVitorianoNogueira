from abc import ABC, abstractclassmethod


class Pagamento(ABC):
    def __init__(self, valor : float, descricao : str):
        self.valor = valor
        self.descricao = descricao


    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descricao}")



    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("Valor inválido para pagamento")
        

    @abstractmethod
    def processar(self):
        pass






class CartaoCredito(Pagamento):
    def __init__(self, valor, descricao, numero, nome_titular, limite_disponivel):
        super()










