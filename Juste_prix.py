from random import randint

# compteur point
compteur = 100

# prix à deviner
juste_prix = randint(1, 1000)
print("Bienvenue au Juste Prix !")
print(f"Vous avez {compteur} points")

# fourchette prix
x = max(1, juste_prix - randint(10, 100))
y = min(1000, juste_prix + randint(10, 100))
print(f"Le prix est entre {x} et {y}")


def erreur(string):
    try:
        return int(string)
    except ValueError:
        return False


# lancement
lancement = True

# debut
while lancement:

    # prix donné
    prix_client = erreur(input("Votre Prix : "))
    if prix_client == False:
        print("Seul les nombres entier sont acceptés")
        continue

    # victoire
    if prix_client == juste_prix:
        print("C'est gagné")
        lancement = False

    # c'est plus
    elif prix_client < juste_prix:
        print("C'est plus")
        compteur -= 1

    # c'est  moins
    elif prix_client > juste_prix:
        print("C'est moins")
        compteur -= 1

print("Fin du jeu")
