class Ville:
    def __init__(self, nom, nb_habitants) -> None:
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitants


class Personne:
    def __init__(self, nom, age, objet_ville) -> None:
        self.__nom = nom
        self.__age = age
        self.__objet_ville = objet_ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_objet_ville(self):
        return self.__objet_ville

    def ajouter_population(self, nb_habitants_ajoutes):
        self.__objet_ville._Ville__nb_habitants += nb_habitants_ajoutes
        print(f'Mise à jour de la population de la ville de {self.__objet_ville.get_nom()}: {self.__objet_ville.get_nb_habitants()} habitants')


# Les villes et le nombre d'habitants
Ville1 = Ville('Paris', 1000000)
Ville2 = Ville('Marseille', 861635)

# Les personnes qui seront ajoutées
personne1 = Personne('John', '45 ans', Ville1)
personne2 = Personne('Myrtille', '4 ans', Ville1)
personne3 = Personne('Chloe', '18 ans', Ville2)

print('Population de la ville de', Ville1.get_nom(), ':', Ville1.get_nb_habitants(), 'habitants')
print('Population de la ville de', Ville2.get_nom(), ':', Ville2.get_nb_habitants(), 'habitants')

# Ajout de population par les personnes
personne1 and personne2.ajouter_population(2)
personne3.ajouter_population(1)