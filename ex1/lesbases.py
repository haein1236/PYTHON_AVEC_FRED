try:
    n = int(input("Entre un entier : "))

    if n > 0:
        print("positif")
    elif n < 0:
        print("négatif")
    else:
        print("zéro")

except ValueError:
    print("Ce n’est pas un nombre valide")
