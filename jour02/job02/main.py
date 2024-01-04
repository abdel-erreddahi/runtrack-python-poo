class livre:
    def __init__(self, titre, auteur, nombre_de_pages) -> None:
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        pass

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
    
    def set_titre(self, titre_modifie):
        self.__titre = titre_modifie
    
    def set_auteur(self, auteur_modifie):
        self.__auteur = auteur_modifie
    
    def set_nombre_de_pages(self, nombre_de_pages_modifie):
        self.__nombre_de_pages = nombre_de_pages_modifie
    
Livre = livre('la boite a merveille', 'Ahmed Sefrioui', '249 pages')

print("le titre du livre est ", Livre.get_titre())
print("le nom d'auteur de ce roman est", Livre.get_auteur())
print("le nombre de pages de ce roman est", Livre.get_nombre_de_pages())

Livre_modifie = livre('les amants de casablanca', 'Taher Ben Jelloun','336 pages')

print("le titre du livre est ", Livre_modifie.get_titre())
print("le nom d'auteur de ce roman est", Livre_modifie.get_auteur())
print("le nombre de pages de ce roman est", Livre_modifie.get_nombre_de_pages())

