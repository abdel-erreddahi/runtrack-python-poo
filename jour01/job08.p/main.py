import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Rayon du cercle : {self.rayon}")
        print(f"Diamètre du cercle : {self.diametre()}")
        print(f"Circonférence du cercle : {self.circonference()}")
        print(f"Aire du cercle : {self.aire()}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles avec des rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
print("Cercle 1:")
cercle1.afficherInfos()

print("\nCercle 2:")
cercle2.afficherInfos()
