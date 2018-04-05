﻿import pygame
from pygame.locals import*
from random import *
import time
pygame.init()
fenetre=pygame.display.set_mode((800,600))


class menu():
    def __init__(self):
        self.menu_=0
        
class sac():
    def __init__(self,q):
        self.quantite=q
        
    
class perso(pygame.sprite.Sprite):
    def __init__(self, imageperso,imageperso2):
        self.image = pygame.image.load(imageperso).convert_alpha()
        self.image2 = pygame.image.load(imageperso2).convert_alpha()
        self.rect = self.image.get_rect()
        self.size=self.image.get_size()
        self.alive=True
        self.niveau=1
        self.xp=0
        self.difficulteniveau=self.niveau/0.75*100
        self.ptdecompetance=0
        self.ptforce=0
        self.ptvie=0
        self.bonus=0
        if self.xp==self.difficulteniveau:
            self.xp=0
            self.niveau+=1
            

class perso1(perso):
    def __init__(self):
        perso.__init__(self, "Perso1nship0.png", "Perso1nship1.png")
        self.vie=150
        self.mana=100
        self.fleche=0
        self.armure=0
        self.ptmana=0
        self.bonusmagique=0
        self.sortdefeu=False

class perso2(perso):
    def __init__(self):
        perso.__init__(self, "perso2base0.png", "perso2base1.png")
        self.vie=200
        self.taunt=0
        self.armure=10

class perso3(perso):
    def __init__(self):
        perso.__init__(self, "perso3armurebase.png", "perso3armurebase2.png")
        self.vie=100
        self.active=False
        self.poison=False

class ennemi(pygame.sprite.Sprite):
    def __init__(self, imageperso):
        self.image = pygame.image.load(imageperso).convert_alpha()
        self.rect = self.image.get_rect()
        self.size=self.image.get_size()
        self.alive=False

class ennemi1(ennemi):
    def __init__(self):
        ennemi.__init__(self,"cerberus.png")
        self.vie=250


perso_joueur=perso1()
david=perso2()
sinatra=perso3()
loup=ennemi1()
base=menu()
objet=menu()
attaque=menu()
enemitipe=ennemi("cerberus.png")
soin=sac(1)
resurection=sac(1)

