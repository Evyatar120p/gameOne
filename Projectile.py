import pygame

class projectile(object):
    def __init__(self, x, y, radius, color, facing ):    #this is to add bullets
        self.y = y
        self.x = x
        self.radius = radius
        self.color = color
        self.facing = facing   #this will be  1 or -1 depend on where the player is facing
        self.vel = 12 * facing

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x , self.y), self.radius)   #this is how to make a circle, if i want him to br empty i can add 1 in the end


