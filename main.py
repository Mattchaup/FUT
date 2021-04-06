from player import*
from team import creerTeam
from fonction import*

nomDoss = "listeJoueur.txt"
listeInfo = recupDonnee(nomDoss)

listeJoueur = []
for j in listeInfo:
    listeJoueur.append(Joueur(j[0],j[1],j[2],j[3],[int(j[4]),int(j[5]),int(j[6]),int(j[7]),int(j[8]),int(j[9])],j[10]))

#creerTeam(listeJoueur) #Pour créer une équipe
#nouvJ = creerJoueur() #Pour créer un joueur
#nouvJ.enregistrerJoueur(nomDoss) #Enregistré ce nouveau joueur