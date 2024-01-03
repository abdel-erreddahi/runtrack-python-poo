class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA / 100  # Convertir le pourcentage de TVA en décimal

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficher(self):
        infos = f"Produit : {self.nom}\n"
        infos += f"Prix HT : {self.prixHT} €\n"
        infos += f"TVA : {self.TVA * 100}%\n"
        infos += f"Prix TTC : {self.calculerPrixTTC()} €"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

# Création de plusieurs produits
produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 400, 15)

# Affichage des informations initiales
print("Produit 1:")
print(produit1.afficher())
print("\nProduit 2:")
print(produit2.afficher())

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Laptop")
produit1.modifierPrixHT(900)

produit2.modifierNom("Smartphone")
produit2.modifierPrixHT(450)

# Affichage des informations après modification
print("\nAprès modification :")
print("Produit 1:")
print(produit1.afficher())
print("\nProduit 2:")
print(produit2.afficher())
