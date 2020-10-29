import pygame
import os, random

class Musica:

    def __init__(self):
        self.music = pygame.mixer.Sound("music/Musk.wav")

    def _play_music(self):
        pygame.mixer.init()
        self.music.play()