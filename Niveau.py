import pygame
from Labyrinthe import *
from Joueur import *
from Constantes import *
from Patern import *
from Monstres import *
from Potion import *
from Inventaire import *
from Collisions import *
from Meute import *
from Evenement import *
from Animation import *
from Affichage import *
from Clee import *
from Murs import *
from Minimap import *
from Pnjs import *
from Cailloux import *

class Niveau:
    def __init__(self,niveau,difficulte,mode_affichage,mode_minimap,debut_niveau=False,joueur=None,labyrinthe=None,entitees=None,evenements=None,horloge_cycle=None):
        
        self.mode_affichage = mode_affichage
        self.difficulte = difficulte
        self.mode_minimap = mode_minimap
        self.niveau = niveau
        if self.mode_affichage == voir_tout :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
        elif self.mode_affichage == aveugle :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
        elif self.mode_affichage == parcours_en_profondeur :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1
        elif self.mode_affichage == distance_max :
            self.LARGEUR_CASE = 20
            self.LARGEUR_MUR = 1

        if labyrinthe == None:
            if niveau == 0:
                if difficulte == BEGINNER :
                    self.CASES_X = 20
                    self.CASES_Y = 20
                    res = True
                    #self.salles=[Patern((8,8),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.5
                    self.teleporteurs = []
                elif difficulte == EASY :
                    self.CASES_X = 20
                    self.CASES_Y = 20
                    res = False
                    #self.salles=[Patern((14,14),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.4
                    self.teleporteurs = []
                elif difficulte == AVERAGE :
                    self.CASES_X = 40
                    self.CASES_Y = 40
                    res = False
                    #self.salles=[Patern((17,17),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.3
                    self.teleporteurs = []
                elif difficulte == HARD :
                    self.CASES_X = 60
                    self.CASES_Y = 60
                    res = False
                    #self.salles=[Patern((10,29),40,2,self.LARGEUR_CASE,self.LARGEUR_MUR,[])]
                    #on génère les entrées de manière a avoir un espace ouvert
                    #self.salles[0].pre_gen_entrees_x(0,0,39)
                    #self.salles[0].pre_gen_entrees_x(1,0,39)
                    proba_murs = 0.2
                    self.teleporteurs = []
                elif difficulte == INSANE :
                    self.CASES_X = 100
                    self.CASES_Y = 100
                    res = False
                    #self.salles=[Patern((49,30),2,40,self.LARGEUR_CASE,self.LARGEUR_MUR)]
                    proba_murs = 0.1
                    self.teleporteurs = []
                elif difficulte == IMPOSSIBLE :
                    self.CASES_X = 1000
                    self.CASES_Y = 1000
                    res = False
                    self.salles=[]
                    proba_murs = 0
                    self.teleporteurs = []

                self.clees = [Clee((3,3),"goodooKey")]
                
                self.salles=[Patern((0,0),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[9,9]],self.clees)]
                self.depart = (0,0)
                self.arrivee = (self.CASES_X-1,self.CASES_Y-1)
                #variables correspondants a la largeur et la hauteur du zoom

            elif niveau == "tuto1":
                self.CASES_X = 15
                self.CASES_Y = 3
                self.arrivee = (14,1)
                self.depart = (1,1)
                res = False
                self.clees = []
                self.salles = [Patern((0,0),14,3,self.LARGEUR_CASE,self.LARGEUR_MUR,[[13,1]],[Clee(None,"Premier pas")])]
                proba_murs = 1
                self.teleporteurs = [[(3,1),Teleporteur(["tuto1",(12,1)],self.LARGEUR_CASE,self.LARGEUR_MUR)]]
                
            elif niveau == "tuto2":
                #niveau labyrinthique sans monstres pour apprendre à se déplacer

                self.CASES_X = 40
                self.CASES_Y = 40
                self.arrivee = (39,39)
                self.depart = (0,0)
                res = False
                self.clees = [Clee((1,1),"Nord"),Clee((3,18),"Ouest"),Clee((5,35),"Est"),Clee((35,18),"Sud")]
                self.salles=[Patern((0,0),20,20,self.LARGEUR_CASE,self.LARGEUR_MUR,[[15,19],[16,19],[17,19],[18,19],[19,19],[19,18],[19,17],[19,16],[19,15]],[],False),Patern((20,20),20,20,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[3,0],[2,0],[1,0],[0,0],[0,1],[0,2],[0,3],[0,4]],[],False),Patern((0,0),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,3]]),Patern((15,15),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1],[0,8],[9,1],[9,8]],self.clees)]
                self.clees.append(Clee((19,1),"Bonus_1"))
                proba_murs = 0.1
                self.teleporteurs = []

            elif niveau == "tuto3":
                #niveau monstrueux sans trop de labyrinthe pour apprendre à se battre

                self.CASES_X = 10
                self.CASES_Y = 60
                self.arrivee = (5,59)
                self.depart = (5,0)
                res = False
                self.clees = [Clee((0,59),"Bonus_2")]
                self.salles=[Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]),Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0]]),Patern((0,0),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,3]],[Clee(None,"Bonus_1")])]
                proba_murs = 0.3
                self.teleporteurs = []

            elif niveau == "tuto4":
                #niveau monstrueux sans labyrinthe pour apprendre à se battre

                self.CASES_X = 10
                self.CASES_Y = 60
                self.arrivee = (5,59)
                self.depart = (5,0)
                res = False
                self.clees = [Clee((0,59),"Bonus_3")]
                self.salles=[Patern((4,0),2,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,9],[1,9]]),Patern((1,13),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((1,25),6,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((2,40),8,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0],[5,7]]),Patern((4,52),5,8,self.LARGEUR_CASE,self.LARGEUR_MUR,[[4,0]]),Patern((0,56),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((0,52),4,4,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,0],[2,3]],[Clee(None,"Bonus_2"),Clee(None,"Bonus_1")])]
                proba_murs = 0.2
                self.teleporteurs = []

            elif niveau == "tuto5":
                #niveau monstrueux sans labyrinthe pour apprendre à se battre contre des meutes

                self.CASES_X = 16
                self.CASES_Y = 16
                self.arrivee = (13,14)
                self.depart = (1,2)
                res = False
                self.salles=[Patern((0,0),16,16,self.LARGEUR_CASE,self.LARGEUR_MUR,[]),Patern((0,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,0],[2,13]],[Clee(None,"Bonus_3")]),Patern((3,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((6,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,1],[2,13]]),Patern((9,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,13],[2,1]]),Patern((12,1),3,15,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,13],[0,1]],[Clee(None,"Bonus_3")])]
                proba_murs = 0
                self.teleporteurs = []

            elif niveau == "tuto6":
                #niveau avec labyrinthe et montres pour apprendre l'utilité des potions

                self.CASES_X = 40
                self.CASES_Y = 40
                self.arrivee = (39,39)
                self.depart = (0,0)
                res = False
                self.clees = [Clee((3,38),"Porte_1_niveau_6_tutoriel"),Clee((37,4),"Porte_2_niveau_6_tutoriel"),Clee((25,7),"Porte_3_niveau_6_tutoriel"),Clee((8,22),"Porte_4_niveau_6_tutoriel"),Clee((17,38),"Porte_5_niveau_6_tutoriel"),Clee((38,13),"Porte_6_niveau_6_tutoriel"),Clee((21,22),"Porte_7_niveau_6_tutoriel"),Clee((17,23),"Porte_8_niveau_6_tutoriel")]
                self.salles=[Patern((0,0),11,11,self.LARGEUR_CASE,self.LARGEUR_MUR,[[10,1]]),Patern((0,30),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[8,0],[9,0],[9,1]]),Patern((8,27),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[3,0],[0,4]],[Clee(None,"Bonus_2"),Clee(None,"Bonus_3")]),Patern((30,0),10,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,8],[0,9],[1,9]]),Patern((27,8),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[3,4],[4,0]],[Clee(None,"Bonus_1"),Clee(None,"Bonus_3")]),Patern((35,35),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,4],[0,3],[0,2],[0,1],[1,0],[2,0],[3,0],[4,0]],self.clees),Patern((24,5),3,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[1,9]]),Patern((5,19),5,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[2,0]]),Patern((15,35),10,5,self.LARGEUR_CASE,self.LARGEUR_MUR,[[5,0]],[Clee(None,"Porte_7_niveau_6_tutoriel")]),Patern((35,15),5,10,self.LARGEUR_CASE,self.LARGEUR_MUR,[[0,5]],[Clee(None,"Porte_3_niveau_6_tutoriel")])]
                self.clees = self.clees + [Clee((5,6),"Bonus_4"),Clee((28,37),"Bonus_5"),Clee((38,17),"Bonus_6")]
                proba_murs = 0.2
                self.teleporteurs = []

            self.poids=[6,2,1,2]
            #génération du labyrinthe
            self.lab=Labyrinthe(self.CASES_X,self.CASES_Y,self.arrivee,self.depart,self.LARGEUR_CASE,self.LARGEUR_MUR,self.poids,self.salles,self.teleporteurs)
            print (self.lab.matrice_cases)
            self.lab.generation(proba_murs,None,None)

        else:
            self.lab = labyrinthe
            self.arrivee = self.lab.arrivee
            self.depart = self.lab.depart




        if joueur == None:
            print("halfbadcheck")
            if niveau == 0:
                inventaire_joueur = Inventaire()
            #    if difficulte == BEGINNER :
            #    elif difficulte == EASY :
            #    elif difficulte == AVERAGE :
            #    elif difficulte == HARD :
            #    elif difficulte == INSANE :
            #    elif difficulte == IMPOSSIBLE :
            elif niveau == "tuto1":
                inventaire_joueur = Inventaire([Clee(None,"Premier pas")])
            elif niveau == "tuto2":
                inventaire_joueur = Inventaire()
            elif niveau == "tuto3":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1")])
            elif niveau == "tuto4":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1"),Clee(None,"Bonus_2")])
            elif niveau == "tuto5":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1"),Clee(None,"Bonus_2"),Clee(None,"Bonus_3")])
            elif niveau == "tuto6":
                inventaire_joueur = Inventaire([Clee(None,"Bonus_1"),Clee(None,"Bonus_2"),Clee(None,"Bonus_3")])
                
            self.force_joueur = 10
            self.hp_joueur = 200
            self.vitesse_joueur_lab=3
            self.vitesse_joueur_autres=6
            minimap = Minimap(self.lab.getMatrice_cases(),mode_minimap,self.depart,self.arrivee)

            #variables correspondants a la largeur et la hauteur du zoom
            self.zoom_largeur=13
            self.zoom_hauteur=13

            self.joueur=Joueur(minimap,inventaire_joueur,self.hp_joueur,self.hp_joueur,self.force_joueur,self.vitesse_joueur_lab,self.vitesse_joueur_autres,2,self.zoom_largeur,self.zoom_hauteur,self.depart)
            
        elif debut_niveau:

            minimap = Minimap(self.lab.getMatrice_cases(),mode_minimap,self.depart,self.arrivee)
            self.joueur = Joueur(minimap,joueur.inventaire,joueur.pv_max,joueur.pv_max,joueur.degats,joueur.vitesse_lab,joueur.vitesse_autres,joueur.radius,joueur.largeur_vue,joueur.hauteur_vue,self.depart)

        else:

            self.joueur = joueur




        if entitees == None:

            if niveau == 0:
                
                self.vitesse_montres=20
            
                monstres=[Slime([10,13]),Fatti([15,12])]

                self.entitees = self.clees

                #pnj d'expérimentation
                self.pnj = Pnj_passif([4,4],100,(125,255,125),[Replique("Teswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwt",20)])
                self.entitees.append(self.pnj)

                potions_vue=[Potion_de_vision((35,26),self.joueur),Potion_de_vision((27,38),self.joueur),Potion_de_vision((21,19),self.joueur),Potion_de_visibilite_permanente((8,7),self.joueur)]
                potions_combat=[Potion_de_force((i,j),self.joueur)for j in range(5,45,10) for i in range(5,45,10)] + [Potion_de_portee((i,j),self.joueur)for j in range (10,40,10) for i in range (10,40,10)] + [Potion_de_soin((20,20),self.joueur),Potion_de_portee_permanente((2,2),self.joueur)]
                potions=potions_vue+potions_combat
                for potion in potions:
                    self.entitees.append(potion)
                #on place les indices
                positions = self.lab.petit_poucet(20)
                for position in positions:
                    self.entitees.append(Caillou(position))


            elif niveau == "tuto1":
                self.vitesse_monstres=20

                monstres=[]
                self.entitees=self.clees

                self.pnj = Pnj_passif((1,0),1000,(125,255,125),[Replique("Tu as déjà découvert comment te déplacer ? Essaies les touches directionnelles !",20),Replique("Tu devrais chercher la sortie de cette grotte. La porte au bout du couloir me semble suspecte.",20)])
                self.entitees.append(self.pnj)

            elif niveau == "tuto2":

                self.vitesse_montres=20

                monstres=[]
                self.entitees=self.clees

                self.pnj = Pnj_passif((2,3),1000,(190,255,56),[Replique("J'ai peur j'ai peur j'ai peur !J'ai peeeeuuurrr ! ! !",20),Replique("Cet endroit est horrible ! Jevoudrais remonter à la surface, mais avec ce labyrinthe je risque de me perdre, ce serait terrible !",20),Replique("Quelqu'un est passé avant, il a dit que la sortie était en bas à droite et qu'il avait laissé des cailloux sur le chemin, mais je n'ose pas y aller...",20),Replique("Je crois aussi qu'il a parlé de clées, je crois que tu dois les trouver pour ouvrir des portes",20),Replique("L'une d'elle est sur la case de coordonnées (19,1), mais je ne sais pas ce que ça veut dire",20)])
                self.entitees.append(self.pnj)

                positions = self.lab.petit_poucet(5,(0,0),self.clees[0].position)
                for position in positions:
                    self.entitees.append(Caillou(position))

                positions = self.lab.petit_poucet(5,self.clees[0].position,(14,16))
                for position in positions:
                    self.entitees.append(Caillou(position))

                positions = self.lab.petit_poucet(5,(14,16),self.clees[1].position)
                for position in positions:
                    self.entitees.append(Caillou(position))

                positions = self.lab.petit_poucet(5,self.clees[1].position,self.clees[2].position)
                for position in positions:
                    self.entitees.append(Caillou(position))

                positions = self.lab.petit_poucet(5,self.clees[2].position,self.clees[3].position)
                for position in positions:
                    self.entitees.append(Caillou(position))

                positions = self.lab.petit_poucet(5,self.clees[3].position)
                for position in positions:
                    self.entitees.append(Caillou(position))
                    
            elif niveau == "tuto3":

                self.vitesse_montres=20

                monstres=[Fatti([5,17]),Fatti([5,28]),Fatti([3,43]),Fatti([5,59])]
                self.entitees=self.clees

                self.pnj = Pnj_passif((5,3),1,(56,255,190),[Replique("Bonjour ! Fais très attention, il y des montres là-bas. Heureusement que je cours plus vite qu'eux !",20),Replique("C'est vraiment dommage, s'il n'y avait pas tous ces monstres, je serais sorti depuis longtemps. Mais j'ai beau être très intelligente et pouvoir trouver la sortie de tous ces labyrinthes en une fraction de seconde, je suis faible.",20),Replique("Tu peux essayer de tuer les monstres en les attaquant avec la touche espace, mais ne fait pas ça trop près de moi. C'est une attaque qui affecte tous les êtres vivants dans son périmètre.",20),Replique("Je peux voir tes armes ? Mais tu as une lance ! Tu peux utiliser les touches WASD pour attaquer dans la direction de ton choix. Cette attaque tape plus loin et plus fort que l'autre, mais dans une seule direction.",20),Replique("Tu peux essayer d'éviter les monstres en les coutournant, car ceux-ci ont une moins bonne vue que toi, mais je préférerais que tu les tues tous. Tu veux bien ?",20)])
                self.entitees.append(self.pnj)

                self.pnj = Pnj_passif((0,2),100,(0,255,125),[Replique("Qu'est-ce que tu fais là ? Personne ne vient jamais ici d'habitude ! Mais tu as raison. Il faut toujours explorer tout le labyrinthe, écouter toutes les répliques de tout le monde, ne rien négliger. C'est le seul moyen de gagner...",20)])
                self.entitees.append(self.pnj)
                
                positions = self.lab.petit_poucet(6,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif niveau == "tuto4":

                self.vitesse_montres=20

                monstres=[Slime([5,17]),Fatti([8,25]),Runner(self.lab.getMatrice_cases(),5,59,[3,48]),Fatti([5,59])]
                self.entitees=self.clees

                self.pnj = Pnj_passif((5,3),1,(56,255,190),[Replique("Eh bah, je suis contente d'avoir survécu.",20),Replique("Ici, les monstres sont différents. Tu devrais aller voir chaque salle puis revenir pour que je t'explique",20),Replique("Tu as vu le premier ? C'est un slime ! Il est presque aveugle, mais il se déplace et attaque très vite. Enfin, il ne te fais pas beaucoup de dégats et il meure vite aussi. Au fait, j'ai analysé ses mouvements et il semblerait qu'il se déplace totalement au hasard ! Ce n'est pas comme ça qu'on trouve quelques chose dans un labyrinthe...",20),Replique("Tu as vu le monstre suivant ? C'est le même qu'au niveau précédent, un fatti. Il est lent et ne bouge pas tant qu'il ne t'a pas repéré, mais évite de le laisser te taper, il fait très mal.",20),Replique("La salle suivante était vide ? Normal, elle était habitée par un runner. Il s'est précipité jusqu'à la sortie pour t'attendre.",20),Replique("Un fatti sur la sortie et un runner juste à côté, voilà un combo qui les rend très dangereux.",20)])
                self.entitees.append(self.pnj)

                positions = self.lab.petit_poucet(7,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif niveau == "tuto5":

                self.vitesse_montres=20

                meute1 = [Fatti([1,6],1),Fatti([2,13],1),Fatti([0,13],1),Fatti([1,14],1)]
                meute2 = [Slime([4,1],2),Slime([3,2],2),Slime([5,2],2),Slime([4,1],2),Slime([3,4],2),Slime([5,4],2),Slime([4,5],2),Slime([3,6],2),Slime([5,6],2),Slime([4,7],2),Slime([3,8],2),Slime([5,8],2),Slime([4,9],2)]
                meute3 = [Slime([7,9],3),Slime([8,10],3),Slime([6,10],3),Fatti([6,12],3),Fatti([7,12],3),Fatti([8,12],3)]
                meute4 = [Slime([10,6],4),Slime([10,7],4),Slime([10,8],4),Slime([10,9],4),Slime([10,10],4),Slime([10,11],4),Fatti([10,3],4,10,10,300,30)]
                meute5 = [Slime([13,9],5),Slime([14,10],5),Slime([12,10],5),Fatti([12,12],5),Fatti([13,12],5),Fatti([14,12],5),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[12,6]),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[13,1]),Runner(self.lab.getMatrice_cases(),self.CASES_X-1,self.CASES_Y-1,[14,6])]
                monstres = meute1
                for meutenumerote in [meute2,meute3,meute4,meute5]:
                    for monstre in meutenumerote:
                        monstres.append(monstre)

                self.pnj = Pnj_passif((2,2),1,(56,255,190),[Replique("Ces monstres ont l'air différents, c'est comme s'ils communiquaient ! Tu vois les trois qui n'étaient pas dans ton champ de vision au départ ? Ils ne te voyaient pas, donc ils n'auraient pas du pouvoir venir jusqu'ici. Mais l'autre qui te voyait leur a révélé ta position ! D'ailleurs, as-tu remarqué que tu ne peux ni te battre, ni te déplacer quand tu parles à quelqu'un ?",20)])
                self.entitees=[self.pnj]

                positions = self.lab.petit_poucet(8,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            elif niveau == "tuto6":

                self.vitesse_montres=20

                fattis=self.spawn_aleatoire(Fatti,10,10,200,20,20,1,((10,10),(30,30)),0.05,5,0,(0,0,100))
                slimes=self.spawn_aleatoire(Slime,5,5,50,3,6,1,((15,15),(25,25)),0.15,5,0,(255,100,100))

                potions_vue=[Potion_de_vision((35,26),self.joueur),Potion_de_vision((27,38),self.joueur),Potion_de_vision((21,19),self.joueur)]
                potions_combat=[Potion_de_force((i,j),self.joueur)for j in range(5,45,10) for i in range(5,45,10)] + [Potion_de_portee((i,j),self.joueur)for j in range (10,40,10) for i in range (10,40,10)]
                potions_bonus=[Potion_de_visibilite_permanente((8,23),self.joueur),Potion_de_visibilite_permanente((8,31),self.joueur),Potion_de_portee_permanente((23,37),self.joueur),Potion_de_portee_permanente((7,35),self.joueur),Potion_de_force_permanente((24,13),self.joueur),Potion_de_force_permanente((32,2),self.joueur),Potion_de_soin_permanente((39,0),self.joueur),Potion_de_soin_permanente((37,16),self.joueur),Potion_de_soin((20,20),self.joueur),Potion_de_soin((35,5),self.joueur),Potion_de_soin((5,35),self.joueur)]
                potions=potions_vue+potions_combat+potions_bonus

                self.pnj = Pnj_passif((3,4),250,(255,200,20),[Replique("Malheureux ! Jamais tu ne sortiras d'ici vivant ! Moi-même, qui ait atteint le plus haut niveau qu'un mage puisse atteindre, j'ai été forcé de fuir face au [insérer le nom du boss final ici] qui garde la sortie !",20),Replique("Mes potions me permettent d'annihiler tous les monstres sur mon passage, de voir au travers des murs de ces labyrinthes et même de les briser, mais elle n'ont pas suffit face au [insérer le nom du boss final ici].",20),Replique("Le plus terrible, c'est que j'ai perdu mes potions dans ma fuite, et qu'elles sont dispersées dans les labyrinthes. Si tu me les ramènes, je te donnerai beaucoup d'argent ! Hélas, je n'ai pas assez pour racheter les potions permanentes, ce sont de vrais trésors qui coutent une fortune. Si tu en trouve, tu peux les garder. D'ailleurs, gardes toutes les potions si ça peut te permettre d'éliminer le [insérer le nom du boss final ici] une bonne fois pour toute.",20)])
                self.entitees=potions+self.clees
                self.entitees.append(self.pnj)
                monstres = fattis + slimes

                positions = self.lab.petit_poucet(9,self.depart,self.arrivee)
                for position in positions:
                    self.entitees.append(Caillou(position))

            self.monstres = monstres

            self.entitees.append(self.joueur)

            if res :
                self.lab.resolution(self.arrivee[0],self.arrivee[1],self.depart[0],self.depart[1],"Largeur")

            for i in range(0,len(self.monstres)):
                self.entitees.append(self.monstres[i])

            #generation des meutes
            self.meutes=self.generation_meutes()

        else:
            self.entitees = entitees




        if evenements == None:
            self.evenements=[]
        else:
            self.evenements = evenements




        if horloge_cycle == None:
            self.horloge_cycle=0
        else:
            self.horloge_cycle = horloge_cycle




        pygame.display.set_caption("niveau " + str(niveau))
        self.screen = pygame.display.set_mode((FENETRE_X,FENETRE_Y),pygame.RESIZABLE)
        self.screen.fill((0,0,0))

        
        #objet qui traite les collisions
        self.collision=Collision()

        self.plus_lent=self.getPlusLent()
        #variable qui nous sert a exécuter les actions des entitées

        #objet d'affichage
        self.affichage=Affichage(self.screen,self.mode_affichage,self.LARGEUR_CASE,self.LARGEUR_MUR,self.lab.largeur,self.lab.hauteur)

        if niveau == "tuto1":
            self.affichage.affiche = DIALOGUE
            self.affichage.diag_cour = Replique("Tu va bien ? Quand je    t'ai vu tomber de là-hautj'ai cru que tu allais       mourir...            Bon, je te laisse te         reposer. N'hésite pas à revenir me parler avec  la touche x.",20)
            


        #texte de fin
        font = pygame.font.SysFont(None, 72)
        self.textWin = font.render("Vous avez gagné!! \(^o^)/", True, (128, 0, 0))
        self.textLose = font.render("Vous avez perdu!! ;o;", True, (0, 128, 128))
        
        self.position_screen=(0,0)

    def sauve(self):
        return [self.niveau,self.difficulte,self.mode_affichage,self.mode_minimap,self.lab.as_gagner(self.joueur.getPosition()) or self.as_perdu(),self.joueur,self.lab,self.entitees,self.evenements,self.horloge_cycle]



    def run(self):
        """
        Boucle principale du niveau
        Sorties:
            -le temps a attendre si le joueur as finit la niveau
            -un booléen indiquant si le joueur a gagné ou perdu
            -le joueur
        """
        run=True
        self.redraw()
        #objet qui permet de gérer le temps en pygame
        clock = pygame.time.Clock()
        
        while run:
            #on cadence à 60 frames/sec
            clock.tick(60)
            self.actualiser_temps()

            #si l'utilisateur décide de mettre fin au programme on sort de la boucle
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    res = -1
                    run=False

                if event.type == pygame.VIDEORESIZE:
                    self.zoom_largeur = event.w//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.zoom_hauteur = event.h//(self.LARGEUR_CASE + self.LARGEUR_MUR)
                    self.redraw()
                    
            self.actions_entitees()

            #si on détecte un mouvement on redessine l'écran
            #if move_j or move_m:
            self.redraw()
            self.traitement_evenements()

            if self.lab.as_gagner(self.joueur.getPosition()) and self.affichage.affiche == LABYRINTHE:
                self.screen = pygame.display.set_mode((640, 300))
                self.ecran_fin_niveau(self.textWin)
                res = 1000
                run=False
            if self.as_perdu():
                self.screen = pygame.display.set_mode((640, 300))
                self.ecran_fin_niveau(self.textLose)
                res = 1000
                run=False
            pygame.display.update()
        self.fin_niveau()
        return res,self.lab.as_gagner(self.joueur.getPosition()),self.joueur

    def fin_niveau(self):
        """
        Fonction qui gère la fin du niveau
        """
        #on met fin a tout les événements
        for evenement in self.evenements:
            evenement.temps_restant=0
            evenement.action()
    def generation_meutes(self):
        """
        Fonction qui génère les meutes
        Sorties:
            -les meutes
        """
        meutes=[]
        id_meutes=[0]
        for monstre in self.monstres:
            if not(monstre.id_meute in id_meutes):
                #on génère une nouvelle meute
                nb_monstres=0
                id_meute=monstre.id_meute
                for monstre in self.monstres:
                    if monstre.id_meute==id_meute:
                        nb_monstres+=1
                id_meutes.append(id_meute)
                #on récupère les données de la vue de la meute
                vues,positions=self.recuperer_vues_meute(id_meute)
                
                meutes.append(Meute(self.CASES_X,self.CASES_Y,id_meute,nb_monstres,vues,positions))
        return meutes
                
    def actualiser_temps(self):
        """
        Fonction qui actualise la variable permettant de mesurer le temps pour
        les entitées
        """
        #on vérifie qu'on n'est pas a la fin d'un cycle
        if self.horloge_cycle<self.plus_lent+1:
            self.horloge_cycle+=1
        else:
            self.horloge_cycle=1
            
    
    def traitement_evenements(self):
        """
        Fonction qui traite les événements
        """
        events_tmps=[self.evenements[i] for i in range(0,len(self.evenements))]
        nbSup=0
        
        for i in range(0,len(events_tmps)):
            #print (events_tmps)
            if events_tmps[i].execute():
                self.evenements.pop(i-nbSup)
                nbSup+=1
                
                 
    def action_joueur(self):
        """
        Fonction qui exécute la partie du code ou le jpueur demande à agir
        et qui renvoie rien
        """
                    


        #on récupère toutes les touches préssés sous forme de booléen
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.affichage.affiche = MINIMAP
            self.joueur.vitesse = self.joueur.vitesse_autres
        elif keys[pygame.K_i]:
            self.affichage.affiche = INVENTAIRE
            self.joueur.vitesse = self.joueur.vitesse_autres
        elif keys[pygame.K_RETURN] and (self.affichage.affiche == INVENTAIRE or self.affichage.affiche == MINIMAP):
            self.affichage.affiche = LABYRINTHE
            self.joueur.vitesse = self.joueur.vitesse_lab

        if self.affichage.affiche == INVENTAIRE:
            if keys[pygame.K_RIGHT]:
                self.joueur.inventaire_vers_la_droite()
            elif keys[pygame.K_LEFT]:
                self.joueur.inventaire_vers_la_gauche()
            elif keys[pygame.K_SPACE]:
                self.joueur.utilise_inventaire()
            elif keys[pygame.K_EQUALS]:
                self.affichage.affiche = ITEM

        if self.affichage.affiche == ITEM:
            if keys[pygame.K_MINUS]:
                self.affichage.affiche = INVENTAIRE

        elif self.affichage.affiche == MINIMAP:
            if keys[pygame.K_UP]:
                self.joueur.minimap.va_vers_le_haut()
            elif keys[pygame.K_DOWN]:
                self.joueur.minimap.va_vers_le_bas()
            elif keys[pygame.K_RIGHT]:
                self.joueur.minimap.va_vers_la_droite()
            elif keys[pygame.K_LEFT]:
                self.joueur.minimap.va_vers_la_gauche()
            elif keys[pygame.K_EQUALS]:
                self.joueur.minimap.rezoom()
            elif keys[pygame.K_MINUS]:
                self.joueur.minimap.dezoom()

        elif self.affichage.affiche == LABYRINTHE:
            if keys[pygame.K_UP]:
                self.joueur.va_vers_le_haut()
            elif keys[pygame.K_DOWN]:
                self.joueur.va_vers_le_bas()
            elif keys[pygame.K_RIGHT]:
                self.joueur.va_vers_la_droite()
            elif keys[pygame.K_LEFT]:
                self.joueur.va_vers_la_gauche()
            elif keys[pygame.K_SPACE]:
                self.joueur.attaque()
            elif keys[pygame.K_x]:
                self.joueur.tentative_interaction()

        elif self.affichage.affiche == DIALOGUE:
            self.joueur.vitesse = self.joueur.vitesse_autres
            if keys[pygame.K_RETURN]:
                self.affichage.pass_replique()
                self.joueur.vitesse = self.joueur.vitesse_lab


    def actions_entitees(self):
        """
        Fonction qui exécute les actions des entitées
        renvoie un booléen indiquant si il y a besoin de redessiner l'écran
        """
        redessiner=False

        agissants=self.getAgissants()
        
        self.actualiser_vues_agissants(agissants)
        
        for agissant in agissants:
            if self.horloge_cycle % agissant.getVitesse()==0:
                if issubclass(type(agissant),Joueur):
                    self.action_joueur()

                agissant.soigne_toi()
                
                agissant=self.actualiser_donnee(agissant)

                agissant.prochaine_action()

                agissant.execute_evenements()
                if redessiner:
                    self.traitement_action(agissant)
                else:
                    redessiner=self.traitement_action(agissant)

        self.delete_entitees()
        
        return redessiner
    def getAgissants(self):
        """
        Fonction qui renvoie un tableau contenant les agissants
        """
        agissants=[]
        
        for entitee in self.entitees:
            if issubclass(type(entitee),Agissant):
                agissants.append(entitee)

        return agissants
    def delete_entitees(self):
        """
        Fonction qui supprime les entitees mortes
        """
        nbSupp=0
        for i in range(0,len(self.entitees)):
            if issubclass(type(self.entitees[i-nbSupp]),Agissant):
                if self.entitees[i-nbSupp].pv<=0:
                    self.entitees.pop(i-nbSupp)
                    nbSupp+=1
            elif issubclass(type(self.entitees[i-nbSupp]),Item) or issubclass(type(self.entitees[i-nbSupp]),Potion):
                if self.entitees[i-nbSupp].position==None:
                    self.entitees.pop(i-nbSupp)
                    nbSupp+=1
        
    def actualiser_vues_agissants(self,agissants):
        """
        Fonction qui actualise la vue de touts les agissants (meutes inclues)
        Entrée:
            -les agissants
        """
        for agissant in agissants:
            #l'id 0 indique que l'entitée n'appartient a aucune meute
            if not(issubclass(type(agissant),Monstre)) or agissant.id_meute==0:
                #on actualise la vue de l'entitée seule
                vue_entitee,position_vue=self.actualiser_vue(agissant.getPosition(),agissant.getLargeurVue(),agissant.getHauteurVue())
                agissant.actualiser_vue(vue_entitee,position_vue)

        id_meutes=[0]
        for agissant in agissants:
            #on vérifie si on n'as pas déja executée la meute de l'entitée
            if issubclass(type(agissant),Monstre) and not(agissant.id_meute in id_meutes):
                id_meutes.append(agissant.id_meute)
                #on récupère les données de la vue de la meute
                vues,positions=self.recuperer_vues_meute(agissant.id_meute)
                #on obtient la meute du monstre
                meute=self.getMeute(agissant.id_meute)
                #on crée la vue de la meute
                vue_meute=meute.actualisation_vues(vues,positions)
                
                #on actualise les vues des monstres de la meute
                for agissant_bis in agissants:
                    if issubclass(type(agissant_bis),Monstre):
                        if agissant_bis.id_meute==agissant.id_meute:
                            agissant_bis.actualiser_vue(vue_meute,[0,0])

    def getMeute(self,id_meute):
        """
        Fonction qui renvoie la meute correspondant a l'identifiant entrer
        Entrée:
            -l'identifiant de la meute
        Sortie:
            -la meute qui correspond a l'indentifiant
        """
        meute=None
        for meute_tmp in self.meutes:
            if meute_tmp.id_meute==id_meute:
                meute=meute_tmp
        return meute

    def recuperer_vues_meute(self,identifiant):
        """
        Fonction qui doit renvoyer les vues nécessaires a une meute
        Entrées:
            -l'identifiant de la meute
        Sorties:
            -les vues des monstres
            -les positions des vues
        """
        vues=[]
        positions=[]
        for entitee_bis in self.entitees:
            if issubclass(type(entitee_bis),Monstre) and entitee_bis.id_meute==identifiant:
                vue_entitee,position_vue=self.actualiser_vue(entitee_bis.getPosition(),entitee_bis.getLargeurVue(),entitee_bis.getHauteurVue())
                vues.append(vue_entitee)
                positions.append(position_vue)

        return vues,positions
    
    def actualiser_vue(self,position,largeur_vue,hauteur_vue):
        """
        Fonction qui construit la vue d'un agissant
        Entrée:
            -la position de la vue de l'agissant
            -la largeur de la vue de l'agissant
            -la hauteur de la vue de l'agissant
        Sortie:
            -la vue de l'agissant
            -la position de la vue de l'agissant
        """
        vue_agissant,position_vue=self.lab.construire_vue(position,largeur_vue,hauteur_vue)

        return vue_agissant,position_vue
    def actualiser_donnee(self,agissant):
        """
        Fonction qui actualise les données des agissant en fonction de leur
        type
        Entrée:
            un agissant
        Sortie:
            un agissant avec ces données actualisées
        """
        if issubclass(type(agissant),Monstre):
            #on donne la position du joueur au monstre
            agissant.setPosition_joueur(self.joueur.getPosition())
            
        return agissant
    def traitement_action(self,agissant):
        """
        Fonction qui traite une action donnée d'un agissant
        et qui renvoie un booléen indiquant si l'action à été exécutée
        """
        succes=False
        
        id_action,action=agissant.get_action()

        #print(type(agissant),id_action,action)
        
        if id_action==BOUGER:
            #print("veut bouger")
            direction_voulue=action
            if direction_voulue!=None:
                if issubclass(type(agissant),Joueur):
                    passe,newcoord,tel=self.lab.peut_passer(agissant.getPosition(),direction_voulue,agissant.inventaire)
                else:
                    passe,newcoord,tel=self.lab.peut_passer(agissant.getPosition(),direction_voulue)
                #print(passe)
                if passe:
                    libre = self.collision.case_libre(agissant,newcoord,self.entitees)
                    #print(libre)
                    if libre:
                        succes=True
                        #print(succes)
                        agissant.setPosition(newcoord)
                        if agissant == self.joueur:
                            nouveaux_evenements = self.collision.visite_case(newcoord,agissant,self.entitees)
                            self.lab.matrice_cases[newcoord[0]][newcoord[1]].passage = True
                            for evenement in nouveaux_evenements :
                                self.evenements.append(evenement)
                            if tel != None:
                                if tel[0] == self.niveau:
                                    agissant.setPosition(tel[1])
                                
        elif id_action==ATTAQUER:
            self.affichage.ajout_animation(agissant.getPosition(),0,3,agissant.getRadius()*(self.LARGEUR_CASE+self.LARGEUR_MUR))
            succes=self.collision.tentative_attaque(agissant,self.entitees)
        elif id_action==INTERAGIR:
            succes = self.collision.tentative_interaction(agissant,self.entitees)
        elif id_action==PARLER:
            succes = self.affichage.add_dialogue(action)
        return succes
    def getPlusLent(self):
        """
        Fonction qui permet d'obtenir la plus grande vitesse
        Sorties:
            -la vitesse de l'agissants le plus lent
        """
        agissants=self.getAgissants()
        vitesses=[]
        for agissant in agissants:
            vitesses.append(agissant.getVitesse())
            if issubclass(type(agissant),Joueur):
                vitesses.append(agissant.vitesse_autres)
        return self.ppcm(vitesses)
    def as_perdu(self):
        """
        Fonction qui vérifie si le joueur as perdu(pv=0 ou soft lock)
        """
        return (self.joueur.pv<=0)
    def ecran_fin_niveau(self,text):
        """
        Fonction qui as pour but d'afficher l'écran de fin de niveau (stats etc)
        """
        self.screen.fill((255,255,255))
        self.screen.blit(text,(0,0))
    def redraw(self):
        """
        Fonction qui redessine l'entièreté de l'écran
        """
        self.affichage.dessine_frame(self.joueur,self.lab,self.entitees,self.evenements)

    def spawn_aleatoire(self,monstre,largeur_vue,hauteur_vue,pv,degats,vitesse,radius,perimetre,proba,max_meute,premiere_meute,couleur=(255,0,0)):
        """
        Fonction qui génére des monstres aléatoirement
        Entrées :
            caractéristiques des monstres à spawner (type de monstre, vue, stats)
            zone où les monstres seront spawnés
            probabilité de spawn par case
            quelques détails pour les meutes (numéro de la première meute libre et nombre maximum de monstre par meute)
        Sorties :
            Un tableau avec les monstres demandés
        """
        nb_meute = premiere_meute
        taille_meute = 0
        res = []
        for i in range (perimetre[0][0],perimetre[1][0]):
            for j in range (perimetre[0][1],perimetre[1][1]):
                if random.random() <= proba :
                    res.append(monstre((i,j),nb_meute,largeur_vue,hauteur_vue,pv,degats,vitesse,radius,couleur))
                    taille_meute += 1
                    if taille_meute == max_meute :
                        nb_meute += 1
                        taille_meute = 0
        return res

    def ppcm(self,vitesses):
        """Calcul du 'Plus Petit Commun Multiple' des vitesses"""
        def _pgcd(a,b):
            while b != 0:
                a,b = b,a%b
            return a
        if len(vitesses) == 1:
            res = vitesses[0]
        else:
            res = (vitesses[0]*vitesses[1])//_pgcd(vitesses[0], vitesses[1])
            for x in vitesses[2:]:
                res = (res*x)//_pgcd(res, x)
        return res

    def __str__(self):
        return "Niveau("+str(self.niveau)+","+str(self.difficulte)+","+str(self.mode_affichage)+","+str(self.mode_minimap)+","+str(self.joueur)+")"
