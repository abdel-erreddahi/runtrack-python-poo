class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Résultat de l'addition:", resultat)

# Instanciation de la classe
operation_instance = Operation()

# Appel de la méthode addition
operation_instance.addition()
