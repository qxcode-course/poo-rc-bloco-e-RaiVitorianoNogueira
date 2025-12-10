from typing import Any
from abc import ABC, abstractmethod

class Brinquedo(ABC):
    @abstractmethod
    def apertar(self):
        pass

    @abstractmethod
    def jogar_no_chao(self):    
        pass

def brincar(briquedo: Any):



class Ursinho(Brinquedo) -> None:
    def apertar(self):
        print("O ursinho é macio!")

    def jogar_no_chao(self) -> None:
        print("O ursinho quica!")

    def __str__(self) -> str:
        return "Ursinho de pelúcia"
    


class Chinela()
    
