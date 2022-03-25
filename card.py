class Card:
    def __init__(self,suit,face):
        self.suit = int(suit)
        self.face = int(face)

    def cardSuit(self):
        if self.suit == 0:
            return "SPADES"
        elif self.suit == 1:
            return "HEARTS"
        elif self.suit == 2:
            return "CLUBS"
        elif self.suit == 3:
            return "DIAMONDS"
    def cardWorth(self):
        if self.face == 0:
            return 11
        elif self.face < 10:
            return self.face + 1
        else:
            return 10
    def cardFace(self):
        if self.face == 0:
            return "ACE"
        elif self.face > 0 and self.face < 10:
            return self.face + 1
        elif self.face == 10:
            return "JACK"
        elif self.face == 11:
            return "QUEEN"
        elif self.face == 12:
            return "KING"
    def printCard(self):
        print(str(self.cardFace()) + " OF " + self.cardSuit())
    def __str__(self):
        return str(self.cardFace()) + " OF " + self.cardSuit()
    def __repr__(self):
        return self.__str__()
