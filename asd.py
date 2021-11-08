import pygame, sys, random
from pygame import mixer
clock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()
myfont = pygame.font.SysFont('', 120)
textsurface = myfont.render('0', False, (255, 255, 255))
pontszamlalo = myfont.render('0', False, (255, 255, 255))

Hframe = 0
Rframe = 0
hatter_anim = [pygame.image.load('IKT starwars/háttér/Háttérkép.png'), pygame.image.load('IKT starwars/háttér/Háttérkép1.png'), pygame.image.load('IKT starwars/háttér/Háttérkép2.png'), pygame.image.load('IKT starwars/háttér/Háttérkép3.png'), pygame.image.load('IKT starwars/háttér/Háttérkép4.png'), pygame.image.load('IKT starwars/háttér/Háttérkép5.png'), pygame.image.load('IKT starwars/háttér/Háttérkép6.png'), pygame.image.load('IKT starwars/háttér/Háttérkép7.png'), pygame.image.load('IKT starwars/háttér/Háttérkép8.png'), pygame.image.load('IKT starwars/háttér/Háttérkép9.png'), pygame.image.load('IKT starwars/háttér/Háttérkép10.png'), pygame.image.load('IKT starwars/háttér/Háttérkép11.png'), pygame.image.load('IKT starwars/háttér/Háttérkép12.png'), pygame.image.load('IKT starwars/háttér/Háttérkép13.png'), pygame.image.load('IKT starwars/háttér/Háttérkép14.png'), pygame.image.load('IKT starwars/háttér/Háttérkép15.png'), pygame.image.load('IKT starwars/háttér/Háttérkép16.png'), pygame.image.load('IKT starwars/háttér/Háttérkép17.png'), pygame.image.load('IKT starwars/háttér/Háttérkép18.png'), pygame.image.load('IKT starwars/háttér/Háttérkép19.png'), pygame.image.load('IKT starwars/háttér/Háttérkép20.png'), pygame.image.load('IKT starwars/háttér/Háttérkép21.png')]
robbans_anim = [pygame.image.load('robbanás/robbanás0.png'), pygame.image.load('robbanás/robbanás1.png'), pygame.image.load('robbanás/robbanés2.png'), pygame.image.load('robbanás/robbanás3.png'), pygame.image.load('robbanás/robbanás4.png'), pygame.image.load('robbanás/robbanás5.png')]

meteor0 = pygame.transform.scale(pygame.image.load('meteor/meteor0.png'), (128, 128))
meteor1 = pygame.transform.scale(pygame.image.load('meteor/meteor1.png'), (110, 110))
meteor2 = pygame.transform.scale(pygame.image.load('meteor/meteor2.png'), (140, 140))
meteor3 = pygame.transform.scale(pygame.image.load('meteor/meteor3.png'), (128, 128))

abl_meret = (1920, 1080)
hatter = pygame.image.load('IKT starwars/háttér/háttér.gif')
abl = pygame.display.set_mode(abl_meret, 0, 32)

urhajo = pygame.transform.scale(pygame.image.load('urhajo.png'), (300, 96))
urhajo_hely = [20, (abl.get_height()-urhajo.get_height())/2]

urhajo_rect = pygame.Rect(urhajo_hely[0], urhajo_hely[1], urhajo.get_width(), urhajo.get_height()/2)
szamlalo = 0

lovedek_kep = pygame.image.load('lovedek.png')
lovedek0_hely = [urhajo_hely[0] + 200, urhajo_hely[1] + 2]
lovedek0_rect = pygame.Rect(lovedek0_hely[0], lovedek0_hely[1], lovedek_kep.get_width(), lovedek_kep.get_height())
lovedek1_hely = [urhajo_hely[0] + 200, urhajo_hely[1] + 83]
lovedek1_rect = pygame.Rect(lovedek1_hely[0], lovedek1_hely[1], lovedek_kep.get_width(), lovedek_kep.get_height())

fel = False
le = False
jobbra = False
balra = False
robbanas = False
loves = False
meteor_mozgas = True
urhajo_mozgas = True
hatter_mozgas = True
kijelzo_szoveg = True
folyamatos = False
eletero = 3
pont = 0

bossEletero = 100
sebzes = 1
bossHSebzes = 3

j_ido = 0
varakozas = 0
a = 0

Kilep = myfont.render('asd', False, (60, 10, 60))
Kilep_ = False
robbanas_hang = pygame.mixer.Sound("mixkit-8-bit-bomb-explosion-2811.wav")
gyogyitas_hang = pygame.mixer.Sound("mixkit-retro-game-notification-212.wav")
loves_hang = pygame.mixer.Sound("mixkit-game-whip-shot-1512.wav")
halal_hang = pygame.mixer.Sound('halal.wav')

gyogyitas_kep = pygame.transform.scale(pygame.image.load('hp.png'), (96, 96))
gyogyitas_rect = pygame.Rect(0, 0, gyogyitas_kep.get_width(), gyogyitas_kep.get_height())
Rfolyamatos = False

RobbanasHely = [urhajo_hely[0] + urhajo.get_width(), urhajo_hely[1]]
loves_ = True

def Hanimacio(hatter_anim):
    global Hframe
    if Hframe >= 84:
        Hframe = 0
    if hatter_mozgas:
        abl.blit(pygame.transform.scale((hatter_anim[Hframe//4]), (abl.get_width(), abl.get_height())), (0,0))
        Hframe += 1


def urhajoKep():
    abl.blit(urhajo, urhajo_hely)


def randomY():
    randY = random.randint(0, abl.get_height()-meteor2.get_height())
    return randY


def randomMeteor():
    randM = random.randint(0, 3)
    if randM == 0:
        return meteor0
    elif randM == 1:
        return meteor1
    else:
        return meteor2


def randTavolsag():
    RT = random.randint(0, 1500)
    return  RT

def Ranimacio():
    global Rframe
    global Rfolyamatos
    global a
    global RobbanasHely
    if Rframe >= 12:
        Rframe = 0
        Rfolyamatos = False
        a = 0

    if Rfolyamatos:
        if a == 0:
            if urhajo_rect.colliderect(meteor0_rect):
                RobbanasHely = [urhajo_hely[0] + urhajo.get_width(), urhajo_hely[1]]
            if urhajo_rect.colliderect(meteor1_rect):
                RobbanasHely = [urhajo_hely[0] + urhajo.get_width(), urhajo_hely[1]]
            if urhajo_rect.colliderect(meteor2_rect):
                RobbanasHely = [urhajo_hely[0] + urhajo.get_width(), urhajo_hely[1]]
            if urhajo_rect.colliderect(meteor3_rect):
                RobbanasHely = [urhajo_hely[0] + urhajo.get_width(), urhajo_hely[1]]

            a += 1
        abl.blit(pygame.transform.scale(robbans_anim[Rframe // 2], (150, 150)), RobbanasHely)
        Rframe += 1

def UHloves():
    global folyamatos
    if loves:
        folyamatos = True

    if folyamatos:
        lovedek0_rect.x += 100
        lovedek1_rect.x += 100
        abl.blit(lovedek_kep, lovedek0_hely)
        abl.blit(lovedek_kep, lovedek1_hely)
    else:
        lovedek0_rect.x = urhajo_hely[0] + 200
        lovedek0_rect.y = urhajo_hely[1] + 2
        lovedek1_rect.x = urhajo_hely[0] + 200
        lovedek1_rect.y = urhajo_hely[1] + 83

    if lovedek1_rect.colliderect(meteor0_rect) or lovedek0_rect.colliderect(meteor0_rect):
        folyamatos = False
    if lovedek1_rect.colliderect(meteor1_rect) or lovedek0_rect.colliderect(meteor1_rect):
        folyamatos = False
    if lovedek1_rect.colliderect(meteor2_rect) or lovedek0_rect.colliderect(meteor2_rect):
        folyamatos = False
    if lovedek1_rect.colliderect(meteor3_rect) or lovedek0_rect.colliderect(meteor3_rect):
        folyamatos = False

    if lovedek0_rect.x > abl.get_width():
        folyamatos = False



meteor0_hely = [abl.get_width() + randTavolsag(), randomY()]
meteor1_hely = [abl.get_width() + randTavolsag(), randomY()]
meteor2_hely = [abl.get_width() + randTavolsag(), randomY()]
meteor3_hely = [abl.get_width() + randTavolsag(), randomY()]

meteor0_rect = pygame.Rect(meteor0_hely[0], meteor0_hely[1], meteor0.get_width(), meteor0.get_height())
meteor1_rect = pygame.Rect(meteor1_hely[0], meteor1_hely[1], meteor1.get_width(), meteor1.get_height())
meteor2_rect = pygame.Rect(meteor2_hely[0], meteor2_hely[1], meteor2.get_width(), meteor2.get_height())
meteor3_rect = pygame.Rect(meteor3_hely[0], meteor3_hely[1], meteor3.get_width(), meteor3.get_height())

gyogyitas_hely = [abl.get_width() + randTavolsag(), randomY()]

pygame.mixer.music.load("Háttérhang.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1, 0.0)

menu = pygame.Surface((1920, 1080))
tart = 1
while True:
    if tart%2 == 0:
        abl.blit(menu, (0, 0))
        menu.fill((20,0,20))
    else:
        abl.fill((0, 0, 0))

        if not (hatter_mozgas):
            abl.blit(pygame.transform.scale((hatter_anim[Hframe // 4]), (abl.get_width(), abl.get_height())), (0, 0))

        Hanimacio(hatter_anim)
        #pygame.draw.rect(abl, (255, 255, 255), urhajo_rect, 2)
        #pygame.draw.rect(abl, (255, 255, 255), meteor0_rect, 2)
        #pygame.draw.rect(abl, (255, 255, 255), meteor1_rect, 2)
        #pygame.draw.rect(abl, (255, 255, 255), meteor2_rect, 2)
        #pygame.draw.rect(abl, (255, 255, 255), meteor3_rect, 2)
        #pygame.draw.rect(abl, (255, 255, 255), lovedek0_rect, 2)
        #pygame.draw.rect(abl, (255, 255, 255), lovedek1_rect, 2)
        #pygame.draw.rect(abl, (255, 255, 255), gyogyitas_rect, 2)
        urhajoKep()
        abl.blit(meteor0, meteor0_hely)
        abl.blit(meteor1, meteor1_hely)
        abl.blit(meteor2, meteor2_hely)
        abl.blit(meteor3, meteor3_hely)
        abl.blit(gyogyitas_kep, gyogyitas_hely)
        Ranimacio()


    j_ido = pygame.time.get_ticks()

    if kijelzo_szoveg:
        abl.blit(textsurface, (0, 0))
        abl.blit(pontszamlalo, (abl.get_width()-pontszamlalo.get_width(), 0))
    else:
        textsurface = myfont.render('MEGHALTÁL', False, (255, 255, 255))
        abl.blit(textsurface, ((abl.get_width()-textsurface.get_width()) /2, (abl.get_height()-textsurface.get_height())/2))
        abl.blit(pontszamlalo, ((abl.get_width()-textsurface.get_width()) /2, (abl.get_height()-textsurface.get_height())))

    if meteor_mozgas:
        if meteor0_hely[0] > -1*(meteor0.get_width()):
            meteor0_hely[0] -= 30
        else:
            meteor0_hely[0] = abl.get_width() + randTavolsag()
            meteor0_hely[1] = randomY()

        if meteor1_hely[0] > -1*(meteor1.get_width()):
            meteor1_hely[0] -= 30
        else:
            meteor1_hely[0] = abl.get_width() + randTavolsag()
            meteor1_hely[1] = randomY()

        if meteor2_hely[0] > -1*(meteor2.get_width()):
            meteor2_hely[0] -= 30
        else:
            meteor2_hely[0] = abl.get_width() + randTavolsag()
            meteor2_hely[1] = randomY()

        if meteor3_hely[0] > -1*(meteor3.get_width()):
            meteor3_hely[0] -= 30
        else:
            meteor3_hely[0] = abl.get_width() + randTavolsag()
            meteor3_hely[1] = randomY()

        if gyogyitas_hely[0] > -1 * (gyogyitas_kep.get_width()):
            gyogyitas_hely[0] -= 30
        else:
            gyogyitas_hely[0] = 50000
            gyogyitas_hely[1] = randomY()

    urhajo_rect.x = urhajo_hely[0]
    urhajo_rect.y = urhajo_hely[1] + urhajo.get_height()/4
    meteor0_rect.x = meteor0_hely[0]
    meteor0_rect.y = meteor0_hely[1]
    meteor1_rect.x = meteor1_hely[0]
    meteor1_rect.y = meteor1_hely[1]
    meteor2_rect.x = meteor2_hely[0]
    meteor2_rect.y = meteor2_hely[1]
    meteor3_rect.x = meteor3_hely[0]
    meteor3_rect.y = meteor3_hely[1]
    gyogyitas_rect.x = gyogyitas_hely[0]
    gyogyitas_rect.y = gyogyitas_hely[1]

    if urhajo_rect.colliderect(meteor0_rect):
        meteor0_hely[0] = abl.get_width() + randTavolsag()
        meteor0_hely[1] = randomY()
        eletero -= 1
        robbanas_hang.play()
        Rfolyamatos = True
        meteor_hely = meteor0_hely

    if urhajo_rect.colliderect(meteor1_rect):
        meteor1_hely[0] = abl.get_width() + randTavolsag()
        meteor1_hely[1] = randomY()
        eletero -= 1
        robbanas_hang.play()
        Rfolyamatos = True
        meteor_hely = meteor1_hely

    if urhajo_rect.colliderect(meteor2_rect):
        meteor2_hely[0] = abl.get_width() + randTavolsag()
        meteor2_hely[1] = randomY()
        eletero -= 1
        robbanas_hang.play()
        Rfolyamatos = True
        meteor_hely = meteor2_hely

    if urhajo_rect.colliderect(meteor3_rect):
        meteor3_hely[0] = abl.get_width() + randTavolsag()
        meteor3_hely[1] = randomY()
        eletero -= 1
        robbanas_hang.play()
        Rfolyamatos = True
        meteor_hely = meteor3_hely

    if urhajo_rect.colliderect(gyogyitas_rect):
        eletero += 1
        gyogyitas_hely[0] = 50000
        gyogyitas_hely[1] = randomY()
        gyogyitas_hang.play()

    if lovedek1_rect.colliderect(meteor0_rect) or lovedek0_rect.colliderect(meteor0_rect):
        meteor0_hely[0] = abl.get_width() + randTavolsag()
        meteor0_hely[1] = randomY()
        pont += 10
        robbanas_hang.play()
        meteor_hely = meteor0_hely

    if lovedek1_rect.colliderect(meteor1_rect) or lovedek0_rect.colliderect(meteor1_rect):
        meteor1_hely[0] = abl.get_width() + randTavolsag()
        meteor1_hely[1] = randomY()
        pont += 10
        robbanas_hang.play()
        meteor_hely = meteor1_hely

    if lovedek1_rect.colliderect(meteor2_rect) or lovedek0_rect.colliderect(meteor2_rect):
        meteor2_hely[0] = abl.get_width() + randTavolsag()
        meteor2_hely[1] = randomY()
        pont += 10
        robbanas_hang.play()
        meteor_hely = meteor2_hely

    if lovedek1_rect.colliderect(meteor3_rect) or lovedek0_rect.colliderect(meteor3_rect):
        meteor3_hely[0] = abl.get_width() + randTavolsag()
        meteor3_hely[1] = randomY()
        pont += 10
        robbanas_hang.play()
        meteor_hely = meteor3_hely

    if eletero <= 0:
        meteor_mozgas = False
        urhajo_mozgas = False
        hatter_mozgas = False
        kijelzo_szoveg = False
        loves_ = False
        egyszer = 0
        mixer.music.stop()

    if urhajo_mozgas:
        if jobbra:
            urhajo_hely[0] += 30
        if balra:
            urhajo_hely[0] -= 30
        if fel:
            urhajo_hely[1] -= 30
        if le:
            urhajo_hely[1] += 30

    if urhajo_hely[1] > abl_meret[1] - urhajo.get_height():
        urhajo_hely[1] = 0

    if urhajo_hely[1] < 0:
        urhajo_hely[1] = abl_meret[1] - urhajo.get_height()

    if urhajo_hely[0] > abl_meret[0] - urhajo.get_width():
        urhajo_hely[0] = 0

    if urhajo_hely[0] < 0:
        urhajo_hely[0] = abl_meret[0] - urhajo.get_width()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                tart += 1
                if tart%2 == 0:
                    meteor_mozgas = False
                    urhajo_mozgas = False
                    hatter_mozgas = False
                    loves_ = False
                    mixer.music.pause()
                    menu.fill((50, 50, 50))
                    Kilep = myfont.render('Kilépés', False, (80, 20, 160))
                    abl.blit(Kilep, ((450 - Kilep.get_width()) / 2, 650))

                else:
                    meteor_mozgas = True
                    urhajo_mozgas = True
                    hatter_mozgas = True
                    mixer.music.unpause()
                    loves_ = True


            if event.key == K_d:
                jobbra = True

            if event.key == K_a:
                balra = True

            if event.key == K_w:
                fel = True

            if event.key == K_s:
                le = True

            if loves_:
                if event.key == K_SPACE:
                    loves = True
                    if lovedek0_rect.x == urhajo_hely[0] + 200:
                        loves_hang.play()

        if event.type == KEYUP:
            if event.key == K_d:
                jobbra = False

            if event.key == K_a:
                balra = False

            if event.key == K_w:
                fel = False

            if event.key == K_s:
                le = False

            if event.key == K_SPACE:
                loves = False

    lovedek1_hely = (lovedek1_rect.x, lovedek1_rect.y)
    lovedek0_hely = (lovedek0_rect.x, lovedek0_rect.y)
    UHloves()
    textsurface = myfont.render('Életerő: ' + str(eletero), False, (255, 255, 255))
    pontszamlalo = myfont.render('Pontszám: ' + str(pont), False, (255, 255, 255))
    pygame.display.update()
    clock.tick(60)
