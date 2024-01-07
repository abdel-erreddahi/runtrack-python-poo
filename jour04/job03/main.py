class Rectangle:
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur_modifiee):
        self.__longueur = longueur_modifiee

    def set_largeur(self, largeur_modifiee):
        self.__largeur = largeur_modifiee


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur) -> None:
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur


# Utilisation
rectangle = Rectangle(20, 10)
print(f"Le périmètre du Rectangle est : {rectangle.perimetre()} cm")
print(f"La surface du Rectangle est : {rectangle.surface()} cm²")

parallelepipede = Parallelepipede(20, 10, 50)
print(f"Le volume du Parallélépipède est : {parallelepipede.volume()} cm³")