# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

def init_ligne():
    global img_ligne
    img_ligne = loadImage("src/Ligne.png")
    
def afficher_ligne() :
    tint(255, 128)
    image(img_ligne, 260, 200, 1000, 1000)
    tint(255, 255)
