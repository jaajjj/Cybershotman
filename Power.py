# -*- coding: utf-8 -*-
from random import randint
import var as var

def init_power():
    global img_power
    img_power = loadImage("src/Power.png")
    
def creer_power():
    if (int(var.depart/600) == var.depart/600 and len(var.tab_power)==0) :
        var.tab_power.append([770, randint(60, 335)])
        
def afficher_power():
    for elm in var.tab_power :
        image(img_power,elm[0],elm[1])
        
def prendre_power ():
    random_var=randint(0,4)
    for power in var.tab_power :
        if power[1] >= int(var.coords_perso[1])-51 and power[1] <= int(var.coords_perso[1])+51 and power[0] >= int(var.coords_perso[0])-10 and power[0] <= int(var.coords_perso[0])+10 : 
            var.tab_power.remove(power)
            var.in_power_use=True
            var.score += 30
            var.affichage_power = True
            if random_var == 0 : 
                var.name_power="SPEED"
                var.base_speed += 4
                var.bullet_speed += 4
            if random_var == 1 : 
                var.name_power="TRANSPERCANT"
                var.percing = True
            if random_var == 2 : 
                var.name_power="MACHINE GUN"
                var.power_bullet = True
            if random_var == 3 :  
                var.name_power="AVANCEE"
                var.avance=True

            if random_var == 4 : 
                var.name_power=""
                var.name_power="MALADE"
                var.back=False
def avancee_power () :
    if (int(var.temps_power/60) == var.temps_power/60) and var.avance==True :
        var.coords_perso[0] += 5
                
def deplacer_power():
    for power in var.tab_power :
        power[0] -= 5
        if (power[0] < -10): var.tab_power.remove(power)
    
