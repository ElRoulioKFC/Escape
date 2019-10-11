from Cases import *
from Resolveur import *
from math import sqrt

class Monstre:
    def __init__(self,position,largeur_vue,hauteur_vue,couleur=(255,0,0)):
        self.position=position
        self.largeur_vue=largeur_vue
        self.hauteur_vue=hauteur_vue
        self.couleur=couleur
        
    def joueur_en_vue(self,position_lab,vue,position_joueur):
        """
        Fonction qui renvoie un booléen qui nous dit si le joueur est en visible par le monstre
        Entrées:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
            la position du joueur dans le labrinthe
        Sorties:
            booléen indiquant si le joueur est visible
        
        """
        visible=False

        min_x=position_lab[0]
        min_y=position_lab[1]
        
        max_x=min_x+len(vue)
        max_y=min_y+len(vue[0])

        if position_joueur[0]>=min_x and position_joueur[0]<max_x and position_joueur[1]>=min_y and position_joueur[1]<max_y:
            visible=True
            
        return visible
    
    def joueur_accesible(self,position_lab,vue,position_joueur):
        """
        Fonction qui renvoie un booléen qui nous dit si le joueur est en accesible par le monstre
        Entrées:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
            la position du joueur dans le labrinthe
        Sorties:
            booléen indiquant si le joueur est accesible
        """
        accesible=False

        if self.joueur_en_vue(position_lab,vue,position_joueur):
            solution= Resolveur(vue,len(vue),len(vue[0]),position_joueur[0]-position_lab[0],position_joueur[1]-position_lab[1],self.position[0]-position_lab[0],self.position[1]-position_lab[1])
            accesible=solution.resolution(False,False)

        return accesible

    def decision(self,position_lab,vue,position_joueur):
        """
        Fonction qui choisis quel comportement le monstre va appliquer
        Entrées:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
            la position du joueur dans le labrinthe
        Sorties:
            La direction de la prochaine position voulue par le monstre
        """
        prochaine_position=[]

        prochaine_direction=None
        
        if self.joueur_accesible(position_lab,vue,position_joueur):
            prochaine_direction=self.rush(position_lab,vue,position_joueur)
        else:
            prochaine_direction=self.cherche(vue,position_lab)

        return prochaine_direction
    
    def cherche(self,vue,position_lab):
        """
        Fonction à surdéfinir dans la classe fille (réécrire ce qu'il y a a l'intérieur)
        Elle prend en entrée:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
        Elle renvoie:
            la direction de la prochaine position voulue par le monstre
        """
        print("Objet non défini un monstre est un type pas une entitée!!")

    def rush(self,position_lab,vue,position_joueur):
        """
        Fonction qui définie le comportement lorsque le monstre a vue le joueur
        Elle prend en entrée:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
            la position du joueur dans le labrinthe
        Sorties:
            la direction de la prochaine position voulue
        """
        direction_voulue=None
        #on initialise le résolveut pour qu'il nous trouve la prochaine position
        resolveur= Resolveur(vue,len(vue),len(vue[0]),position_joueur[0]-position_lab[0],position_joueur[1]-position_lab[1],self.position[0]-position_lab[0],self.position[1]-position_lab[1],"Largeur")
        chemin=resolveur.resolution(True,False)
        
        #on renvoie la prochaine action a effectuer
        position_suivante=None
        if chemin!=None:
            if len(chemin)>2:
                position_suivante=chemin[1]
                direction_voulue=self.direction_suivante(chemin[0],chemin[1])
                
        return direction_voulue

    def direction_suivante(self,position_actuelle,position_voulue):
        """
        Fonction qui prend en entrée:
            la position du monstre
            la prochaine position voulue du monstre
        Sortie:
            la direction que le monstre veut prendre
        """
        direction=None

        if position_actuelle[1]>position_voulue[1]:
            direction=HAUT
        elif position_actuelle[0]<position_voulue[0]:
            direction=DROITE
        elif position_actuelle[1]<position_voulue[1]:
            direction=BAS
        else:
            direction=GAUCHE

        
        return direction

    def directions_utilisables(self,position_x,position_y,vue):
        """
        Fonction qui prend en entrées:
            la position du monstre
            la vue disponible au monstre
        et qui renvoie les directions ou le monstre peut passer
        """
        directions_utilisables=[]

        voisins,positions_voisins=self.voisins_monstre(position_x,position_y,vue)

        for i in range(0,len(voisins)):
            if voisins[i]!=None:
                voisin_x=positions_voisins[i][0]
                voisin_y=positions_voisins[i][1]

                #on vérifie si l'on peut passer
                if not(vue[position_x][position_y].mur_plein(i)):
                    directions_utilisables.append(i)
        return directions_utilisables

    def voisins_monstre(self,x,y,vue):
        """
        Fonction qui prend en entrée:
            les coordonnées du monstre
            la vue disponible au monstre
        et qui renvoie les voisins du monstre
        ainsi que leurs coordonnées
        """
        voisins=[]
        positions_voisins=[]
        #on élimine les voisins aux extrémitées
        if y-1>=0:
            voisins.append(vue[x][y-1])
            positions_voisins.append([x,y-1])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        if x+1<self.largeur_vue:
            voisins.append(vue[x+1][y])
            positions_voisins.append([x+1,y])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        if y+1<self.hauteur_vue:
            voisins.append(vue[x][y+1])
            positions_voisins.append([x,y+1])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        if x-1>=0:
            voisins.append(vue[x-1][y])
            positions_voisins.append([x-1,y])
        else:
            voisins.append(None)
            positions_voisins.append(None)
            
        return voisins,positions_voisins
    
    def dessine_toi(self,screen,decalage,LARGEUR_CASE,LARGEUR_MUR,position_screen):
        pygame.draw.rect(screen, self.couleur,(decalage[0]*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1],decalage[1]*(LARGEUR_CASE+LARGEUR_MUR)+LARGEUR_MUR+position_screen[1],LARGEUR_CASE-2*LARGEUR_MUR,LARGEUR_CASE-2*LARGEUR_MUR))

    
    def setPosition(self,position):
        self.position=position
    def getPosition(self):
        return self.position
    def setCouleur(self,couleur):
        self.couleur=couleur
    def getLargeurVue(self):
        return self.largeur_vue
    def getHauteurVue(self):
        return self.hauteur_vue


class Slime(Monstre):
    def cherche(self,vue,position_lab):
        """
        But: simuler le comportement du slime qui se déplace de manière aléatoire
        Elle prend en entrée:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
        Elle renvoie:
            la direction de la prochaine position voulue par le monstre
        """
        directions=self.directions_utilisables(self.position[0],self.position[1],vue)
        
        return directions[random.randrange(0,len(directions))]


class Fatti(Monstre):
    def cherche(self,vue,position_lab):
        """
        But:Simuler le comportement de Fatti qui ne se déplace que si il peut atteindre le joueur
        Elle prend en entrée:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
        Elle renvoie:
            la direction de la prochaine position voulue par le monstre
        """
        
        return None

class Runner(Monstre):
    def __init__(self,position,largeur_vue,hauteur_vue,fin_lab_x,fin_lab_y,couleur=(255,0,0)):
        self.position=position
        self.largeur_vue=largeur_vue
        self.hauteur_vue=hauteur_vue
        self.couleur=couleur
        self.fin_lab=[fin_lab_x,fin_lab_y]
    def cherche(self,vue,position_lab):
        """
        But:Simuler le comportement de Runner qui va vers la fin du labyrinthe
        Elle prend en entrée:
            la position de la vue dans le labyrinthe
            une matrices de cases correspondant à la vue du monstre
        Elle renvoie:
            la direction de la prochaine position voulue par le monstre
        """
        direction_voulue=None
        
        #on initialise le résolveut pour qu'il nous trouve la prochaine position
        resolveur= Resolveur(vue,len(vue),len(vue[0]),self.fin_lab[0],self.fin_lab[1],self.position[0]-position_lab[0],self.position[1]-position_lab[1],"Largeur")
        chemin=resolveur.resolution(True,False)
        
        #on renvoie la prochaine action a effectuer
        position_suivante=None
        if chemin!=None and chemin!=False:
            if len(chemin)>2:
                position_suivante=chemin[1]
                direction_voulue=self.direction_suivante(chemin[0],chemin[1])
        
        return direction_voulue
    
        
