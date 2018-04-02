#Imported Modules
import pygame
from math import pi, sin, cos
from time import ctime
from winsound import Beep
from random import randint

#Imported Files
from Note import Note
import sheetMusic

elegant = "Vivaldi"
simple = "Arial Rounded MT Bold"
text = ""

#Keys
keys = {"E3": "Z", "F3": "X", "G3": "C", "A3": "V", "B3": "B", "C4": "N", "D4": "M", "E4": ",",
        "F4" : ".",  "G4": "A", "A4": "S", "B4" : "D",  "C5": "F", "D5": "G", "E5": "H", "F5": "J", "G5": "K",
        "A5": "L", "B5": "Q", "C6": "W", "D6": "E", "E6": "R", "F6": "T", "  ": "-"}
    
musicList = []

class Song(object):
    
    def __init__(self, name, music, tempo):
        self.name = name
        self.sheetMusic = music
        self.tempo = tempo
        musicList.append(self)
        
    def displaySheet(self):
        """Displays input sheet music on screen, along with the title"""
        musicSheet = self.sheetMusic
        for key in keys:
            musicSheet = musicSheet.replace(key, keys[key] + " ")
        for line in range(len(musicSheet.split("\n"))):
            screen.blit(font.render(self.name, True,  (0, 0, 0)), [0, 0])
            screen.blit(font.render(musicSheet.split("\n")[line], True, (0, 0, 0)), [0, 20*line])

FunkyTown = Song("Funky Town", sheetMusic.funkyTown, 250)
FurElise = Song("Für Elise", sheetMusic.furElise, 333)
TakeOnMe = Song("Take On Me", sheetMusic.takeOnMe, 250)
JingleBells = Song("Jingle Bells", sheetMusic.jingleBells, 250)
LostWoods = Song("Lost Woods", sheetMusic.lostWoods, 250)
ImBlue = Song("I'm Blue", sheetMusic.imBlue, 254)
AveMaria = Song("Ave Maria", sheetMusic.aveMaria, 240)
AllStar = Song("All Star", sheetMusic.allStar, 250)
TwinkleTwinkle = Song("Twinkle Twinkle", sheetMusic.twinkleTwinkle, 250)

musicIndex = 0

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Piano")
done=False
clock = pygame.time.Clock()

while(not done):
    font =  pygame.font.SysFont(simple, 25, True, False)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            print("Quitting...")
            done = True
            
        elif(event.type == pygame.MOUSEBUTTONDOWN):
            musicIndex = (musicIndex + 1) % len(musicList)
            
        elif(event.type == pygame.KEYDOWN):
            #Key handlers
            if(event.key == pygame.K_SPACE):
                musicIndex = (musicIndex + 1) % len(musicList)
            elif(event.key == pygame.K_z):
                Note("E3", musicList[musicIndex].tempo)
                text = ("E3")
            elif(event.key == pygame.K_x):
                Note("F3", musicList[musicIndex].tempo)
                text = "F3"
            elif(event.key == pygame.K_c):
                Note("G3", musicList[musicIndex].tempo)
                text = "G3"
            elif(event.key == pygame.K_v):
                Note("A3", musicList[musicIndex].tempo)
                text = "A3"
            elif(event.key == pygame.K_b):
                Note("B3", musicList[musicIndex].tempo)
                text = "B3"
            elif(event.key == pygame.K_n):
                Note("C4", musicList[musicIndex].tempo)
                text = "C4"
            elif(event.key == pygame.K_m):
                Note("D4", musicList[musicIndex].tempo)
                text = "D4"
            elif(event.key == pygame.K_COMMA):
                Note("E4", musicList[musicIndex].tempo)
                text = "E4"
            elif(event.key == pygame.K_PERIOD):
                Note("F4", musicList[musicIndex].tempo)
                text = "F4"
            elif(event.key == pygame.K_a):
                Note("G4", musicList[musicIndex].tempo)
                text = "G4"
            elif(event.key == pygame.K_s):
                Note("A4", musicList[musicIndex].tempo)
                text = "A4"
            elif(event.key == pygame.K_d):
                Note("B4", musicList[musicIndex].tempo)
                text = "B4"
            elif(event.key == pygame.K_f):
                Note("C5", musicList[musicIndex].tempo)
                text = "C5"
            elif(event.key == pygame.K_g):
                Note("D5", musicList[musicIndex].tempo)
                text = "D5"
            elif(event.key == pygame.K_h):
                Note("E5", musicList[musicIndex].tempo)
                text = "E5"
            elif(event.key == pygame.K_j):
                Note("F5", musicList[musicIndex].tempo)
                text = "F5"
            elif(event.key == pygame.K_k):
                Note("G5", musicList[musicIndex].tempo)
                text = "G5"
            elif(event.key == pygame.K_l):
                Note("A5", musicList[musicIndex].tempo)
                text = "A5"
            elif(event.key == pygame.K_q):
                Note("B5", musicList[musicIndex].tempo)
                text = "B5"
            elif(event.key == pygame.K_w):
                Note("C6", musicList[musicIndex].tempo)
                text = "C6"
            elif(event.key == pygame.K_e):
                Note("D6", musicList[musicIndex].tempo)
                text = "D6"
            elif(event.key == pygame.K_r):
                Note("E6", musicList[musicIndex].tempo)
                text = "E6"
            elif(event.key == pygame.K_t):
                Note("F6", musicList[musicIndex].tempo)
                text = "F6"
            elif(event.key == pygame.K_y):
                Note("G6", musicList[musicIndex].tempo)
                text = "G6"
            elif(event.key == pygame.K_u):
                Note("A6", musicList[musicIndex].tempo)
                text = "A6"
            elif(event.key == pygame.K_i):
                Note("B6", musicList[musicIndex].tempo)
                text = "B6"
            elif(event.key == pygame.K_o):
                #Hit O for a random tune (Likely a higher tune)
                tone = randint(37, 20000)
                Beep(tone, musicList[musicIndex].tempo)
                text = str(tone)

    musicList[musicIndex].displaySheet()
    
    screen.blit(font.render(text, True, (128, 0, 255)), [300, 200])
    pygame.display.flip()
    
    #Clears screen for redrawing
    screen.fill((255, 255, 255))
    
    clock.tick(60)

pygame.quit()
