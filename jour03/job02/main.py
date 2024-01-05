class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom et prénom : {self.__nom} {self.__prenom}")
        print(f"Solde : {self.__solde} €")
        print(f"Autorisation de découvert : {'Oui' if self.__decouvert else 'Non'}")

    def afficher_solde(self):
        print(f"Solde du compte : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Solde insuffisant. Opération impossible.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios de {agios} € appliqués. Nouveau solde : {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire.__numero_compte}.")
        else:
            print("Solde insuffisant. Opération de virement impossible.")


# Création d'une instance de la classe CompteBancaire
compte1 = CompteBancaire(numero_compte="123456", nom="Dupont", prenom="Jean", solde=1000)
compte1.afficher()

# Création d'une deuxième instance de la classe CompteBancaire avec découvert
compte2 = CompteBancaire(numero_compte="789012", nom="Durand", prenom="Marie", solde=-500, decouvert=True)
compte2.afficher()

# Versement du premier compte vers le compte à découvert
compte1.virement(compte2, 500)
compte1.afficher()
compte2.afficher()
