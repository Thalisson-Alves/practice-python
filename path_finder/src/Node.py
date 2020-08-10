import pygame

class Node:
    def __init__(self, size, y, x):
        self.body = pygame.Surface((size[0]-1, size[1]-1))
        self.wall = False
        self.color = (255, 255, 255)
        self.size = size
        self.neighbors = list()
        self.previous = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.x_position = x
        self.y_position = y

    def show(self, screen, color):
        if self.wall:
            color = 0
        self.color = color
        pos = self.x_position * self.size[0] + 1, self.y_position * self.size[1] + 1
        self.body.fill(self.color)
        screen.blit(self.body, pos)
