# -*- coding: utf-8 -*-
import var as var

def init_perso():
    global img_perso
    img_perso = loadImage("src/Perso.png")
    
def afficher_perso():
    image(img_perso,var.coords_perso[0], var.coords_perso[1])
    
def reset_power():
    var.base_speed = 4
    var.bullet_speed = 6
    var.percing = False
    var.power_bullet = False
    var.back=True
    var.in_power_use=False
    var.affichage_power=False
    var.name_power = ""
    var.temps_power=0.0
    var.affichage_verif= False
    var.avance=False
def deplacer() :
    if var.up and var.coords_perso[1] <= 335:
        var.coords_perso[1] += var.base_speed
    if var.down and var.coords_perso[1] >= 60 :
        var.coords_perso[1] -= var.base_speed
def fin_jeu() :
    if var.vie == 0 :
        var.game = False
        
def reset_jeu() : 
    if var.touche :
        var.touche=False
        var.temps_power=0.0
        var.coords_perso=[50,200]
        var.game = True
        var.depart=0.0
        var.base_speed= 5
        var.bullet_speed = 6
        var.monstre_speed = 3
        var.percing=False
        var.power_bullet = False
        var.up = False
        var.down = False
        var.tab_monstre=[]
        var.tab_bullet=[]
        var.tab_power=[]
        var.vie = 4
        var.frame=30
        var.score = 0
        var.win = False
        var.name_power=""

def win_jeu():
    if var.coords_perso[0] >= 250 :
        var.win=True
