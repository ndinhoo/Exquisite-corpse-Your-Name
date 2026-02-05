import random

p1 = input("Pierre, Feuille, Ciseaux : ")

p2 = random.choice(["Pierre", "Feuille", "Ciseaux"])

if p1 == "Pierre" and p2 == "Ciseaux":
    print("You won ✨")