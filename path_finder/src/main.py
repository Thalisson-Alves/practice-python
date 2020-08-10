import pygame
from Setup import SetUp
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GRID_N = 50
SPOT_SIZE = (SCREEN_HEIGHT//GRID_N, SCREEN_WIDTH//GRID_N)

SCENE = SetUp(GRID_N, SPOT_SIZE)

FPS = 250
CLOCK = pygame.time.Clock()
while True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        SCENE.handle_event(event)
        if isinstance(SCENE, SetUp):
            if SCENE.end:
                SCENE = SCENE.grid

    SCREEN.fill((100, 100, 100))
    SCENE.show(SCREEN)
    SCENE.update()

    pygame.display.update()
