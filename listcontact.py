contacts = [
    {"nom": "Alice", "tel": "0601020304"},
    {"nom": "Bob", "tel": "0604050607"},
    {"nom": "Eva", "tel": "0611223344"}
]

for c in contacts:
    print(c.get("nom"))


recherche = input("Nom a chercher:")

for c in contacts:
    if c.get("nom") == recherche:
        print("Telephone: ",c.get("tel"))