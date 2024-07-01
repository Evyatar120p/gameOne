import pygame
from Enemy import enemy
from Projectile import projectile
from PlayerOne import player

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 560

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))       #to set  the screen

pygame.display.set_caption("First game") #to give a name to the screen

bg = pygame.image.load('bg.jpg')   # the bg image

fps = pygame.time.Clock()  #so the game will have fps

damage = 0   #so we can track how many times the enemy got hit
score = 0 # so we can track how mant time i killes the enemy

#to make a sound when i fire a bullet
bulletSound = pygame.mixer.Sound("bullet.mav")


#to music play while the game is on
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1) #-1 so it will play all the time

#elad


def draw_game():
    screen.blit(bg, (0,0))         # do make the screen be a pic and where tou want it to be in the screen
    david.draw(screen)                  #to call the draw function in the class
    lior.draw(screen)

    #to draw the text
    text_damage = font.render("damage: " + str(damage), 1, (255, 0, 0))  # Arguments are: text, anti-aliasing, color
    text_score = font.render("score: " + str(score), 1, (255, 0, 0))  # Arguments are: text, anti-aliasing, color
    screen.blit(text_damage, (10, 10))
    screen.blit(text_score, (10, 50))

    #drawing the bullets
    #drawing the bullets
    for bullet in bullets:
        bullet.draw(screen)         # fo draw all the bullets

    pygame.display.update()             #to make the screen update every time

#to creat the charectors
david = player(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 70,64,64)
lior = enemy(0, 495 , 64 , 64, 1000-64)
shootOne = 0
bullets = []
font = pygame.font.SysFont("comicsans", 30, True) #to make the font of the things i write in the game


# this is the main loop
run = True
while run:
    fps.tick(27)


    #so we shoot one bullet at the time (it makes a time delay)
    if shootOne > 0:
        shootOne += 1
    if shootOne > 10:
        shootOne = 0


    for event in pygame.event.get():              #to make the screen stay on , its making a list of every thing you do and checks if you press quit
        if event.type == pygame.QUIT:
            run = False


    if lior.visible :   # so we will hit him inly when he is alive
        # to check if the player hit the enemy
        if david.hitbox[1] < lior.hitbox[1] + lior.hitbox[3] and david.hitbox[1] + david.hitbox[3] > lior.hitbox[1]: # y axis
            if david.hitbox[0] + david.hitbox[2] > lior.hitbox[0] and david.hitbox[0] < lior.hitbox[0] + lior.hitbox[2]: # x axis
                david.hit(screen)
                score -= 2


        # to make the enemy get hit br a bullet
    for bullet in bullets:
        if bullet.y - bullet.radius <lior.hitbox[1] + lior.hitbox[3] and bullet.y + bullet.radius > lior.hitbox[1]:  #to chck if the bolets are in the enemy hit box on the y axis
            if bullet.x + bullet.radius > lior.hitbox[0] and bullet.x - bullet.radius < lior.hitbox[0] + lior.hitbox[2]:  #to chck if the bolets are in the enemy hit box on the x axis
                lior.hit()
                if lior.visible: damage += 1
                if damage % 10 == 0 and lior.visible:
                    score +=1
                if lior.visible: bullets.pop(bullets.index(bullet))


        if bullet.x < 1000 and bullet.x > 0: #so if they leave the screen i they will be deleted
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))



    #the folowing lines are to make the character move       +       the and part is so the characyer wont go off the screen
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and shootOne == 0:
        bulletSound.play()
        if david.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:     #so there will be only 5 at a time
            bullets.append(projectile(round(david.x + david.width //2) , round(david.y + david.height//2), 5, (250,250,250) , facing))  #making a bullet
            shootOne = 1


    if key[pygame.K_RIGHT] and david.x < SCREEN_WIDTH - david.width :  #to move right
        david.x += david.player_vel
        david.left = False
        david.right = True
        david.standig = False


    elif key[pygame.K_LEFT] and david.x > david.player_vel:  #to move left
        david.x -= david.player_vel
        david.left = True
        david.right = False
        david.standig = False

    else:
        david.standig = True
        david.walkCount = 0


    if not(david.is_jump):    # we don't want to make the character move up and down while jumping
        if key[pygame.K_UP]:
            david.is_jump = True
            david.right = False
            david.left = False
            david.walkCount = 0


    else:     # to make thw character jump
        if david.jumpCount >= -10:
            neg = 1
            if david.jumpCount < 0:
                neg = -1
            david.y -= (david.jumpCount ** 2) *0.5 * neg
            david.jumpCount -= 1
        else:
            david.is_jump = False
            david.jumpCount = 10


    draw_game()


pygame.quit()