import pygame
from src.events.event_handler import EventHandler

event_handler = EventHandler()

window_width = 800
window_height = 1200
name = "Me Pub"

pygame.init()
window = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Me Pub")
while True:
    for event in pygame.event.get():
        event_handler.check_event(window, event)
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
    if keys[pygame.K_RIGHT]:
    if keys[pygame.K_UP]:
    if keys[pygame.K_DOWN]:



    pygame.draw.rect(window, (255,150, 0), (20, 20, 50, 60))
    pygame.display.update()

