from fonction import*

class Team:
    def __init__(self,nom,joueurs,formation,argent):
        self.nom = nom
        self.joueurs = joueurs
        self.formation = formation
        self.argent = argent
    
    def choisirJoueur(self,listeJ):
        while True:
            print("Voici les joueurs que vous pouvez acheter : \n")
            i = 0
            for j in listeJ:
                if j.pret == "i":
                    i += 1
                    stat = j.affichageRapide(roles)
                    print(f"{i} - {stat}")
            print("Choisissez 6 joueurs pour votre équipe ex : (7,8,11,2)")
            nbj = input(">> : ")
            n=0
            while n < len(nbj):
                nb = nbj[n]
                if verifNum(nb):
                    if n+1 < len(nbj):
                        n += 1
                    else:
                        self.joueurs.append(listeJ[int(nb)-1])
                        break
                    while verifNum(nbj[n]):
                        nb += nbj[n]
                        if n+1 < len(nbj):
                            n += 1
                        else:
                            self.joueurs.append(listeJ[int(nb)-1])
                            break
                    else:
                        self.joueurs.append(listeJ[int(nb)-1])
                n += 1
            if len(self.joueurs)==6:
                return
            elif len(self.joueurs)>6:
                print("Vous avez choisi trop de joueur")
            else:
                print("Vous n'avez pas choisi assez de joueur")
    
    def choisirFormation(self,formations):
        print("_____________")
        print(formations[0])
        print("_____________")
        print(formations[1])
        print("_____________")
        print(formations[2])

        while True:
            forma = input("Choisissez la fomation qui vous plait (1 ,2 ou 3) : ")
            if verifNum(forma):
                forma = int(forma)
                if 0<forma<4:
                    self.formation = forma
                    return
                else:
                    print("Choisissez un nombre entre 1 et 3.\n")
            else:
                print("Vous n'avez pas sélectionné de nombre entier.\n")
    
    def compo(self,formations):
        print("######################################################################################")
        print(formations[self.formation-1])
        print("_____________")
        i = 0
        for j in self.joueurs:
            i += 1
            stat = j.affichageRapide(roles)
            print(f"{i} - {stat}")
        print("L'ordre des joueurs vont de gauche à droite et de haut en bas.")
        for i in range(5):
            input(f"Entrer le numéro du joueur {i+1} : ")
        input(f"Entrer le numéro du gardien : ")

###############################
def creerTeam(listeJ):
    t1 = Team("Aiglons Durtalois",[],0,800)
    t1.choisirFormation(formations)
    t1.choisirJoueur(listeJ)
    t1.compo(formations)