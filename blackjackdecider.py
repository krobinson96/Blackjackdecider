#!python3
# Written by Kody Robinson
from card import Card
import random, time

# Function to remove one card from playing deck and add to dead pile
def hitFunc(deck, hand, ddeck):
    ddeck.append(deck.pop(0))
    hand.append(ddeck[len(ddeck) - 1])
    return hand, ddeck

# Function to determine the worth of a particular hand
def detWorth(hand):
    temp = 0
    aces = count(hand, "ACE")
    for i in hand:
        temp = temp + i.cardWorth()
    if temp > 21 and aces > 0:
        for i in range(aces):
            temp -= 10
            if temp < 22:
                break
    return temp

# Function to determine of a target is contained within a hand
def contains(hand, target):
    flag = False
    for i in hand:
        if i.cardFace() == target:
            flag = True
    return flag

# Function to find number of targets in a hand
def count(hand, target):
    temp = 0
    for i in hand:
        if i.cardFace() == target:
            temp += 1
    return temp

# Function to populate a deck with 6 52-card decks
def popDeck(deck):
    for i in range(6):
        for j in range(4):
            for k in range(13):
                deck.append(Card(j, k))
    random.shuffle(deck)

# Function to add cards from dead deck to main deck and then reshuffle
def reshuffleDeck(deck, ddeck):
    for i in range(len(ddeck)):
        deck.append(ddeck.pop())
    random.shuffle(deck)
    return deck, ddeck

# Initializes variables for a new game
def initGame(deck, ddeck):
    player = []
    dealer = []
    player, ddeck = hitFunc(deck, player, ddeck)
    dealer, ddeck = hitFunc(deck, dealer, ddeck)
    player, ddeck = hitFunc(deck, player, ddeck)
    return player, dealer, deck, 0, 0

def printDealer1stHand(hand):
    string = ""
    suit = hand[0].cardSuit() # temp value to hold suit
    face = hand[0].cardFace() # temp value to hold face
    '''suit = suit.replace("SPADES","♠️")
    suit = suit.replace("HEARTS","♥️")
    suit = suit.replace("DIAMONDS","♦️")
    suit = suit.replace("CLUBS","♣️")
    face = str(face).replace("ACE","A")
    face = str(face).replace("JACK","J")
    face = str(face).replace("QUEEN","Q")
    face = str(face).replace("KING","K")'''
    print("------------")
    print("DEALER CARDS")
    print("------------")
    string += str(face) + " OF " + suit + " " 
    string += "\n" + str(hand[0].cardWorth()) + " - Dealer"
    print(string)
    return hand[0].cardWorth()    

# Updates hand worth and prints cards in hand
def printCards(hand, id):
    if id == 0:
        print("----------")
        print("YOUR CARDS")
        print("----------")
        for i in hand:
            i.printCard()
        handCards = detWorth(hand)
        print(str(handCards) + " - Player")
        return handCards
    else:
        print("------------")
        print("DEALER CARDS")
        print("------------")
        for i in hand:
            i.printCard()
        handCards = detWorth(hand)
        print(str(handCards) + " - Dealer")
        return handCards

def main(games):
    deck = []
    ddeck = []  # Dead deck to contain all cards that were played
    wins = 0
    global gamesPlayed
    popDeck(deck)
    for i in range(games):
        print("Game #" +  str(i+1))
        if len(deck) < 157:
            deck, ddeck = reshuffleDeck(deck, ddeck)
        player, dealer, deck, playerCards, dealerCards = initGame(deck, ddeck)
        playerCards = printCards(player, 0)
        dealerCards = printDealer1stHand(dealer)
        if playerCards == 21 and dealerCards < 21:
            print("You Win")
            wins += 1
            gamesPlayed += 1
            continue
        playerTurn = True
        while playerTurn:
            if contains(player, "ACE"):
                if playerCards < 18:
                    player, ddeck = hitFunc(deck, player, ddeck)
                    playerCards = printCards(player, 0)
                    continue
                elif playerCards == 18 and dealerCards > 8 and dealerCards < 12:
                    player, ddeck = hitFunc(deck, player, ddeck)
                    playerCards = printCards(player, 0)
                    continue
            else:
                if playerCards < 12:
                    player, ddeck = hitFunc(deck, player, ddeck)
                    playerCards = printCards(player, 0)
                    continue
                elif playerCards == 12 and (dealerCards == 2 or dealerCards == 3):
                    player, ddeck = hitFunc(deck, player, ddeck)
                    playerCards = printCards(player, 0)
                    continue
                elif dealerCards > 6 and dealerCards < 12:
                    if playerCards > 12 and playerCards < 17:
                        player, ddeck = hitFunc(deck, player, ddeck)
                        playerCards = printCards(player, 0)
                        continue
            playerTurn = False
        if playerCards > 21:
            print("You Lose")
            gamesPlayed += 1
            continue

        # DEALER TURN
        dealer, ddeck = hitFunc(deck, dealer, ddeck)
        dealerCards = printCards(dealer, 1)
        if dealerCards > playerCards and dealerCards > 16 and dealerCards < 22:
            print("------------")
            print(str(playerCards) + " - Player")
            print(str(dealerCards) + " - Dealer")
            print("You Lose")
            gamesPlayed += 1
            continue
        while dealerCards < 17:
            dealer, ddeck = hitFunc(deck, dealer, ddeck)
            dealerCards = printCards(dealer, 1)
            if dealerCards > 21:
                print("------------")
                print(str(playerCards) + " - Player")
                print(str(dealerCards) + " - Dealer")
                print("You Win")
                wins += 1
                gamesPlayed += 1
                continue
            elif dealerCards > 16 and dealerCards < 22 and dealerCards > playerCards:
                print("------------")
                print(str(playerCards) + " - Player")
                print(str(dealerCards) + " - Dealer")
                print("You Lose")
                gamesPlayed += 1
                continue
            elif dealerCards == 21 and not playerCards == 21:
                print("------------")
                print(str(playerCards) + " - Player")
                print(str(dealerCards) + " - Dealer")
                print("You Lose")
                gamesPlayed += 1
                continue
        else:
            if playerCards > dealerCards and playerCards < 22:
                print("------------")
                print(str(playerCards) + " - Player")
                print(str(dealerCards) + " - Dealer")
                print("You Win")
                gamesPlayed += 1
                wins += 1
                continue
        if dealerCards == playerCards:
            print("------------")
            print(str(playerCards) + " - Player")
            print(str(dealerCards) + " - Dealer")
            print("Push")
            main(1)
    print(f"{wins/gamesPlayed*100}% Won")

if __name__ == "__main__":
    gamesPlayed = 0
    main(int(input("# of Games: ")))
