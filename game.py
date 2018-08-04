import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((383, 680))
pygame.display.set_caption('Animal Adventurers')

#lots of pre-code here

#colours
bgdColor = pygame.Color(199, 214, 149)
notAsLightGreenColor = pygame.Color(175, 198, 120)
MediumGreenColor = pygame.Color(77, 136, 72)
darkGreenColor = pygame.Color(31, 70, 26)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)

mousex, mousey = 0, 0

fontObj = pygame.font.SysFont("helveticaneue", 40)

msg = "Hi"

mainScreen = True

#pre-code finishes here

while True:
    windowSurfaceObj.fill(bgdColor)

    #if mainScreen == True:
        #do stuff for main screen here
    
    msgSurfaceObj = fontObj.render(msg, False, darkGreenColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (10, 20)
    windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif (event.type == MOUSEBUTTONDOWN):
            mousex, mousey = event.pos
            #if (event.button == 3):
                #insert code re: right click of button

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
        # may not need if don't use keyboard buttons

    pygame.display.update()
    fpsClock.tick(30)
