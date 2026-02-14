total = 0
count = 0

while True:
    val = input("Entre un nombre (stop pour finir) : ")

    if val.lower() == "stop":
        break

    try:
        num = float(val)
        total += num
        count += 1

    except ValueError:
        print("Entrée invalide")

if count > 0:
    moyenne = total / count
    print("Nombre :", count)
    print("Somme :", total)
    print("Moyenne :", moyenne)
else:
    print("Aucune valeur saisie")
