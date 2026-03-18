import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.start_sound = pygame.mixer.Sound('assets/sounds/dance_start.wav')
        self.speed_up_sound = pygame.mixer.Sound('assets/sounds/speed_up.wav')

    def play_start_sound(self):
        self.start_sound.play()

    def play_speed_up_sound(self):
        self.speed_up_sound.play()
