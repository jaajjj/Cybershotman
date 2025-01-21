from Perso import *
from Bullet import *
from Monstre import *
from Power import *
from Texte import *
from Ligne import *
import var as var

def setup():
    size (800, 400) # définition de la taille de la fenêtre de l'application
    imageMode(CENTER) # on affichera les images en précisant les coords du centre
    var.fond=loadImage("src/fond.png")
    init_perso()
    init_bullet()
    init_monstre()
    init_power()
    init_ligne()
    init_coeur()

    

def draw():
    if var.back == True :
        background(200)
        image(var.fond, 400, 200)
    if var.vie > 0 and var.win == False :
        affichage()
        afficher_ligne()

        if (int(var.temps_power)/60) % 2 == 0 :
            affichage_power()
        var.depart += 1
        if var.in_power_use  :
            var.temps_power += 1
        afficher_perso()
        affichage_vie ()
        deplacer()
        afficher_bullet()
        deplacer_bullets()
        afficher_monstre()
        afficher_power()
        creer_monstre()
        creer_power()
        deplacer_monstre()
        tuer_monstre()
        monstre_acceleration()
        deplacer_power()
        prendre_power()
        avancee_power()
        tuer_perso()
        if int(var.temps_power/360) == 1  :
            reset_power()
        win_jeu()
    
    if var.win == True :
        win()
        reset_jeu()
        fin_jeu()
        
    if var.vie == 0  :
        background(200)
        affichage_fin()
        reset_jeu()
        fin_jeu()
    
    
    
def keyPressed():
    if (keyCode == UP ): var.down = True
    if (keyCode == DOWN ): var.up = True
    if (key == " ") and not var.power_bullet: tirer(var.coords_perso[:])
    if (key == ENTER): var.touche = True
        
def keyReleased():
    if (keyCode == UP ): var.down = False
    if (keyCode == DOWN ): var.up = False
    

    
