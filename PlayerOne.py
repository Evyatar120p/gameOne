import pygame

class player(object):

    # This is lists of all the images in the file

    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
                 pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
                 pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
                pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
                pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    char = pygame.image.load('standing.png')

    def __init__(self , x , y , width , height ):
        # for the charactor size
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.player_vel = 8

        # for the jumpung part
        self.is_jump = False
        self.jumpCount = 10

        # for the charactor movment
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standig = True

        #to make a hitbox:
        self.hitbox =  (self.x + 10 , self.y ,35 , 60)  #(x,y, width , hight)

    def draw(self,screen):
        # the following lines are to make the charactoer walk

        if self.walkCount + 1 >= 27:  # This is because we have 9 images and each one will run for 3 frames ( 9 * 3 = 27 )
            self.walkCount = 0

        if not(self.standig):
            if self.left:    #to make him look like he is going
                screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:               #we make to that he will stay facing the last direction he faced
            if self.right:
                screen.blit(self.walkRight[0] , (self.x, self.y))
            else:
                screen.blit(self.walkLeft[0] , (self.x, self.y))

        #to draw the hit box
        self.hitbox =  (self.x + 10 , self.y + 5 ,40 , 60)  # so the hitbox will folow the player
        #pygame.draw.rect(screen, (255,0,0) ,self.hitbox,2 ) # the 2 is to make the box hollow


    def hit(self,screen):
        score_down = self.x
        if self.x > 500:
            self.x = 0
        else:
            self.x = 930  # We are resetting the player position
        self.walkCount = 0

        font1 = pygame.font.SysFont('comicsans', 50)
        text = font1.render('-4 ', 1, (255, 0, 0))
        screen.blit(text, (score_down, 400))
        pygame.display.update()
        i = 0
        while i < 50:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

