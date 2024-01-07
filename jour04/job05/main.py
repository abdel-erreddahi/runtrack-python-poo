pi = 3.14
# J'ai choisoi de mettre les dimensions en m

class Forme:


    def __init__(self) -> None:
        pass

    def aire(self):
        return 0

class Cercle(Forme):


    def __init__(self, radius) -> None:
        super().__init__()
        self.__rayon = radius

    def aire(self):
        return pi * self.__rayon**2

class Rectangle(Forme):


    def __init__(self, largeur, hauteur) -> None:
        super().__init__()
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__largeur * self.__hauteur

cercle_instance = Cercle(radius=5)
rectangle_instance = Rectangle(largeur=4, hauteur=6)

print(f"Aire du cercle: {cercle_instance.aire()} m²")
print(f"Aire du rectangle: {rectangle_instance.aire()} m²")