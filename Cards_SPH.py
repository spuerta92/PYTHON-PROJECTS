# Cards
# Sebastian Puerta Hincapie

class Card(object):
    def __init__(self,suit=1,rank=2):
        if suit < 1 or suit > 4:
            print("invalid suit, setting to 1")
            suit = 1
        self.suit = suit
        self.rank = rank

    def value(self):
        """ we want things order primarily by rank then suit """
        return self.suit + (self.rank-1)*14

    #if we include this to allow for comparisons with < and > between cards
    def __lt__(self,other):
        return self.value() < other.value()

    # Python 2 by default uses ASCII, Python 3 uses Unicode
    def __unicode__(self):
        suit = [u"\u2668", #spade
                u"\u2665", #heart
                u"\u2666", #diamond
                u"\u2777"] #club
        r = str(self.rank)
        if self.rank == 11:     r = "J"
        elif self.rank == 12:   r = "Q"
        elif self.rank == 13:   r = "K"
        elif self.rank == 14:    r = "A"

        return r + ':' + suit[self.suit-1]

    def __str__(self):
        return self.__unicode__()   # .encode("utf-8")

class Deck(object):
    """ the deck is a collection of cards """
    def __init__(self):
        self.nsuits = 4
        self.nranks = 13
        self.minrank = 2
        self.maxrank = self.minrank + self.nranks - 1

        self.cards = []

        for rank in range(self.minrank,self.maxrank+1):
            for suit in range(1,self.nsuits+1):
                self.cards.append(Card(rank=rank,suit=suit))

        def shuffle(self):
            random.shuffle(self.cards)

        def get_cards(self,num=1):
            hand = []
            for n in range(num):
                hand.append(self.cards.pop())
            return hand

        def __str__(self):
            string = ""
            for c in self.cards:
                string += str(c) + " "
            return string
                           
def main():
    # test Card class
    c1 = Card()
    print(c1)
    c2 = Card(3,4)
    print(c2)
    c3 = Card(17,12)
    print(c1 < c2)
    print(c2 > c1)
    c1.value()

    # test Deck class
    mydeck = Deck()
    print("This is my deck")
    print(mydeck)
    print("The length of the deck is: ")
    print(len(mydeck.cards))
    input("Press a key to continue with dealing a hand...")
    print("Shuffling the deck...")
    mydeck.shuffle()
    print("this is your hand")
    hand = mydeck.get_cards(5)
    for c in sorted(hand) : print(c)

main()
