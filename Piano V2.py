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
ImBlue = Song("I'm Blue", sheetMusic.imBlue, 125)
AveMaria = Song("Ave Maria", sheetMusic.aveMaria, 240)
AllStar = Song("All Star", sheetMusic.allStar, 250)
TwinkleTwinkle = Song("Twinkle Twinkle", sheetMusic.twinkleTwinkle, 250)

musicIndex = 0

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

#Loading sound files for keys
grandPiano = {}
for key in keys:
    if(key == "  "):
        continue
    grandPiano[key] = pygame.mixer.Sound("Recordings\\"  + "Grand Piano\\" + key[1] + "\\" + key + ".wav")
    
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
                grandPiano["E3"].play()
                text = ("E3")
            elif(event.key == pygame.K_x):
                grandPiano["F3"].play()
                text = "F3"
            elif(event.key == pygame.K_c):
                grandPiano["G3"].play()
                text = "G3"
            elif(event.key == pygame.K_v):
                grandPiano["A3"].play()
                text = "A3"
            elif(event.key == pygame.K_b):
                grandPiano["B3"].play()
                text = "B3"
            elif(event.key == pygame.K_n):
                grandPiano["C4"].play()
                text = "C4"
            elif(event.key == pygame.K_m):
                grandPiano["D4"].play()
                text = "D4"
            elif(event.key == pygame.K_COMMA):
                grandPiano["E4"].play()
                text = "E4"
            elif(event.key == pygame.K_PERIOD):
                grandPiano["F4"].play()
                text = "F4"
            elif(event.key == pygame.K_a):
                grandPiano["G4"].play()
                text = "G4"
            elif(event.key == pygame.K_s):
                grandPiano["A4"].play()
                text = "A4"
            elif(event.key == pygame.K_d):
                grandPiano["B4"].play()
                text = "B4"
            elif(event.key == pygame.K_f):
                grandPiano["C5"].play()
                text = "C5"
            elif(event.key == pygame.K_g):
                grandPiano["D5"].play()
                text = "D5"
            elif(event.key == pygame.K_h):
                grandPiano["E5"].play()
                text = "E5"
            elif(event.key == pygame.K_j):
                grandPiano["F5"].play()
                text = "F5"
            elif(event.key == pygame.K_k):
                grandPiano["G5"].play()
                text = "G5"
            elif(event.key == pygame.K_l):
                grandPiano["A5"].play()
                text = "A5"
            elif(event.key == pygame.K_q):
                grandPiano["B5"].play()
                text = "B5"
            elif(event.key == pygame.K_w):
                grandPiano["C6"].play()
                text = "C6"
            elif(event.key == pygame.K_e):
                grandPiano["D6"].play()
                text = "D6"
            elif(event.key == pygame.K_r):
                grandPiano["E6"].play()
                text = "E6"
            elif(event.key == pygame.K_t):
                grandPiano["F6"].play()
                text = "F6"
            
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
