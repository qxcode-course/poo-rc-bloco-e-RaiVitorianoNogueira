from  abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, vid: str, tipo: str, entrada: int):
        self.id = vid
        self.entrada = entrada
        self.tipo = tipo

    @abstractmethod
    def calcularValor(self, saida : int) -> float:
        pass


    def __str__(self):
        return(f"{self.tipo:_>10} : {self.id:_>10} : {self.entrada}")
        



class Bike(Veiculo):
    def __init__(self, vid: str, entrada : int):
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
    def __init__(self, vid: str, entrada : str):
        super().__init__(vid, entrada, "Carro")

    def calcularValor(self, saida: int) -> float:
        tempo = saida - self.entrada
        valor = tempo / 10
        return valor if valor >=  5 else 5.0
    










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
    estacionamento = Estacionamento()

    while True:
        line = input().strip()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "tempo":
            tempo_atual += int(args[1])
        elif args[0] == "estacionar":
            tipo = args[1]
            id = args[2]

            if tipo == "bike":
                estacionamento.estacionar(Bike(id, tempo_atual))
            elif tipo == "moto":
                estacionamento.estacionar(Moto(id, tempo_atual))
            elif tipo == "carro":
                estacionamento.estacionar(Carro(id, tempo_atual))
            else:
                print("fail:tipo invalido")
        elif args[0] == "pagar":
            id = args[1]
            veiculo =  estacionamento.buscar(id)


            if veiculo is None:
                print("fail: veiculo não encontrado")
            else:
                valor = veiculo.calcularValor(tempo_atual)
                print(
                    f"{veiculo.tipo} chegou {veiculo.entrada} saiu {tempo_atual}. "
                    f"Pagar R$ {valor:.2f}"
                )
                estacionamento.remover(id)
        elif args[0] == "show":
            print(estacionamento)
            print(f"Hora atual: {tempo_atual}")

        else:
            print("fail: comando invalido")

        
            



       
    





















if __name__ == "__main__":
    main()