try:
    note = float(input("Entre ta note sur 20 : "))

    if note >= 16:
        print("Très bien")
    elif note >= 14:
        print("Bien")
    elif note >= 12:
        print("Assez bien")
    elif note >= 10:
        print("Moyen")
    else:
        print("Insuffisant")

except ValueError:
    print("Note invalide")
