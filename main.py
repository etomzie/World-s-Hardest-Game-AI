#!/usr/local/bin/python3.4
import pygame, sys
from pygame.locals import *






tileSize = 32

grid = [

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1,-1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

tileROW = len(grid) 
tileCOL = len(grid[0]) 

print(tileROW)
print(tileCOL)




class Player():
    def __init__(self):
        self.x = -1
        self.y = -1
        self.speed = 0.2
        
        self.size = 0.8
        
    
    def update(self):

        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
            rx -= self.speed
            lx -= self.speed
            
        #if grid[int(self.y // tileSize)][int((self.x) // tileSize)] == 0:
        #    self.x = int((self.x + tileSize * self.size) // tileSize) * tileSize + tileSize * self.size - tileSize * self.size
                
                
        if keys[pygame.K_d]:
            self.x += self.speed
            rx += self.speed
            lx += self.speed
            
        #    if grid[int(self.y // tileSize)][int((self.x + tileSize * self.size) // tileSize)] == 0:
        #        self.x = int((self.x + tileSize * self.size) // tileSize) * tileSize + tileSize * (1 - self.size) / 2 - tileSize * self.size

        if keys[pygame.K_w]:
            self.y -= self.speed
     
        #    if grid[int(ty / tileSize)][int(lx / tileSize)] == 0 or grid[int(ty / tileSize)][int(rx / tileSize)] == 0:
        #        self.y = round(ty / tileSize) * tileSize
            """
            if grid[int(ty // tileSize)][int(lx // tileSize)] == 0 or \
                grid[int(ty // tileSize)][int(rx // tileSize)] == 0:
                snap_y = round(ty / tileSize) * tileSize
                if grid[round(ty / tileSize)][round(self.x / tileSize)] != 0:
                    self.y = snap_y
            """
        if keys[pygame.K_s]:
            self.y += self.speed

        #    if grid[int(by // tileSize)][int(lx // tileSize)] == 0 or \
        #        grid[int(by // tileSize)][int(rx // tileSize)] == 0:
        #        snap_y = int(by // tileSize) * tileSize + tileSize * (1 - self.size) / 2 - tileSize * self.size
        #        if grid[int(snap_y // tileSize)][int(self.x // tileSize)] != 0:
        #            self.y = snap_y
        
        lx = self.x
        rx = self.x + tileSize * self.size
        ty = self.y
        by = self.y + tileSize * self.size
        
        if grid[int(by / tileSize)][int(lx / tileSize)] == 0:
            
        

        
        
        
    def draw(self, screen):
        cntr_x = self.x + (tileSize * self.size / 2)
        cntr_y = self.y + (tileSize * self.size / 2)
        
        pygame.draw.rect(screen, "#1e1e1e", (cntr_x - (tileSize * self.size / 2), cntr_y - (tileSize * self.size / 2)
                                             , tileSize * self.size, tileSize * self.size))
        pygame.draw.rect(screen, "#ff0000", (cntr_x - (tileSize * self.size / 2) + 5, cntr_y - (tileSize * self.size / 2) + 5
                                             , tileSize * self.size - 10, tileSize * self.size - 10))
        
        




windowHeight = tileSize * tileROW
windowWidth = tileSize * tileCOL

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('World Hardest Game')



player = Player()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill("#b4b5fe")
    
    for i in range(tileROW):
        for j in range(tileCOL):
            if grid[i][j] == -1 and (player.y < 0 or player.x < 0):
                player.y = i * tileSize
                player.x = j * tileSize
            
            
            if grid[i][j] in {1, 2, -1}:
                pygame.draw.rect(screen, "#b5feb4", (tileSize * j, tileSize * i, tileSize, tileSize))
            elif grid[i][j] == 3:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, "#e6e6ff", (tileSize * j, tileSize * i, tileSize, tileSize))
                else:
                    pygame.draw.rect(screen, "#f7f7ff", (tileSize * j, tileSize * i, tileSize, tileSize))
                    
            
            if grid[i][j] != 0:
                if i == 0 or grid[i - 1][j] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSize * j, tileSize * i), (tileSize * (j + 1), tileSize * i), 4)
                if i == tileROW - 1 or grid[i + 1][j] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSize * j, tileSize * (i + 1)), (tileSize * (j + 1), tileSize * (i + 1)), 4)
                    
                if j == 0 or grid[i][j - 1] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSize * j, tileSize * i), (tileSize * (j), tileSize * (i + 1)), 4)
                if i == tileCOL - 1 or grid[i][j + 1] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSize * (j + 1), tileSize * i), (tileSize * (j + 1), tileSize * (i + 1)), 4)
    
    player.update()
    player.draw(screen)
                
    
    pygame.display.update()

#pygame.draw.rect(surface, color, rect, width=0, border_radius=-1)
#pygame.draw.line(surface, color, start_pos, end_pos, width)