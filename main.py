import pygame, sys
from pygame.locals import *

tileSIZE = 32

grid = [
    #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 1,-1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0], # 7
    [0, 0, 0, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 2, 2, 2, 0, 0, 0], # 8
    [0, 0, 0, 1, 1, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

spawn_point = (4 * tileSIZE, 7 * tileSIZE)
direction = [(1, 0), (-1, 0)]

tileROW = len(grid) 
tileCOL = len(grid[0]) 

print(tileROW)
print(tileCOL)

class Player():
    def __init__(self):
        self.x = -1
        self.y = -1
        self.speed = 170
        
        self.size = 0.8
    
    def check_TL(self, x, y):
        ts = tileSIZE
        return grid[int(y / ts)][int(x / ts)] == 0     
        
    def check_TR(self, x, y):
        ts = tileSIZE
        x = x + ts * self.size
        return grid[int(y / ts)][int(x / ts)] == 0     
    
    def check_BL(self, x, y):
        ts = tileSIZE
        y = y + ts * self.size
        return grid[int(y / ts)][int(x / ts)] == 0        
    
    def check_BR(self, x, y):
        ts = tileSIZE
        x = x + ts * self.size
        y = y + ts * self.size
        return grid[int(y / ts)][int(x / ts)] == 0        
    
    def update(self, dt):

        
        keys=pygame.key.get_pressed()
        ts = tileSIZE
        
        offset = 0.01
        
        if keys[pygame.K_a]:
            self.x -= self.speed * dt
            if self.check_TL(self.x + offset, self.y + offset) or self.check_BL(self.x + offset, self.y - offset):
                self.x = round(self.x / ts) * ts

        if keys[pygame.K_d]:
            self.x += self.speed * dt
            if self.check_TR(self.x - offset, self.y + offset) or self.check_BR(self.x - offset, self.y - offset):
                self.x = round((self.x + ts * self.size) / ts) * ts - ts * self.size
    
        if keys[pygame.K_w]:
            self.y -= self.speed * dt
            if self.check_TL(self.x + offset, self.y + offset) or self.check_TR(self.x - offset, self.y + offset):
                self.y = round(self.y / ts) * ts

        if keys[pygame.K_s]:
            self.y += self.speed * dt
            if self.check_BL(self.x + offset, self.y + offset) or self.check_BR(self.x - offset, self.y - offset):
                self.y = round((self.y + ts * self.size) / ts) * ts - ts * self.size
            


 
        
        
    def draw(self, screen):
        """
        cntr_x = self.x + (tileSIZE * self.size / 2)
        cntr_y = self.y + (tileSIZE * self.size / 2)
        """
        pygame.draw.rect(screen, "#1e1e1e", (self.x, self.y
                                             , tileSIZE * self.size, tileSIZE * self.size))
        pygame.draw.rect(screen, "#ff0000", (self.x + 5, self.y + 5
                                             , tileSIZE * self.size - 10, tileSIZE * self.size - 10))        
            
class Enemy():
    def __init__(self,
                posA, posB,
                direc_idx):
        self.posA = posA
        self.posB = posB
        
        self.x = posA[0]
        self.y = posA[1]
         
        self.direc_idx = direc_idx
        
        self.speed = 300
        self.size = 0.3
        
        

    def update(self, dt):
        self.x += direction[self.direc_idx][0] * self.speed * dt
        self.y += direction[self.direc_idx][1] * self.speed * dt
        
        if grid[int(self.y / tileSIZE)][int(self.x / tileSIZE)] == 0 or grid[int(self.y / tileSIZE)][int(self.x / tileSIZE) + 1] == 0:
            self.direc_idx = (self.direc_idx + 1) % len(direction)
            self.x += direction[self.direc_idx][0] * self.speed * dt

    def draw(self, screen):
        cntr_x = self.x + tileSIZE / 2
        cntr_y = self.y + tileSIZE / 2
        
        pygame.draw.circle(screen, "#000000", (cntr_x, cntr_y), tileSIZE * self.size)
        pygame.draw.circle(screen, "#0000ff", (cntr_x, cntr_y), tileSIZE * self.size - 5)
        
def intersects(rect, r, center):
    circle_distance_x = abs(center[0]-rect.centerx)
    circle_distance_y = abs(center[1]-rect.centery)
    if circle_distance_x > rect.w/2.0+r or circle_distance_y > rect.h/2.0+r:
        return False
    if circle_distance_x <= rect.w/2.0 or circle_distance_y <= rect.h/2.0:
        return True
    corner_x = circle_distance_x-rect.w/2.0
    corner_y = circle_distance_y-rect.h/2.0
    corner_distance_sq = corner_x**2.0 +corner_y**2.0
    return corner_distance_sq <= r**2.0  




windowHeight = tileSIZE * tileROW
windowWidth = tileSIZE * tileCOL

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('World Hardest Game')



player = Player()
enemies = [Enemy((16 * tileSIZE, 8 * tileSIZE), (7 * tileSIZE, 8 * tileSIZE), 1),
           Enemy((7 * tileSIZE, 7 * tileSIZE), (16 * tileSIZE, 7 * tileSIZE), 1),
           Enemy((16 * tileSIZE, 6 * tileSIZE), (7 * tileSIZE, 6 * tileSIZE), 1),
           Enemy((7 * tileSIZE, 5 * tileSIZE), (16 * tileSIZE, 5 * tileSIZE), 1),
           ]

clock = pygame.time.Clock()



while 1:
    dt = clock.tick(60) / 1000.0 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill("#b4b5fe")
    
    for i in range(tileROW):
        for j in range(tileCOL):
            if grid[i][j] == -1 and (player.y < 0 or player.x < 0):
                player.y = i * tileSIZE
                player.x = j * tileSIZE
            
            
            if grid[i][j] in {1, 2, -1}:
                pygame.draw.rect(screen, "#b5feb4", (tileSIZE * j, tileSIZE * i, tileSIZE, tileSIZE))
            elif grid[i][j] == 3:
                if (i + j) % 2 == 0:
                    pygame.draw.rect(screen, "#e6e6ff", (tileSIZE * j, tileSIZE * i, tileSIZE, tileSIZE))
                else:
                    pygame.draw.rect(screen, "#f7f7ff", (tileSIZE * j, tileSIZE * i, tileSIZE, tileSIZE))
                    
            
            if grid[i][j] != 0:
                if i == 0 or grid[i - 1][j] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSIZE * j, tileSIZE * i), (tileSIZE * (j + 1), tileSIZE * i), 4)
                if i == tileROW - 1 or grid[i + 1][j] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSIZE * j, tileSIZE * (i + 1)), (tileSIZE * (j + 1), tileSIZE * (i + 1)), 4)
                    
                if j == 0 or grid[i][j - 1] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSIZE * j, tileSIZE * i), (tileSIZE * (j), tileSIZE * (i + 1)), 4)
                if i == tileCOL - 1 or grid[i][j + 1] == 0:
                    pygame.draw.line(screen, "#1e1e1e", (tileSIZE * (j + 1), tileSIZE * i), (tileSIZE * (j + 1), tileSIZE * (i + 1)), 4)
    
    player.update(dt)
    player.draw(screen)
    
    for now in enemies:
        now.update(dt)
        now.draw(screen)

        if intersects(pygame.Rect(player.x, player.y, tileSIZE * player.size, tileSIZE * player.size), tileSIZE * now.size, (now.x + tileSIZE / 2, now.y + tileSIZE / 2)):
            player.x = spawn_point[0]
            player.y = spawn_point[1]
    
        
                
    
    pygame.display.update()

#pygame.draw.rect(surface, color, rect, width=0, border_radius=-1)
#pygame.draw.line(surface, color, start_pos, end_pos, width)