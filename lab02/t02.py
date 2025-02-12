import numpy as np

class Deck:
    def __init__(self, faceValues, suits):
        self.faceValues = faceValues
        self.suits = suits
        self.faceValuesCount = len(faceValues)
        self.suitsCount = len(suits)

    def __getitem__(self, key):
        faceValueIndex, suitIndex = key
        assert faceValueIndex < self.faceValuesCount, "Invalid face value index"
        assert suitIndex < self.suitsCount, "Invalid suit index"
        return f"{self.faceValues[faceValueIndex]}{self.suits[suitIndex]}"


class Dealer:
    def __init__(self, deck):
        self.deck = deck

    def dealCards(self):
        playersCardSet = self.genCardSets()

        for i in range(4):
            s = f"Player {i+1} -> "
            for (faceValueIndex, suitIndex) in playersCardSet[i]:
                s += f"{self.deck[faceValueIndex, suitIndex]}, "
            yield s

    def genCardSets(self):
        suitsPermutation = np.random.permutation(4)
        suitsFaces = [list(range(self.deck.faceValuesCount)) for _ in range(self.deck.suitsCount)]
        result = [[] for _ in range(4)]

        for i in range(4):
            mainSuit = suitsPermutation[i]
            fourFaces = np.random.choice(suitsFaces[mainSuit], 4, replace=False)
            for f in fourFaces:
                suitsFaces[mainSuit].remove(f)
                result[i].append((f, mainSuit))

            for suit in range(4):
                if suit == mainSuit:
                    continue
                threeFaces = np.random.choice(suitsFaces[suit], 3, replace=False)
                for f in threeFaces:
                    suitsFaces[suit].remove(f)
                    result[i].append((f, suit))

        return result


if __name__ == '__main__':
    faceValues = ['1', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K']
    suits = ['♢', '♠', '♣', '♡']

    deck = Deck(faceValues, suits)
    dealer = Dealer(deck)

    for cardSet in dealer.dealCards():
        print(cardSet)