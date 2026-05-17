import pygame, sys
from pygame.locals import *
import neat
import math


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

windowHeight = tileSIZE * tileROW
windowWidth = tileSIZE * tileCOL

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('World Hardest Game')

dest = (18 * tileSIZE, 4 * tileSIZE)




class Player():
    def __init__(self):
        self.x = spawn_point[0]
        self.y = spawn_point[1]
        self.speed = 120 * tileSIZE / 32
        
        self.size = 0.8
        self.state = "alive"

    
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
    
    def update(self, dt, input):


        
        ts = tileSIZE
        
        offset = 0.01
        
        
        self.x += self.speed * dt * input[1]
        if self.check_TL(self.x + offset, self.y + offset) or self.check_BL(self.x + offset, self.y - offset):
            self.x = round(self.x / ts) * ts

        if self.check_TR(self.x - offset, self.y + offset) or self.check_BR(self.x - offset, self.y - offset):
            self.x = round((self.x + ts * self.size) / ts) * ts - ts * self.size
    
        
        self.y += self.speed * dt * input[0]
        if self.check_TL(self.x + offset, self.y + offset) or self.check_TR(self.x - offset, self.y + offset):
            self.y = round(self.y / ts) * ts

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
        
        self.speed = 300 * tileSIZE / 32
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
            


class Game():
    def __init__(self, genomes):
        

        self.enemies = [Enemy((16 * tileSIZE, 8 * tileSIZE), (7 * tileSIZE, 8 * tileSIZE), 1),
                Enemy((7 * tileSIZE, 7 * tileSIZE), (16 * tileSIZE, 7 * tileSIZE), 1),
                Enemy((16 * tileSIZE, 6 * tileSIZE), (7 * tileSIZE, 6 * tileSIZE), 1),
                Enemy((7 * tileSIZE, 5 * tileSIZE), (16 * tileSIZE, 5 * tileSIZE), 1),
                ]


        self.clock = pygame.time.Clock()

        
        
        self.players = {}
        self.fitness = {}
        self.states = {}
        for genome_id, genome in genomes:
            self.states[genome] = 1
            self.fitness[genome] = 0
            self.players[genome] = Player()
            genome.fitness = 0
            
        
        self.max_loop_iteration = 300

    

    def update(self, genomes, config, networks):
        dt = self.clock.tick(60) / 1000.0 
        dt *= 2
                
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
                
        screen.fill("#b4b5fe")
            
        for i in range(tileROW):
            for j in range(tileCOL):
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
                    if j == tileCOL - 1 or grid[i][j + 1] == 0:
                        pygame.draw.line(screen, "#1e1e1e", (tileSIZE * (j + 1), tileSIZE * i), (tileSIZE * (j + 1), tileSIZE * (i + 1)), 4)
                        
                        
        for now in self.enemies:
            now.update(dt)
            now.draw(screen)
        
        
        for genome_id, genome in genomes:
            if self.states[genome] == 0:
                continue
            
            player = self.players[genome]
            if grid[int(player.y / tileSIZE)][int(player.x / tileSIZE)] == 0:
                player.x = spawn_point[0]
                player.y = spawn_point[1]


            #self.fitness[genome] += 0.1
            #genome.fitness += 0.2

            #print(ge)
            # Create a neural network from this genome
            net = networks[genome]
            """
            enemies = []
            for enemy in self.enemies:
                enemies.extend([enemy.x, enemy.y])
                
            enemies = tuple(enemies)
            end = (dest[0], dest[1])
            pos = (player.x, player.y)
            #end = (abs(player.x - dest[0]), abs(player.y - dest[1]))
            output = net.activate(enemies + pos + end)

            """

            # Calculate distances relative to the player
            inputs = []
            for enemy in self.enemies:
                # Distance to each enemy (dx, dy)
                inputs.extend([enemy.x - player.x, enemy.y - player.y])

            # Distance to the destination (dx, dy)
            inputs.extend([dest[0] - player.x, dest[1] - player.y])

            # Feed these 10 inputs into the network (update configs.cfg num_inputs to 10!)
            output = net.activate(inputs)
            
            
            output[0] = round(output[0])
            output[1] = round(output[1])
            
            prev = (player.x, player.y)
            player.update(dt, output)
            after = (player.x, player.y)
            
            if prev[0] < after[0]:
                genome.fitness += 1
            else:
                genome.fitness -= 1
            if prev[1] > after[1]:
                genome.fitness += 1
            else:
                genome.fitness -= 1
        

            
            if grid[int(player.y / tileSIZE)][int(player.x / tileSIZE)] in {1, -1}:
                genome.fitness -= 10
            
            
            

            #print(player.x, player.y)
            
            player.draw(screen)
            


           
            
            for now in self.enemies:
                if self.intersects(pygame.Rect(player.x, player.y, tileSIZE * player.size, tileSIZE * player.size), tileSIZE * now.size, (now.x + tileSIZE / 2, now.y + tileSIZE / 2)):
                    #self.players.x = spawn_point[0]
                    #self.players.y = spawn_point[1]
                    #self.fitness[genome] = math.sqrt((dest[0] - player.x) ** 2 + (dest[1] - player.y) ** 2) * -1
                    self.states[genome] = 0



                    #genome.fitness = self.fitness[i]
                    
                elif (int(player.x), int(player.y)) == (dest[0], dest[1]):
                    #self.fitness[genome] = 1000
                    self.states[genome] = 0
                    #genome.fitness = self.fitness[i]
            
            
            
        pygame.display.update()
        self.max_loop_iteration -= 1
        if self.max_loop_iteration == 0:
            for genome_id, genome in genomes:

                #self.fitness[genome] = -10000
                player = self.players[genome]
                #self.fitness[genome] = math.sqrt((dest[0] - player.x) ** 2 + (dest[1] - player.y) ** 2) * -1
                
                
                if grid[int(player.y / tileSIZE)][int(player.x / tileSIZE)] in {1, -1}:
                    #print("here")
                    genome.fitness -= 20000
                elif grid[int(player.y / tileSIZE)][int(player.x / tileSIZE)] == 2:
                    genome.fitness += 10000
                else:
                    pass
                genome.fitness -= math.sqrt((dest[0] - player.x) ** 2 + (dest[1] - player.y) ** 2) * 4
                
                    
                    
                    
                self.states[genome] = 0
                    
                    
        
                    
        

    def intersects(self, rect, r, center):
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



# [(p_x, p_y), (out_x, out_y), genome]
# [((p_x, p_y)), genome, config]


def eval_genomes(genomes, config):
    
    game = Game(genomes)
    networks = {}
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        networks[genome] = net


    while 1:
        game.update(genomes, config, networks)

            
        states = game.states
        if 1 not in states.values():
            #fitness = game.fitness
            for genome_id, genome in genomes:
                # Create a neural network from this genome
                genome.fitness += game.fitness[genome]
            break
        
    
            
            

            
            
            
            

# Load configuration
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'configs.cfg')

# Create population
p = neat.Population(config)
p.add_reporter(neat.StdOutReporter(True))

# Run evolution for up to 300 generations
winner = p.run(eval_genomes, 10000)

# Test the winner

print('\nBest genome:\n{!s}'.format(winner))


#pygame.draw.rect(surface, color, rect, width=0, border_radius=-1)
#pygame.draw.line(surface, color, start_pos, end_pos, width)