import numpy as np


def printProbabilities(eachSideProbability):
    s = ""
    sum = 0
    for (side, probability) in eachSideProbability.items():
        sum += probability
        s += f"{probability} + "
        print(f"Side: {side}, Side probability: {probability}")
    s = s[:-2]
    s += f"= {sum}"
    print(s)


if __name__ == '__main__':

    values = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]

    for n in values:
        print(20*"-" + f"n={n}" + 20*"-")
        sequence = np.random.randint(1, 7, size=n)
        eachSideProbability = {i: 0 for i in range(1, 7)}

        for side in sequence:
            eachSideProbability[side] += 1

        for j in range(1, 7):
            eachSideProbability[j] /= n

        printProbabilities(eachSideProbability)