from abc import ABC, abstractmethod


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
        super().__init__(valor, descricao)
        self.numero = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel


    def processar(self):
        if self.valor > self.limite_disponivel:
            raise Exception(f"Limite insufuciente no cartão")
        


        self.limite_disponivel -= self.valor
        print(f"Pagamento aprovado no cartão {self.nome_titular}."
              f"Limite restante: {self.limite_disponivel}")






class Pix(Pagamento):
    def __init__(self, valor , descricao, chave, banco):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"PIX  enviado via  {self.banco} usado chave {self.chave}")


class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barras, vencimento):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento  = vencimento 


    def processar(self):
        print(f"Boleto gerado. Aguardando pagamento...")




def processar_pagamento(pagamento: Pagamento):
    try: pagamento.validar_valor()
         pagamento.resumo()
         pagamento.processar()
except Exception as e:
    print(f"Erro: {e}")



def main():
    pagamentos = [
        Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
        CartaoCredito(
            400,
            "Tênis esportivo",
            "1234 5678 9123 4567",
            "Cliente X",
            500
        ),
        Boleto(
            89.90,
            "Livro de Python",
            "123456789000",
            "2025-01-10"
        ),
        CartaoCredito(
            800,
            "Notebook",
            "9999 8888 7777 6666",
            "Cliente Y",
            700
        ),  # deve falhar
    ]

    for pagamento in pagamentos:
        processar_pagamento(pagamento)
        print()


if __name__ == "__main__":
    main()













