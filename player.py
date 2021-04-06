from fonction import verifPointStat, verifNum, verifNom, roles

class Joueur:
    def __init__(self,pret,nom,prenom,position,stat,prix):
        self.pret = pret
        self.nom = nom
        self.prenom = prenom
        self.position = position
        self.stat = stat
        #[vitesse,tirs,passes,dribles,défense,physique]
        self.stat = stat
        self.prix = prix
        
    def poste(self):
        posteRole = {1:"g",2:"dd",6:"dg",3:"md",7:"mg",4:"ad",8:"ag",5:"bu"}
        choixRole = False
        choixPied = False
        while not choixRole:
            role = input("Choisissez un role pour votre joueur :\n 1 - Gardien\n 2 - Défenseur\n 3 - Milieu\n 4 - Attaquant\n 5 - Buteur\n Son poste : ")
            if verifNum(role):
                role = int(role)
                if 0<role<6:
                    choixRole = True
                    if 1<role<5:
                        while not choixPied:
                            pied = input("Choisissez si votre joueur est: \n 0 - droitier\n 2 - gaucher\n Son pied : ")
                            if verifNum(pied):
                                pied = int(pied)
                                if pied in [0,2]:
                                    choixPied = True
                                    role += 2*pied
                                else:
                                    print("####choissez un nombre compris entre 0 et 2..####")
                else:
                    print("####Choissez un nombre compris entre 1 et 5..####")
            else:
                print("Vous n'avez pas sélectionné de nombre entier.\n")
        self.position = posteRole[role]

    def afficherJoueur(self,roles):
        print(f"########## {self.prenom} {self.nom} ##########\n")
        print(f"         Poste : {roles[self.position]}\n")
        print(f"    Tirs : {self.stat[1]}  |   Passes : {self.stat[2]}")
        print(f" Dribble : {self.stat[3]}  |  Dribles : {self.stat[4]}")
        print(f" Vitesse : {self.stat[0]}  |   Passes : {self.stat[5]}\n")
        print("       Moyenne :",self.moyenneStat())
    
    def moyenneStat(self):
        return (self.stat[0] + self.stat[1] + self.stat[2] + self.stat[3] + self.stat[4] + self.stat[5]) // 6

    def affichageRapide(self,roles):
        return f"{self.moyenneStat()} : {self.nom} {self.prenom} poste : {roles[self.position]}"

    def ajouterStat(self):
        liste = ["vitesse","tirs","passes","dribles","défense","physique"]
        pts = 400
        print(f"Vous pouvez ajouter {pts} points de compétence à votre joueur")
        print(f"Vous devez partagé vos points parmis ces {len(liste)} compétences :",liste)
        for index,compétence in enumerate(liste):
            ajout = False
            while not ajout:
                print(f"Il vous reste {pts} points.")
                skill = input(f"Nombre de point en {compétence} : ")
                if verifNum(skill):
                    skill = int(skill)
                    if verifPointStat(skill,pts):
                        ajout = True
                        pts -= skill
                        self.stat[index] = skill
                else:
                    print("Vous n'avez pas sélectionné de nombre entier.\n")
    
    def demanderPrenom(self):
        self.prenom = "--"
        self.nom = "--"
        while not verifNom(self.prenom):
            self.prenom = input("Entrer le prénom de votre joueur : ")
        while not verifNom(self.nom):
            self.nom = input("Entrer le nom de votre joueur : ").upper()


    def enregistrerJoueur(self,nomDoss):
        info = f"{self.pret};{self.nom};{self.prenom};{self.position};"
        for i in self.stat:
            info += str(i)+";"
        with open(nomDoss,"a") as doss:
            doss.write(info[:-1]+";"+str(self.prix)+"\n")


#############################
def creerJoueur():
    j = Joueur("i","--","--","",[0,0,0,0,0,0],100)
    j.demanderPrenom()
    j.poste()
    j.ajouterStat()
    j.afficherJoueur(roles)
    return j