class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

# Instanciation de la classe Point
point1 = Point(3, 4)

# Utilisation des méthodes
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()

point1.changerX(5)
point1.changerY(8)

point1.afficherLesPoints()
