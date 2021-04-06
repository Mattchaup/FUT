roles ={"g":"Gardien","mg":"Milieu Gauche","md":"Milieu Droit",
        "dd":"Défenceur Droit","dg":"Défenceur Gauche","ag":"Attaquant Gauche",
        "ad":"Attaquant Droit","bu":"Buteur"}

formations=["   ---o---\n   -o---o-\n   --o-o--",
            "   --o-o--\n   -o---o-\n   ---o---",
            "   ---o---\n   -o-o-o-\n   ---o---"]

def verifPointStat(n,pts):
    if n > 100:
        print("Vous ne pouvez pas miser plus de 100 points")
        return False
    if 0<=n<=pts and n<=100:
        return True
    print("Vous ne pouvez pas miser ce nombre de point")
    return False 

def verifNum(nbr):
    if nbr == "":
        print("Vous n'avez rien entré")
        return False
    for chiffre in nbr:
        if chiffre not in ["0","1","2","3","4","5","6","7","8","9"]:
            return False
    return True

def verifNom(nom):
    if nom == "--":
        return False
    for lettre in nom:
        if lettre == ";":
            print("Vous ne pouvez pas utiliser ce caractère -> ;")
            return False
    if len(nom) >= 15:
        print("Le nom que vous avez rentré est trop long")
        return False
    if len(nom) == 0:
        print("Vous n'avez rien saisi")
        return False
    return True

def recupDonnee(nomDoss):
    info = []
    with open(nomDoss,"r") as doss:
        listeJ = doss.readlines()
        for joueur in listeJ:
            info.append(joueur[:-1].split(";"))
    return info
