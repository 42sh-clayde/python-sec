import random

class generator():
    def __init__(self) -> None:
        self.characters = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789_$:)/!><#&-+@.?"
        self.length = 30 
        self.mdp = ""
        self.compteur = 0 
    
    def passgen(self):
        while self.compteur < self.length:
            word = self.characters[random.randint(0, len(self.characters)-1)] 
            self.mdp += word 
            self.compteur += 1
        return self.mdp