import pygame
from Grid import Grid

class SetUp:
    def __init__(self, grid_n, spot_size):
        self.grid = Grid(spot_size, grid_n)
        self.target = pygame.Surface(spot_size)
        self.target.set_colorkey(0)
        pygame.draw.circle(self.target, (255, 0, 0), (spot_size[0]//2, spot_size[1]//2), spot_size[0]//2)
        self.start = pygame.Surface(spot_size)
        pygame.draw.circle(self.start, (0, 255, 0), (spot_size[0]//2, spot_size[1]//2), spot_size[0]//2)
        self.start.set_colorkey(0)
        self.spot_size = spot_size[0]
        self.start_follow = False
        self.target_follow = False
        self.end = False
        self.set_wall = False
        self.clear_wall = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.end = True
                self.grid.current = self.grid.body[self.grid.start_pos[0]][self.grid.start_pos[1]]
                self.grid.open_set.append(self.grid.current)
                self.grid.add_neighbor()
                
        pos = pygame.mouse.get_pos()
        pos = (pos[0]//self.spot_size, pos[1]//self.spot_size)
        if pygame.mouse.get_pressed()[0]:
            if pos == self.grid.start_pos:
                self.start_follow = True
            elif pos == self.grid.target_pos:
                self.target_follow = True
        else:
            self.start_follow = False
            self.target_follow = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.set_wall = not self.grid.body[pos[0]][pos[1]].wall
            self.clear_wall = self.grid.body[pos[0]][pos[1]].wall
        elif event.type == pygame.MOUSEBUTTONUP:
            self.set_wall = False
            self.clear_wall = False
            self.grid.body[self.grid.target_pos[0]][self.grid.target_pos[1]].wall = False
            self.grid.body[self.grid.start_pos[0]][self.grid.start_pos[1]].wall = False

    def update(self):
        mouse = pygame.mouse.get_pos()
        mouse = mouse[0]//self.spot_size, mouse[1]//self.spot_size
        if self.start_follow:
            self.grid.start_pos = mouse
        elif self.target_follow:
            self.grid.target_pos = mouse
        elif self.set_wall:
            self.grid.body[mouse[0]][mouse[1]].wall = True
        elif self.clear_wall:
            self.grid.body[mouse[0]][mouse[1]].wall = False

    
    def show(self, screen):                    
        self.grid.show(screen)
        screen.blit(self.target, (self.grid.target_pos[0]*self.spot_size, self.grid.target_pos[1]*self.spot_size))
        screen.blit(self.start, (self.grid.start_pos[0]*self.spot_size, self.grid.start_pos[1]*self.spot_size))
