class Point2d:
    def __init__(self, x: int, y:int):
        self.x: int = x 
        self.y: int = y



    def __str__(self):
        return f"({self.x}, {self.y})"
    
            









        
    




























































def main():

    shape = Shape()
    
    while True:
        line = input()

        args = line.split()
        print("$" + line)

        if args[0] == "end":
            break
        elif args[0] == "circle":

        elif args[0] == "react":

        elif args[0] == "show":
            print(shape)

        






























main()