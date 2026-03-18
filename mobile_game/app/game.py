import pygame
from animation import Animation
from sound import Sound
from utils.helpers import detect_touch

class Game:
    def __init__(self):
        self.score = 0
        self.animation = Animation()
        self.sound = Sound()

    def start(self):
        self.score = 0
        self.sound.play_start_sound()
        self.animation.start_dancing()

    def on_touch(self):
        if detect_touch():
            self.score += 1
            self.animation.increase_speed()
            self.sound.play_speed_up_sound()
