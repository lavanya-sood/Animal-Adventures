import pygame, sys
from pygame.locals import *

def create_button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    active_click = 0
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(windowSurfaceObj, ac,(x,y,w,h))
        if click == 1:
            active_click = 1
    else:
        pygame.draw.rect(windowSurfaceObj, ic,(x,y,w,h))

    textSurf = fontSmallObj.render(msg, False, whiteColor)
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)),(y+(h/2)) )
    windowSurfaceObj.blit(textSurf, textRect)

    return active_click

def create_image_button(icon,x,y,w,h):
    mouse = pygame.mouse.get_pos()

    active_click = 0

    imageSurfaceObj = pygame.image.load(icon)
    windowSurfaceObj.blit(imageSurfaceObj, (x, y))
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y and click == 1:
        active_click = 1

    return active_click

def create_text(size,msg,x,y,color):
    textSurfaceObj = size.render(msg, False, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (x, y)
    windowSurfaceObj.blit(textSurfaceObj, textRectObj)

def question1_screen():
    windowSurfaceObj.fill(bgdColor)
    head1 = "Let's"
    head2 = "Discuss"
    question = "Where did you find it?"
    create_text(fontHeadingObj,head1,80,50,darkGreenColor)
    create_text(fontHeadingObj,head2,50,120,darkGreenColor)
    create_text(fontMediumObj,question,40,230,darkGreenColor)
    op1 = create_button("Water",40,300,300,100,darkGreenColor,lightBlueColor)
    op2 = create_button("Land",40,430,300,100,darkGreenColor,orangeColor)
    op3 = create_button("Air",40,560,300,100,darkGreenColor,darkBlueColor)
    random = 0

    if op1 == 1:
        #print("op1")
        return op1
    elif op2 == 1:
        #print("op2")
        return op2
    elif op3 == 1:
        #print("op3")
        return op3
    else:
        #print("op4")
        return random

def question2_screen():
    windowSurfaceObj.fill(bgdColor)
    head1 = "Let's"
    head2 = "Discuss"
    question = "What was it?"
    create_text(fontHeadingObj,head1,80,50,darkGreenColor)
    create_text(fontHeadingObj,head2,50,120,darkGreenColor)
    create_text(fontMediumObj,question,40,230,darkGreenColor)
    op1 = create_button("Mammal",40,300,300,50,darkGreenColor,babyPinkColor)
    op2 = create_button("Bird",40,400,300,50,darkGreenColor,orangeColor)
    op3 = create_button("Fish",40,500,300,50,darkGreenColor,yellowColor)
    op4 = create_button("Reptile",40,600,300,50,darkGreenColor,darkBlueColor)

    if op1 == 1:
        return op1
    elif op2 == 1:
        return op2
    elif op3 == 1:
        return op3
    elif op4 == 1:
        return op4

def question3_screen():
    windowSurfaceObj.fill(bgdColor)
    head1 = "Let's"
    head2 = "Discuss"
    question = "What color is it?"
    create_text(fontHeadingObj,head1,80,50,darkGreenColor)
    create_text(fontHeadingObj,head2,50,120,darkGreenColor)
    create_text(fontMediumObj,question,40,230,darkGreenColor)
    op1 = create_button("Brown",40,300,150,50,darkGreenColor,babyPinkColor)
    op2 = create_button("Black",40,400,150,50,darkGreenColor,orangeColor)
    op3 = create_button("White",40,500,150,50,darkGreenColor,yellowColor)
    op4 = create_button("Green",200,300,150,50,darkGreenColor,darkBlueColor)
    op5 = create_button("Peach",200,400,150,50,darkGreenColor,darkBlueColor)
    op6 = create_button("Grey",200,500,150,50,darkGreenColor,darkBlueColor)

    if op1 == 1:
        return op1
    elif op2 == 1:
        return op2
    elif op3 == 1:
        return op3
    elif op4 == 1:
        return op4
    elif op5 == 1:
        return op5
    elif op6 == 1:
        return op6
    else:
        return 0

def done_screen():
    windowSurfaceObj.fill(bgdColor)
    create_text(fontHeadingObj,"Thanks",80,50,darkBlueColor)

#animals = ['Ibis', 'Cat', 'Dog', 'Horse', 'Possum', 'Fish', 'Curlew']
ultimoLocal = ['Ibis', 'Pigeon', 'Dog']
test = {'name': 'Australian White Ibis',
        'location': 'Eastern, Northern and South-Western Australia',
        'funFact': 'While ibises, who are waterbirds, generally live in wetland areas, droughts have meant that ibises now prefer more city based areas with lots of food and water in easy access.'}
curlew = {'name': 'Bush-Stone Curlew',
          'location': 'Brisbane, Cairns and Townsville, in greener areas',
          'funFact': "While the curlew may look cute, its bird call can be horrifying to hear. Beware: some say it sounds like a person screaming!"}

ibis = {'Scientific Name': 'Australian White Ibis', 'Common Name' : 'Bin Chicken',
        'Location': 'Australia', 'Color': 'White'
        }

def information_screen():
    windowSurfaceObj.fill(bgdColor)
    ibisSurfaceObj = pygame.image.load("IbisBigReduced.png")
    windowSurfaceObj.blit(ibisSurfaceObj, (40,50))
    create_text(fontHeadingObj,"Ibis",120,250,darkGreenColor)
    m = 400
    n = 380
    o = 375
    for i in ibis:
        pygame.draw.rect(windowSurfaceObj, lightboxColor,(30,o,230,47))
        create_text(fontSmallObj,i,40,n,orangeColor)
        create_text(fontSmallObj,ibis[i],40,m,darkBlueColor)

        m +=  70
        n += 70
        o += 70

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((383, 680))
pygame.display.set_caption('Animal Adventurers')

#lots of pre-code here

#images
#starSurfaceObj = pygame.image.load('gold-star-sticker-clipart-1.png')

#colours
bgdColor = pygame.Color(199, 214, 149)
notAsLightGreenColor = pygame.Color(175, 198, 120)
MediumGreenColor = pygame.Color(77, 136, 72)
darkGreenColor = pygame.Color(31, 70, 26)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
lightBlueColor = pygame.Color(139, 167, 211)
darkBlueColor = pygame.Color(28, 97, 206)
orangeColor = pygame.Color(206, 128, 28)
babyPinkColor = pygame.Color(224, 134, 212)
yellowColor = pygame.Color(234, 193, 11)
lightRedColor = pygame.Color(226, 108, 112)
lightboxColor = pygame.Color(242, 247, 242)

mousex, mousey = 0, 0

#fonts
fontHeadingObj = pygame.font.SysFont("helveticaneue", 100)
fontMediumObj = pygame.font.SysFont("helveticaneue", 40)
fontSmallObj = pygame.font.SysFont("helveticaneue", 30)

mainScreen = True
storageScreen = False
cameraScreen = False
whatIsAnimalScreen = False
searchAnimalScreen = False
questionAnimalSearchScreen = False
genericTemplateScreen = False
q1_screen = False
q2_screen = False
q3_screen = False
welcome_screen = False
animal_screen = False

click = 0
#active_click = 0

#pre-code finishes here

while True:
    windowSurfaceObj.fill(bgdColor)

    if mainScreen == True:
        pygame.draw.rect(windowSurfaceObj, notAsLightGreenColor,
                         (283, 0, 100, 680))
        successful_click_collection = create_image_button('gold-star-sticker-clipart-1.png', 298, 595, 70, 70)
        if successful_click_collection == 1:
            storageScreen = True
            mainScreen = False
            click = 0
        successful_click_camera = create_image_button('camera.png', 156.5, 595, 70, 70)
        if successful_click_camera == 1:
            cameraScreen = True
            mainScreen = False
            click = 0
        if 'Ibis' in ultimoLocal:
            successful_click_ibis = create_image_button('IbisSmallReduced.png', 298, 510, 70, 70)
            if successful_click_ibis == 1:
                ibisFacts = True
                animal_screen = True
                mainScreen = False
                click = 0

    if cameraScreen == True:
        successful_click_photo_taken = create_image_button('camera.png', 156.5, 595, 70, 70)
        if successful_click_photo_taken == 1:
            whatIsAnimalScreen = True
            cameraScreen = False
            click = 0

    if whatIsAnimalScreen == True:
        successful_click_finding_animal = create_button("",156.5,595,70,70,MediumGreenColor,darkGreenColor)
        if successful_click_finding_animal == 1:
            q1_screen = True
            whatIsAnimalScreen = False
            click = 0

    if storageScreen == True:
        successful_click_ibis = create_image_button('IbisSmallReduced.png', 50, 50, 70, 70)
        if successful_click_ibis == 1:
            ibisFacts = True
            animal_screen = True
            storageScreen = False
            click = 0

    if animal_screen == True:
        information_screen()
        
    if q1_screen == True:
        stat = question1_screen()
        if stat == 1:
            q2_screen = True
            q1_screen = False
            q3_screen = False
            click = 0

    if q2_screen == True:
        stat = question2_screen()
        if stat == 1:
            q2_screen = False
            q3_screen = True
            q1_screen = False
            click = 0

    if q3_screen == True:
        stat = question3_screen()
        if stat == 1:
            welcome_screen = True
            q3_screen = False
            q2_screen = False
            q1_screen = False
            click = 0
    
    if welcome_screen == True:
        done_screen()
    
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
            if (event.button == 1):
                click = 1
        elif (event.type == MOUSEBUTTONUP):
            mousex, mousey = event.pos
            if (event.button == 1):
                click = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

        #cameraButton.event_handler(event)
        # may not need if don't use keyboard buttons

    pygame.display.update()
    fpsClock.tick(30)
