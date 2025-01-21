# -*- coding: utf-8 -*-
import var as var

def init_coeur():
    global coeur1
    global coeur2
    global coeur3
    global coeur4
    coeur1 = loadImage("src/Coeur1.png")
    coeur2 = loadImage("src/Coeur2.png")
    coeur3 = loadImage("src/Coeur3.png")
    coeur4 = loadImage("src/Coeur4.png")
    
def affichage():
    textSize(32)
    fill("#fffff")
    text("Score : " + str(var.score), 320, 29)
    fill("#FF0000")
    text("Fin", 300, 400)
def affichage_fin() :
    if var.vie <= 0 :
        textSize(75)
        fill("#FF0000")
        text("Vous etes mort ", 120, 200)
        textSize(32)
        fill("#FF0000")
        text("T'es trop nul ", 120, 250)
        textSize(32)
        fill("#FF0000")
        text("votre score est de : " + str(var.score), 120, 300)
        textSize(20)
        fill("#000000")
        text("Appuyez sur Entrer pour recommencer ", 120, 350)
def affichage_vie ():
    if var.vie == 4 :
        image(coeur4, 30, 30)
    elif var.vie == 3 :
        image(coeur3, 30, 30)
    elif var.vie == 2 :
        image(coeur2, 30, 30)
    elif var.vie == 1 :
        image(coeur1, 30, 30)
        
    
    

def win():
    textSize(75)
    fill("#FF0000")
    text("Vous avez gagne ", 120, 200)
    textSize(32)
    fill("#FF0000")
    text("Tu es le GOAT ", 120, 250)
    textSize(32)
    fill("#FF0000")
    text("votre score est de : " + str(var.score), 120, 300)
    textSize(20)
    fill("#000000")
    text("Appuyez sur Entrer pour recommencer ", 120, 350)

def affichage_power():
    textSize(65)
    fill("#FF0000")
    text(var.name_power, 290, 150)

        
