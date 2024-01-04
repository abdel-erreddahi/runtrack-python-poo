class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
        else:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")

    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__statut_commande = "annulée"

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés:")
        for nom_plat, details in self.__plats_commandes.items():
            print(f"- {nom_plat}: {details['prix']} € ({details['statut']})")
        print(f"Total à payer : {self.__calculer_total()} €")
        print(f"Statut de la commande : {self.__statut_commande}")

    def calculer_tva(self):
        tva = self.__calculer_total() * 0.20  # 20% de TVA, ajustez selon vos besoins
        return tva

# Exemple d'utilisation de la classe Commande
commande1 = Commande(1)

# Ajout de plats à la commande
commande1.ajouter_plat("Pizza", 12)
commande1.ajouter_plat("Salade", 8)

# Affichage de la commande
commande1.afficher_commande()

# Calcul de la TVA
tva_commande1 = commande1.calculer_tva()
print(f"TVA à payer : {tva_commande1} €")

# Annulation de la commande
commande1.annuler_commande()

# Affichage de la commande annulée
commande1.afficher_commande()
