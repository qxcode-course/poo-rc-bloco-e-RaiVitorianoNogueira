from abc import ABC, abstractmethod



class Veiculo(ABC):
    def __init__(self, vid: str, entrada: int, tipo: str):
        self.id = vid
        self.entrada = entrada
        self.tipo = tipo

    @abstractmethod
    def calcularValor(self, saida: int) -> float:
        pass

    def __str__(self):
        return (
            self.tipo.rjust(10, "_")
            + " : "
            + self.id.rjust(10, "_")
            + " : "
            + str(self.entrada)
        )



class Bike(Veiculo):
    def __init__(self, vid: str, entrada: int):
        super().__init__(vid, entrada, "Bike")

    def calcularValor(self, saida: int) -> float:
        return 3.0



class Moto(Veiculo):
    def __init__(self, vid: str, entrada: int):
        super().__init__(vid, entrada, "Moto")

    def calcularValor(self, saida: int) -> float:
        tempo = saida - self.entrada
        return tempo / 20



class Carro(Veiculo):
    def __init__(self, vid: str, entrada: int):
        super().__init__(vid, entrada, "Carro")

    def calcularValor(self, saida: int) -> float:
        tempo = saida - self.entrada
        valor = tempo / 10
        return valor if valor >= 5 else 5.0



class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.tempo_atual = 0

    def tempo(self, minutos: int):
        self.tempo_atual += minutos

    def estacionar(self, tipo: str, vid: str):
        if tipo == "bike":
            self.veiculos.append(Bike(vid, self.tempo_atual))
        elif tipo == "moto":
            self.veiculos.append(Moto(vid, self.tempo_atual))
        elif tipo == "carro":
            self.veiculos.append(Carro(vid, self.tempo_atual))

    def pagar(self, vid: str):
        for i, v in enumerate(self.veiculos):
            if v.id == vid:
                valor = v.calcularValor(self.tempo_atual)
                print(
                    f"{v.tipo} chegou {v.entrada} saiu {self.tempo_atual}. "
                    f"Pagar R$ {valor:.2f}"
                )
                self.veiculos.pop(i)
                return
        print("fail: veiculo nao encontrado")

    def show(self):
        for v in self.veiculos:
            print(v)
        print(f"Hora atual: {self.tempo_atual}")



def main():
    est = Estacionamento()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        print(f"${line}")
        args = line.split()

        if not args:
            continue

        if args[0] == "end":
            break

        elif args[0] == "tempo":
            est.tempo(int(args[1]))

        elif args[0] == "estacionar":
            est.estacionar(args[1], args[2])

        elif args[0] == "pagar":
            est.pagar(args[1])

        elif args[0] == "show":
            est.show()


if __name__ == "__main__":
    main()
