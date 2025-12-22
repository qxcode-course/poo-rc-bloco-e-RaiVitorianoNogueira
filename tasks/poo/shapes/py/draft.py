import math
from abc import ABC, abstractmethod



class shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass


class Point2d:
    def __init__(self, x: int, y:int):
        self.x: int = x 
        self.y: int = y



    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
    



class Circle(shape):
    def __init__(self, center : Point2d, radius: float):
        self.center = center
        self.radius = radius
        






    def getName():
        return "Circ"
    



    def getArea():
        return math.pi * self.radius * self.radius



    def getPerimeter():
        return 2 * math.pi * self.radius





    def __str__(self):
        return f"Circ: C={self.center}, R={self.radius:.2f}"
    
class Rectangle:





def main():

    shapes = []
    
    while True:
        line = input()

        args = line.split()
        print("$" + line)

        if args[0] == "end":
            break
        elif args[0] == "circle":
            x = float(args[1])
            y = float(args[2])
            r = float(args[3])
            shapes.append(Circle(Point2D(x, y), r))


        elif args[0] == "show":
            for s in shapes:
                print(s) 


    except EOFError:
        break


if __name__ == "__main__":
main()