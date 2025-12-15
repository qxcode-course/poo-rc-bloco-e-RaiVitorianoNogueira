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
        super().__init__(vid, entrada, "Moto"):


    def calcularValor(self, saida: int) -> float:
        tempo = saida - self.entrada
        return tempo / 20
    


class Carro(self):

    





        
































def main():
    estacionamento = Estacionamento()

    while True:
        line = input().strip()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == ""

       
    






















main()