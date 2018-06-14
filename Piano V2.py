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
keys = {"C2": "^Z", "D2": "^X", "E2": "^C", "F2": "^V", "G2": "^B", "A2": "^N", "B2": "^M", "C3": "^,",
        "D3": "^.", "E3": "Z", "F3": "X", "G3": "C", "A3": "V", "B3": "B", "C4": "N", "D4": "M", "E4": ",",
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
LetItSnow = Song("Let It Snow", sheetMusic.letItSnow, 125)
AllStar = Song("All Star", sheetMusic.allStar, 250)
TwinkleTwinkle = Song("Twinkle Twinkle", sheetMusic.twinkleTwinkle, 250)

musicIndex = 0

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

#Loading sound files for keys
instrumentList = []

class Instrument(object):
    def __init__(self, name):
        self.name = name
        self.keys = {}

        for key in keys:
            if(key != "  "):
                self.keys[key] = pygame.mixer.Sound("Recordings\\"  + name + "\\" + key[1] + "\\" + key + ".wav")
        instrumentList.append(self)
        
GrandPiano = Instrument("Grand Piano")
BrightPiano = Instrument("Bright Piano")
instrumentIndex = 0

#Miscellaneous
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
            #Cycles through instruments
            if(event.key == pygame.K_TAB):
                instrumentIndex = (instrumentIndex + 1) % len(instrumentList)
            #Cycles through sheet music
            elif(event.key == pygame.K_SPACE):
                musicIndex = (musicIndex + 1) % len(musicList)
                
            #Lowest keys needs mods
            elif(event.key == pygame.K_z and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["C2"].play()
                text = ("C2")
            elif(event.key == pygame.K_x and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["D2"].play()
                text = ("D2")
            elif(event.key == pygame.K_c and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["E2"].play()
                text = ("E2")
            elif(event.key == pygame.K_v and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["F2"].play()
                text = ("F2")
            elif(event.key == pygame.K_b and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["G2"].play()
                text = ("G2")
            elif(event.key == pygame.K_n and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["A2"].play()
                text = ("A2")
            elif(event.key == pygame.K_m and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["B2"].play()
                text = ("B2")
            elif(event.key == pygame.K_COMMA and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["C3"].play()
                text = ("C3")
            elif(event.key == pygame.K_PERIOD and (pygame.key.get_mods() & pygame.KMOD_LSHIFT)):
                instrumentList[instrumentIndex].keys["D3"].play()
                text = ("D3")
                
            #Normal keys
            elif(event.key == pygame.K_z):
                instrumentList[instrumentIndex].keys["E3"].play()
                text = ("E3")
            elif(event.key == pygame.K_x):
                instrumentList[instrumentIndex].keys["F3"].play()
                text = "F3"
            elif(event.key == pygame.K_c):
                instrumentList[instrumentIndex].keys["G3"].play()
                text = "G3"
            elif(event.key == pygame.K_v):
                instrumentList[instrumentIndex].keys["A3"].play()
                text = "A3"
            elif(event.key == pygame.K_b):
                instrumentList[instrumentIndex].keys["B3"].play()
                text = "B3"
            elif(event.key == pygame.K_n):
                instrumentList[instrumentIndex].keys["C4"].play()
                text = "C4"
            elif(event.key == pygame.K_m):
                instrumentList[instrumentIndex].keys["D4"].play()
                text = "D4"
            elif(event.key == pygame.K_COMMA):
                instrumentList[instrumentIndex].keys["E4"].play()
                text = "E4"
            elif(event.key == pygame.K_PERIOD):
                instrumentList[instrumentIndex].keys["F4"].play()
                text = "F4"
            elif(event.key == pygame.K_a):
                instrumentList[instrumentIndex].keys["G4"].play()
                text = "G4"
            elif(event.key == pygame.K_s):
                instrumentList[instrumentIndex].keys["A4"].play()
                text = "A4"
            elif(event.key == pygame.K_d):
                instrumentList[instrumentIndex].keys["B4"].play()
                text = "B4"
            elif(event.key == pygame.K_f):
                instrumentList[instrumentIndex].keys["C5"].play()
                text = "C5"
            elif(event.key == pygame.K_g):
                instrumentList[instrumentIndex].keys["D5"].play()
                text = "D5"
            elif(event.key == pygame.K_h):
                instrumentList[instrumentIndex].keys["E5"].play()
                text = "E5"
            elif(event.key == pygame.K_j):
                instrumentList[instrumentIndex].keys["F5"].play()
                text = "F5"
            elif(event.key == pygame.K_k):
                instrumentList[instrumentIndex].keys["G5"].play()
                text = "G5"
            elif(event.key == pygame.K_l):
                instrumentList[instrumentIndex].keys["A5"].play()
                text = "A5"
            elif(event.key == pygame.K_q):
                instrumentList[instrumentIndex].keys["B5"].play()
                text = "B5"
            elif(event.key == pygame.K_w):
                instrumentList[instrumentIndex].keys["C6"].play()
                text = "C6"
            elif(event.key == pygame.K_e):
                instrumentList[instrumentIndex].keys["D6"].play()
                text = "D6"
            elif(event.key == pygame.K_r):
                instrumentList[instrumentIndex].keys["E6"].play()
                text = "E6"
            elif(event.key == pygame.K_t):
                instrumentList[instrumentIndex].keys["F6"].play()
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
