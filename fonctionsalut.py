def saluer(prenom, civilite="M.", passion="sourit"):
    return f"Bonjour {civilite} {prenom} {passion} "


print(saluer("Dupont"))
print(saluer("Durand", "Mme"))
