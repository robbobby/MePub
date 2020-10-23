import pygame


class EventHandler:
    def __init__(self):
        pygame.init()
        self.keys = pygame.key.get_pressed()

    def check_event(self, window, event):
        if event.type == pygame.QUIT:
            return pygame.quit()