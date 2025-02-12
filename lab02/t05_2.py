import numpy as np

def empiricalProbability(n):
    faceValues = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    evenValues = {'2', '4', '6', '8', '10'}
    suits = ['♢', '♠', '♣', '♡']

    neededCarts = {(i + j): 0 for i in evenValues for j in suits}

    deck = [(value, suit) for value in faceValues for suit in suits]

    sequence = np.random.randint(0, len(deck), size=n)

    for i in sequence:
        (faceValue, suit) = deck[i]
        if faceValue in evenValues:
            neededCarts[faceValue + suit] += 1

    return neededCarts

values = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]

for n in values:
    print(20*"-" + f"n={n}" + 20*"-")
    neededCards = empiricalProbability(n)

    for (card, count) in neededCards.items():
        print(f"Probability for: {card} = {count/n}")

    print()


