class Forme:
    def __init__(self) -> None:
        pass

    def aire(self):
        return 0
        

class Rectangle(Forme):
    def __init__(self, largeur, hauteur) -> None:
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__largeur * self.__hauteur


rectangle = Rectangle(5, 10)
aire_rectangle = rectangle.aire()
print(f"L'aire du rectangle est : {aire_rectangle} cm²")