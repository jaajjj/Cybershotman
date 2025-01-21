# -*- coding: utf-8 -*-
from random import randint
import var as var


def init_monstre():
    global img_monstre
    
    img_monstre = loadImage("src/Monstre.png")
    
def creer_monstre():
    if (int(var.depart/var.frame) == var.depart/var.frame) and len(var.tab_monstre)<=var.limit_monstre:
         var.tab_monstre.append([770, randint(60, 335)])

def afficher_monstre():
    for monstre in var.tab_monstre :
        image(img_monstre, monstre[0], monstre[1])
        
def deplacer_monstre():
    for coord in var.tab_monstre :
        coord[0] -= 3
        if (coord[0] < -10): 
            var.tab_monstre.remove(coord)
            var.vie -= 1
    
def monstre_acceleration():
    if int(var.depart/900) == var.depart/900 : 
            if var.frame!=1 :
                var.frame -= 1
    if int(var.depart/1600) == var.depart/1600 : 
        var.limit_monstre += 1
        
    
def tuer_monstre ():
    for monstre in var.tab_monstre:
        for bullet in var.tab_bullet :
            if bullet[0] >= int(monstre[0])-56 and bullet[0] <= int(monstre[0])+56 and bullet[1] >= int(monstre[1])-10 and bullet[1] <= int(monstre[1])+65 : 
                try:
                    var.tab_monstre.remove(monstre)
                except:
                    print("bug")
                var.score += 10
                if not var.percing  :
                    try:
                        var.tab_bullet.remove(bullet)
                    except:
                        print("bug")
def tuer_perso():
    for monstre in var.tab_monstre :
        if monstre[1] >= int(var.coords_perso[1])-40 and monstre[1] <= int(var.coords_perso[1])+40 and monstre[0] >= int(var.coords_perso[0])-10 and monstre[0] <= int(var.coords_perso[0])+10 :
            var.vie -= 1
            var.tab_monstre.remove(monstre)

    
