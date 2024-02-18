import random

def randomBeer(array):
    randomBeer = random.choice(array)
    return randomBeer

randomBeers = ["Dark", "Light", "Hazy"]

selectedBeer = randomBeer(randomBeers)

print(selectedBeer)