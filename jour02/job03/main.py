class livre:
    def __init__(self, titre, auteur, nombre_de_pages, disponible = True) -> None:
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = disponible
        pass

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
    
    def verification(self):
        return self.__disponible
    
    def get_emprunter(self):
       if self.verification():
            print("Le livre a été emprunté :")
            self.__disponible = False
            return True
    
    def set_emprunter(self):
        return not self.__disponible
    
    def set_titre(self, titre_modifie):
        self.__titre = titre_modifie
    
    def set_auteur(self, auteur_modifie):
        self.__auteur = auteur_modifie
    
    def set_nombre_de_pages(self, nombre_de_pages_modifie):
        self.__nombre_de_pages = nombre_de_pages_modifie
    
    def rendre(self):
        if self.set_emprunter():
            print("Le livre a été rendu :")
            self.__disponible = True
            return self.verification() == False

    
    
Livre = livre('la boite a merveille', 'Ahmed Sefrioui', '249 pages', 'disponible')

print("le titre du livre est ", Livre.get_titre())
print("le nom d'auteur de ce roman est", Livre.get_auteur())
print("le nombre de pages de ce roman est", Livre.get_nombre_de_pages())
print("Disponibilité du livre :", Livre.verification())
print(Livre.get_emprunter())


print("Disponible après emprunt :", Livre.verification())
print(Livre.rendre())

Livre_modifie = livre('les amants de casablanca', 'Taher Ben Jelloun','336 pages')

print("le titre du livre est ", Livre_modifie.get_titre())
print("le nom d'auteur de ce roman est", Livre_modifie.get_auteur())
print("le nombre de pages de ce roman est", Livre_modifie.get_nombre_de_pages())
