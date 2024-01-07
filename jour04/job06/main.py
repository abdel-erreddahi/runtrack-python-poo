class Vehicule:

    def __init__(self, marque, modele, annee, prix, message = "Attention, je roule") -> None:
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix
        self.__message = message

    def informationsVehicule(self):
        infos = f"Marque = {self.__marque}\n" \
                f"Modèle = {self.__modele}\n" \
                f"Année = {self.__annee}\n" \
                f"Prix = {self.__prix} euros."
        return infos
    
    def get_demarrer(self):
        return self.__message
    

class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix, portes=4) -> None:
        super().__init__(marque, modele, annee, prix)
        self.__portes = portes

    def informationsVehicule(self):
        infos = super().informationsVehicule()
        return f"{infos}\nNombre de portes = {self.__portes}"
    
    def set_demarrer(self, personnalise_message):
        self.__message = personnalise_message
        return personnalise_message
    
class Moto(Vehicule):

    def __init__(self, marque, modele, annee, prix, roue = 2) -> None:
        super().__init__(marque, modele, annee, prix)
        self.__roue = roue

    def informationsVehicule(self):
        infos = super().informationsVehicule()
        return f"{infos}\nNombre de roue = {self.__roue}"
    
    def get_demarrer(self):
        return self.__message
    
    def set_demarrer(self, personnalise_message):
        self.__message = personnalise_message
        return personnalise_message



voiture = Voiture(marque="Mercedes", modele="Class A", annee=2020, prix=18500, portes=4)

# Les infos sur la voitures
print("A.LES INFOS SUR LA VOITURE :")
print(voiture.informationsVehicule())
print(voiture.set_demarrer("Ma Mercedes vient d'être demarrer et elle roule"))

print('\n')

# Les infos sur la moto
moto = Moto(marque="Yamaha", modele="1200 Vmax", annee="1987", prix=4500)
print("B.LES INFOS SUR LA MOTO :")
print(moto.informationsVehicule())
print(moto.set_demarrer("Je viens de demarrer ma Moto, On se capte plus tard"))