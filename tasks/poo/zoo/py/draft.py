from typing import Any
from abc import ABC, abstractmethod

class Brinquedo(ABC):
    def __init__(self, nome: str = "") -> None:
        self.nome = nome

    @abstractmethod
    def apertar(self):
        pass

    @abstractmethod
    def jogar_no_chao(self):    
        pass 

    

def brincar(briquedo: Brinquedo):
    brinquedo.apertar()
    brinquedo.jogar_no_chao()
    print(brinquedo)



class Ursinho(Brinquedo):

    def __init__(self) -> None:
        self.nome = "Ursinho de pelúcia"
    def apertar(self) -> None:
        print("O ursinho é macio!")

    def jogar_no_chao(self) -> None:
        print("O ursinho quica!")

    def __str__(self) -> str:
        return "Ursinho de pelúcia"
    


class Mordedor(Brinquedo):
    def apertar(self) -> None:
        print("O mordedor faiz barulho")

class Chinela():
    def apertar(self) -> None:




    
