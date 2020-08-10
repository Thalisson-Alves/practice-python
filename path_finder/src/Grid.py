import pygame
from Node import Node 

class Grid:
    def __init__(self, spot_size, grid_size):
        self.body = [[Node(spot_size, j, i) for j in range(grid_size)] for i in range(grid_size)]
        self.grid_size = grid_size
        self.start_pos = 0, 0
        self.target_pos = grid_size-1, grid_size-1
        self.path = list()
        self.open_set = list()
        self.closed_set = list()
        self.debug = False
        self.current = None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.debug = not self.debug

    def add_neighbor(self):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                for d in directions:
                    new_i = d[0] + i
                    new_j = d[1] + j
                    if 0 <= new_i < self.grid_size and 0 <= new_j < self.grid_size and not self.body[new_i][new_j].wall:
                        self.body[i][j].neighbors.append(self.body[new_i][new_j])

    def heuristic(self, a: Node, b: Node):
        return abs(b.x_position - a.x_position) + abs(b.y_position - a.y_position)
        # return ((b.x_position - a.x_position)**2 + (b.y_position - a.y_position)**2)**0.5

    def a_star(self):
        if len(self.open_set) > 0 and self.current != self.body[self.target_pos[0]][self.target_pos[1]]:
            self.current = self.open_set[0]
            for spot in self.open_set:
                if spot.f_score < self.current.f_score:
                    self.current = spot
            
            self.open_set.remove(self.current)
            self.closed_set.append(self.current)

            for neighbor in self.current.neighbors:
                if neighbor not in self.closed_set:
                    temp_g = self.current.g_score + 1
                    if neighbor in self.open_set:
                        new_path = False
                        if temp_g < neighbor.g_score:
                            neighbor.g_score = temp_g
                            new_path = True
                    else:
                        neighbor.g_score = temp_g
                        new_path = True
                        self.open_set.append(neighbor)
                    
                    if new_path:
                        neighbor.h_score = self.heuristic(neighbor, self.body[self.target_pos[0]][self.target_pos[1]])
                        neighbor.f_score = neighbor.g_score + neighbor.h_score
                        neighbor.previous = self.current
        else:
            pass
            
        self.path = [self.current]
        temp = self.current.previous
        while temp:
            self.path.append(temp)
            temp = temp.previous

    def update(self):
        self.a_star()

    def show(self, screen):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.current and i == self.target_pos[0] and j == self.target_pos[1]:
                    self.body[i][j].show(screen, (150, 50, 61))
                else:
                    self.body[i][j].show(screen, (255, 255, 255))

        
        if self.debug:
            for node in self.open_set:
                node.show(screen, (0, 255, 0))
            for node in self.closed_set:
                node.show(screen, (255, 0, 0))
        
        for p in self.path:
            p.show(screen, (0, 0, 255))
