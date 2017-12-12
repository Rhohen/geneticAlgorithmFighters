class Personne:

    """Classe définissant une personne caractérisée par :

    - ses hp

    - son attaque

    - sa defense"""

    def __init__(self, hp, attaque, defense, generation): # Notre méthode constructeur     

        self.hp = hp
        self.currentHP = hp
        self.attaque = attaque
        self.defense = defense
        self.value = 0
        self.generation = generation
