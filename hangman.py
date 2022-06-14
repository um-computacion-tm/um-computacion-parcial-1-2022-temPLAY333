
from invalidassignmentexception import InvalidAssignmentException

class Hangman():
    def __init__(self):
        self.word = False
        self.lifes = 5
        self.tries = []

    def set_word(self, word):
        self.word = str(word).lower()

    def show(self):
        display = "Lifes: " + repr(self.lifes) + " - Word: "
        if self.word == False:
            print("Choose a word firts, please")
        else:
            for letra in self.word:
                if letra in self.tries:
                    display += letra + " "
                else:
                    display += "_ "
        return display
                
    def assign(self, letter):
        if letter == "x":
            self.lifes = 2
        for letra in self.word:
            if letter.lower() == letra:
                if letter in self.tries:
                    self.lifes -= 1
                    raise InvalidAssignmentException
                self.tries.append(letter.lower())
                break
        else:
            self.lifes -= 1
            raise InvalidAssignmentException
        return True
        
    def winner(self):
        count = 0
        for letra in self.word:
            if letra in self.tries:
                count += 1
        if count == len(self.word):
            return True
        else:
            return False

    def play(self):
        estado = False
        while estado == False:
            letra = input("Dime una letra: ")
            try:
                self.assign(letra)
            except:
                InvalidAssignmentException
            if self.winner() == True:
                return "Ganaste"
            if self.lifes == 0:
                return "Perdiste"
