import pygame
import random
import time
 
# Define some colors
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (51, 153, 255)
NOTASLIGHTBLUE = (0, 110, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1000, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chase!")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#setup

# -------- Setup Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    # background image.
    screen.fill(LIGHTBLUE)
    
    # --- Game logic should go here
    #Code that detects the mouse
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    startfont = pygame.font.SysFont('Calibri', 20, True, False)
    humantext = startfont.render("("+str(mouseX)+","+str(mouseY)+")",True,RED)
    screen.blit(humantext, [220, 500])

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, NOTASLIGHTBLUE, [(20,20),(200, 560)])
    pygame.draw.rect(screen, GREY, [(20,20),(200, 560)], 5)

    startfont = pygame.font.SysFont('Calibri', 180, True, False)
    humantext = startfont.render("RACER",True,RED)
    screen.blit(humantext, [220, 0])
    
    startfont = pygame.font.SysFont('Calibri', 50, True, False)
    humantext = startfont.render("Ur a",True,RED)
    screen.blit(humantext, [725, 15])
    humantext = startfont.render("Square",True,RED)
    screen.blit(humantext, [725, 50])
    humantext = startfont.render("Beware",True,RED)
    screen.blit(humantext, [725, 80])

    #pygame.draw.line(screen, RED, [720, 25], [720, 135], 10)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            #pygame.quit()
    # --- Game logic should go here

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
