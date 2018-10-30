from winsound import Beep
from time import sleep
import sheetMusic
import pygame

beep = {"E2": 82, "F2": 87, "G2": 98, "A2": 110, "B2": 123, "C3": 131, "D3": 147, "E3": 165, "F3": 175,
         "G3": 196, "A3": 220, "B3": 247, "C4": 262, "D4": 294, "E4": 330, "F4": 349, "G4": 392, "A4": 440,
         "B4": 494,  "C5": 523, "D5": 587, "E5": 659, "F5": 698, "G5": 784, "A5": 880, "B5": 988, "C6": 1047,
         "D6": 1175, "E6": 1319, "F6": 1397, "G6": 1568, "A6": 1760, "B6": 1976}

keys = ["E2", "F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4" ,  "G4", "A4", "B4" ,  "C5", "D5", "E5",
        "F5", "G5", "A5", "B5", "C6", "D6", "E6", "F6"]

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

instrumentList = ["Beep"]

class Song(object):
    
    def __init__(self, name, music, tempo):
        self.name = name
        self.sheetMusic = music
        self.tempo = tempo
        
    def play(self, instrument):
        music = self.sheetMusic.replace("\n", "")
        for note in range(int(len(music)/2)):
            tune = music[(note * 2): (note * 2 + 2)]
            if(tune != "  "):
                if(instrument == "Beep"):
                    Beep(beep[tune], int(self.tempo))
                else:
                    instrument.keys[tune].play()
                    sleep(self.tempo/1000)
            elif(tune == "  "):
                sleep(self.tempo/1000)

class Instrument(object):
    def __init__(self, name):
        self.name = name
        self.keys = {}

        instrumentList.append(self)
        
        for key in keys:
            if(key != "  "):
                self.keys[key] = pygame.mixer.Sound("Recordings\\"  + name + "\\" + key[1] + "\\" + key + ".wav")
        
GrandPiano = Instrument("Grand Piano")
BrightPiano = Instrument("Bright Piano")

FunkyTown = Song("Funky Town", sheetMusic.funkyTown, 250)
FurElise = Song("Für Elise", sheetMusic.furElise, 250)
TakeOnMe = Song("Take On Me", sheetMusic.takeOnMe, 250)
JingleBells = Song("Jingle Bells", sheetMusic.jingleBells, 250)
LostWoods = Song("Lost Woods", sheetMusic.lostWoods, 250)
ImBlue = Song("I'm Blue", sheetMusic.imBlue, 254)
AveMaria = Song("Ave Maria", sheetMusic.aveMaria, 480)
LetItSnow = Song("Let It Snow", sheetMusic.letItSnow, 200)
AllStar = Song("All Star", sheetMusic.allStar, 250)
TwinkleTwinkle = Song("Twinkle Twinkle", sheetMusic.twinkleTwinkle, 500)

FunkyTown.play("Beep")
