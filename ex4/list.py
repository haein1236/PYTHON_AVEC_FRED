fruits = ["Pomme", "Banane", "Mangue", "Orange", "Fraise"]

nouveau = input("Ajouter un fruits: ")
fruits.append(nouveau)

print(fruits)

supp = input("Supprimer un fruits: ")

if supp in fruits:
    fruits.remove(supp)

    print(sorted(fruits)) 
