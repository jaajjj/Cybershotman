# -*- coding: utf-8 -*-
import var as var

def init_bullet():
    global img_bullet
    img_bullet = loadImage("src/Lazer.png")
    
def afficher_bullet():
    for coords in var.tab_bullet :
        image(img_bullet,coords[0]+48,coords[1]-33)
        
def tirer(coords_bullet):
    if not len(var.tab_bullet) == 5 or var.power_bullet==True :
        var.tab_bullet.append(coords_bullet)
        
def deplacer_bullets():
    for bullet in var.tab_bullet :
        bullet[0] += var.bullet_speed 
        if bullet[0] >= 817 :
            var.tab_bullet.remove(bullet)
    if (int(var.depart/15) == var.depart/15) and var.power_bullet == True :
         var.tab_bullet.append(var.coords_perso[:])
    
    
                
    
