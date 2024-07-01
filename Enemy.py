import pygame
import time

class enemy(object):
    # the pic of the enemy
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]



    # definning the enemy
    def __init__(self,x ,y ,width ,hight, end):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.end = end
        self.path = [x,end]  #the start and the end posision
        self.walkCount = 0
        self.vel = 3

        #to make a hit box
        self.hitbox = (self.x + 10, self.y, 45 ,60)
        self.hit_time = 0
        self.hit_duration = 0.2  # Duration for the explosion to be visible (in seconds)
        self.explosion_image = pygame.image.load('explosion.png')  # the explosion image

        #to track the enemy health
        self.health = 10
        self.visible = True


    # drawing the anemy
    def draw(self,screen):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33: #there are 11 pics and 3 pics every 3 milisec so 3 * 11 = 33
                self.walkCount = 0

            if self.vel > 0 :   #to move right
                screen.blit(self.walkRight[self.walkCount // 3] , (self.x, self.y))
                self.walkCount += 1

            else:          #to move left
                screen.blit(self.walkLeft[self.walkCount // 3] , (self.x , self.y))
                self.walkCount += 1

            # to draw the hit box
            self.hitbox = (self.x + 10, self.y, 45, 60)  # so the hitbox will folow the player
            #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)  # the 2 is to make the box hollow

            #to draw the helth of the enemy
            pygame.draw.rect(screen, (255,0,0) ,(self.hitbox[0], self.hitbox[1] -10 ,50,8 ))
            pygame.draw.rect(screen, (0,255,0) ,(self.hitbox[0], self.hitbox[1] -10 ,50 - (5 * (10- self.health)),8 ))


            # to draw the explosion and make him stay for half of a second
            if self.hit_time and time.time() - self.hit_time < self.hit_duration:
                screen.blit(self.explosion_image, (self.x, self.y))

    def move(self):
        if self.vel > 0 :
            if self.x < self.path[1] + self.vel:  #so he wont go pass the end
                self.x += self.vel
            else:
                self.vel = self.vel * -1       #so if he gets to the end he will turn
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:   #same as the other one but to the other whey
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):       #what i want to do when the enemy get hit
        # to make a sound when a bullet hits
        hitSound = pygame.mixer.Sound("hit.mav")

        if self.visible: hitSound.play()

        self.hit_time = time.time()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        pygame.display.update()

