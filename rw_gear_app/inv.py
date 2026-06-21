import math


def getAlpha(alp):
    inv_alp = alp
    guess = 0.35
    epsilon = 0.00000001
    while abs((math.tan(guess) - guess) - inv_alp) >= epsilon:
        guess = guess - ((math.tan(guess) - guess) - inv_alp) / ((1 / (math.cos(guess))**2) - 1)
        if(guess > 1 or guess < 0.001):
            return 0
            break
    if(guess < 1 and guess > 0.001):
        return guess
