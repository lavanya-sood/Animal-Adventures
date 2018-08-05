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

def create_image_resize_button(icon,x,y,w,h):
    mouse = pygame.mouse.get_pos()

    active_click = 0

    imageSurfaceObj = pygame.image.load(icon)
    imageSurfaceObj = pygame.transform.scale(imageSurfaceObj,(w,h))
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
    #windowSurfaceObj.fill(bgdColor)
    
    question = "Where did you find it?"
    picture = pygame.image.load("frostpng.png")
    picture = pygame.transform.scale(picture, (280, 150))
    windowSurfaceObj.blit(picture,(50,50))

    p2 = pygame.image.load("frostpng.png")
    p2 = pygame.transform.scale(picture,(200,40))
    windowSurfaceObj.blit(p2,(30,220))

    im = pygame.image.load("Australian White Ibis.jpg")
    im = pygame.transform.scale(im,(280,150))
    windowSurfaceObj.blit(im,(50,50))

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
    #windowSurfaceObj.fill(bgdColor)
    head1 = "Let's"
    head2 = "Discuss"
    question = "What was it?"
    picture = pygame.image.load("frostpng.png")
    picture = pygame.transform.scale(picture, (280, 150))
    windowSurfaceObj.blit(picture,(50,50))

    p2 = pygame.image.load("frostpng.png")
    p2 = pygame.transform.scale(picture,(200,40))
    windowSurfaceObj.blit(p2,(30,220))

    im = pygame.image.load("Australian White Ibis.jpg")
    im = pygame.transform.scale(im,(280,150))
    windowSurfaceObj.blit(im,(50,50))

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
    #windowSurfaceObj.fill(bgdColor)
    
   
    question = "What color is it?"
    picture = pygame.image.load("frostpng.png")
    picture = pygame.transform.scale(picture, (280, 150))
    windowSurfaceObj.blit(picture,(50,50))


    p2 = pygame.image.load("frostpng.png")
    p2 = pygame.transform.scale(picture,(200,40))
    windowSurfaceObj.blit(p2,(30,220))

    im = pygame.image.load("Australian White Ibis.jpg")
    im = pygame.transform.scale(im,(280,150))
    windowSurfaceObj.blit(im,(50,50))

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
    picture = pygame.image.load("frostpng.png")
    picture = pygame.transform.scale(picture, (300, 650))
    windowSurfaceObj.blit(picture,(5,20))
    op1 = create_button("More..",100,250,150,50,darkGreenColor,babyPinkColor)
    #windowSurfaceObj.fill(bgdColor)
    im = pygame.image.load("Australian White Ibis.jpg")
    #im2 = pygame.image.load("Australian White Ibis.jpg")
    #im2 = pygame.transform.scale(im,(280,150))
    im = pygame.transform.scale(im,(300,200))
    windowSurfaceObj.blit(im,(50,50))
    create_text(fontHeadingObj,"Congrats!",20,300,blackColor)
    create_text(fontHeadingObj,"+100",80,400,darkBlueColor)
    create_text(fontSmallObj,"The illusive ibis is quiet a find!", 10,500,blackColor)
    create_text(fontSmallObj,"Commonly found in cities but its", 10,525,blackColor)
    create_text(fontSmallObj,"natural habitat are the wetlands.", 10,550,blackColor)
    create_text (fontSmallObj,"Try finding a photo of an Ibis in",10,580,darkBlueColor)
    create_text (fontSmallObj,"its natural habitat.",10,600,darkBlueColor)
    return op1

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
    #windowSurfaceObj.fill(bgdColor)
    soundIbis = 0
    
    p2 = pygame.image.load("frostpng.png")
    p2 = pygame.transform.scale(p2,(100,100))
    windowSurfaceObj.blit(p2,(110,240))

    create_text(fontHeadingObj,"Ibis",120,250,darkGreenColor)

    mouse = pygame.mouse.get_pos()

    ibisSurfaceObj = pygame.image.load("IbisBigReduced.png")
    windowSurfaceObj.blit(ibisSurfaceObj, (40,50))
    
    #w=283 h=197
    if 40+283 > mouse[0] > 40 and 50+197 > mouse[1] > 50:
        im = pygame.image.load("Australian White Ibis.jpg")
        im = pygame.transform.scale(im,(300,200))
        windowSurfaceObj.blit(im,(45,45))
        soundIbis = soundIbisGlobal
        if soundIbisGlobal == 0:
            ibisSoundObj.play()
            soundIbis = 1
        if passed_time == ibisSoundObj.get_length():
            soundIbis = 0
    else:
    	windowSurfaceObj.blit(ibisSurfaceObj, (40,50))

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
    mainButton = create_button("Go Back",200,620,150,50,darkGreenColor,darkBlueColor)
    return soundIbis,mainButton

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

ibisSoundObj = pygame.mixer.Sound('ibissoundfinal.wav')

soundIbisGlobal = 0
timer_started = 0
passed_time = 0

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
storage = False
main = False
d_screen = False

bg = pygame.image.load('leaf bg.jpg')

click = 0
active_click = 0

#pre-code finishes here

while True:
    windowSurfaceObj.fill(bgdColor)
    windowSurfaceObj.blit(bg, (0, 0))

    if mainScreen == True:
        #soundObj.play()
        sidebar = pygame.image.load("frostpng.png")
        windowSurfaceObj.blit(sidebar,(283,0))
        
        p3 = pygame.image.load("headingad.png")
        p3 = pygame.transform.scale(p3,(360,149))
        windowSurfaceObj.blit(p3,(6,10))

        p4 = pygame.image.load("game map.png")
        p4 = pygame.transform.scale(p4,(280,490))
        windowSurfaceObj.blit(p4,(10,180))

        p2 = pygame.image.load("frostpng.png")
        windowSurfaceObj.blit(p2,(0,590))

        p5 = pygame.image.load("koala.png")
        p5 = pygame.transform.scale(p5,(70,70))
        windowSurfaceObj.blit(p5,(298,400))

        p6 = pygame.image.load("cat.png")
        p6 = pygame.transform.scale(p6,(70,70))
        windowSurfaceObj.blit(p6,(298,300))

        p7 = pygame.image.load("pigeon.png")
        p7 = pygame.transform.scale(p7,(70,70))
        windowSurfaceObj.blit(p7,(298,200))
        
        #pygame.draw.rect(windowSurfaceObj, notAsLightGreenColor,
                       #  (283, 0, 100, 680))
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
        im = pygame.image.load("Australian White Ibis.jpg")
        im = pygame.transform.scale(im,(280,300))
        windowSurfaceObj.blit(im,(40,100))
        successful_click_photo_taken = create_button("Let's get some info",40,500,300,100,orangeColor,darkGreenColor)
        if successful_click_photo_taken == 1:
            q1_screen = True
            cameraScreen = False
            click = 0

    if storageScreen == True:
        p5 = pygame.image.load("koala.png")
        p5 = pygame.transform.scale(p5,(100,100))
        windowSurfaceObj.blit(p5,(150,25))

        p6 = pygame.image.load("cat.png")
        p6 = pygame.transform.scale(p6,(100,100))
        windowSurfaceObj.blit(p6,(275,25))

        p7 = pygame.image.load("pigeon.png")
        p7 = pygame.transform.scale(p7,(100,100))
        windowSurfaceObj.blit(p7,(25,150))

        p8 = pygame.image.load("curlew.png")
        p8 = pygame.transform.scale(p8,(100,100))
        windowSurfaceObj.blit(p8,(150,150))
        
        successful_click_ibis = create_image_resize_button('IbisSmall.png', 25, 25, 100, 100)
        if successful_click_ibis == 1:
            ibisFacts = True
            storage = True
            animal_screen = True
            storageScreen = False
            click = 0

    if animal_screen == True:
        soundIbisGlobal = information_screen()[0]
        mp =  information_screen()[1]
        if mp == 1:
            mainScreen = True
            animal_screen = False
            click = 0
        if soundIbisGlobal == 1 and timer_started == 0:
            start_time = pygame.time.get_ticks()
            timer_started = 1
        if timer_started == 1:
            passed_time = pygame.time.get_ticks() - start_time
        
        
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
            d_screen = True
            q3_screen = False
            q2_screen = False
            q1_screen = False
            click = 0
    
    if d_screen == True:
        stat = done_screen()
        if stat == 1:
            animal_screen = True
            d_screen = False
            click = 0
        
        
    
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
            elif (event.button == 4): #scroll down
                if main == True:
                    mainScreen = True
                    animal_screen = False
                elif storage == True:
                    storageScreen = True
                    animal_screen = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

        #cameraButton.event_handler(event)
        # may not need if don't use keyboard buttons

    pygame.display.update()
    fpsClock.tick(30)
