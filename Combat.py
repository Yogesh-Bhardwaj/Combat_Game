import pygame
import random
import os
pygame.init()
W=1300
H=655
gameWindow=pygame.display.set_mode((W,H))
pygame.display.set_caption("Combat")

bgimg=pygame.image.load("Components\Background.jpg").convert_alpha()
bgimg=pygame.transform.scale(bgimg,(W,H)).convert_alpha()

pltfrm=pygame.image.load("Components\Platform.png").convert_alpha()
pltfrm=pygame.transform.scale(pltfrm,(int(1.2*W),int(pltfrm.get_height()/4))).convert_alpha()

P=pygame.image.load("Components\A1.png").convert_alpha()
O=pygame.image.load("Components\A2.png").convert_alpha()

arrow=pygame.image.load("Components\Arrow.png").convert_alpha()
arrow_left=pygame.image.load("Components\Arrow_left.png").convert_alpha()

P=pygame.transform.rotozoom(P,0,0.45)
O=pygame.transform.rotozoom(O,0,0.45)

parr=pygame.transform.rotozoom(arrow,0,0.09)
parr_left = pygame.transform.rotozoom(arrow_left,30,0.06)
oarr=pygame.transform.rotozoom(arrow,180,0.09)

h=P.get_height()
w=P.get_width()

warr=parr.get_width()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,int(H/10))
fps=50

def cut_sound1(sound):
    raw_array = sound.get_raw()
    raw_array = raw_array[10:10000]
    cut_sound = pygame.mixer.Sound(buffer=raw_array)
    return cut_sound

def cut_sound2(sound):
    raw_array = sound.get_raw()
    raw_array = raw_array[20000:40000]
    cut_sound = pygame.mixer.Sound(buffer=raw_array)
    return cut_sound

pygame.mixer.music.load("Sounds\dcpoke__birds-singing-03.mp3")
arrow_shoot = pygame.mixer.Sound("Sounds\\arrow_2.mp3")
Lose = pygame.mixer.Sound("Sounds\\lose.wav")
Win = pygame.mixer.Sound("Sounds\\Win.wav")
self_hit = cut_sound1(Lose)
opp_hit = cut_sound2(Win)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
def welcome():
    gameexit=False
    while not gameexit:
        gameWindow.blit(bgimg,(0,0))
        
        gameWindow.blit(P,(0,H-h-int((0.56)*pltfrm.get_height())))
        gameWindow.blit(parr,(int(1.5*w/3.5),H-int((2.1)*h/3)-int((0.56)*pltfrm.get_height())))
        
        text_screen("Welcome to War",(0,0,0),int(W/3),int(H/2))
        
        text_screen("Press Space Bar to Play",(0,0,0),int(W/3),int(H/2 + H/15))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game()
        pygame.display.update()
        clock.tick(fps)

def game():
    pygame.mixer.music.play(-1)
    Ox=int(2*W/3)
    Oy=H-h-int((0.56)*pltfrm.get_height())
    
    px=0
    py=H-h-int((0.56)*pltfrm.get_height())
    
    chx=px
    chy=py

    ochx=Ox
    ochy=Oy

    parx=int(1.5*w/3.5)
    pary=H-int((2.1)*h/3)-int((0.56)*pltfrm.get_height())
    
    Oarx=Ox+int(1.5*w/3.5)-int(w/2)
    Oary=H-int((2.1)*h/3)-int((0.56)*pltfrm.get_height())
    
    g=0
    vy=0
    og=0
    ovy=0
    
    chary=pary
    charx=parx

    ocharx=Oarx
    ochary=Oary

    gameexit=False
    
    startp=0
    starto=0
    life=100
    olife=100
    
    ip=0
    io=0
    gameover=False
    gamewin=False
    f_arrs = 50
    dec_life_o = 10
    arrs_left = 100//dec_life_o + 2
    dec_life_p = 15
    shoot_allowed = 1
    while not gameexit:
        if not (gameover or gamewin):
            if(py==chy):
                g=0
            else:
                g=1
            if(Oy==chy):
                og=0
            else:
                og=1
            gameWindow.blit(bgimg,(0,0))
            
            gameWindow.blit(P,(px,py))
            pygame.draw.rect(gameWindow,(250,0,0),[px,py,life,10])
            gameWindow.blit(parr,(parx,pary))
            gameWindow.blit(O,(Ox,Oy))
            pygame.draw.rect(gameWindow,(0,0,250),[Ox+int(w/2),Oy,olife,10])
            gameWindow.blit(oarr,(Oarx,Oary))
            if(arrs_left <= 6):
                for i in range(arrs_left):
                    gameWindow.blit(parr_left,(35+int(parr_left.get_width()*i/2),25))
            else:
                for i in range(6):
                    gameWindow.blit(parr_left,(35+int(parr_left.get_width()*i/2),25))
                for i in range(arrs_left-6):
                    gameWindow.blit(parr_left,(35+int(parr_left.get_width()*i/2),25+parr_left.get_height()))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameexit=True
                if event.type==pygame.KEYDOWN :
                    if(event.key==pygame.K_f):
                        startp=1*(shoot_allowed)
                        if(shoot_allowed and parx==px+int(1.5*w/3.5)):
                            pygame.mixer.Sound.play(arrow_shoot)
            keys=pygame.key.get_pressed()
            if(keys[pygame.K_RIGHT])and(px+w+charx-chx<Ox):
            
                px+=10
                parx+=10
            if(keys[pygame.K_LEFT])and(px>0):
                px-=10
                parx-=10
            if(py>=chy):
                if(keys[pygame.K_SPACE]):
                    vy=20
                else:
                    vy=0
            if(Oy>=chy):
                if not(random.randint(0,50)):
                    ovy=20
                else:
                    ovy=0
            if(not random.randint(0,50))and(Ox<W and Ox > int(2*w/3)):
                if(random.randint(0,1))and(Ox<W-55):
                    for i in range(5):
                        Ox+=10
                        Oarx+=10
                elif(Ox>int(2*W/3)+55):
                    for i in range(5):
                        Ox-=10
                        Oarx-=10
            if(not random.randint(0,f_arrs)):
                starto=True
                if(Oarx == Ox+ochx-ocharx and starto):
                    pygame.mixer.Sound.play(arrow_shoot)
            py-=vy
            if(not startp):
                pary-=vy
                
            if(not starto):
                
                Oary=ochary+Oy-ochy
                
            vy-=g
            ovy-=og
            Oy-=ovy
            
            if(startp):
                parx+=15
            if(starto):
                Oarx-=15
            if(abs(Oy+int(h/2)-pary)<int(h/2) and abs(parx+warr - (Ox + int(w/2)))<int(w/2) ):
                if(arrs_left>0):
                    parx=px+int(1.5*w/3.5)
                else:
                    parx = -200
                    shoot_allowed = 0
                arrs_left-=1
                io+=1
                olife=100-(dec_life_o)*io
                pygame.mixer.Sound.play(opp_hit)
                startp=False
                pary=chary+py-chy  
            if(parx>=W):
                if(arrs_left>0):
                    parx=px+int(1.5*w/3.5)
                else:
                    parx = -200
                    shoot_allowed = 0
                
                arrs_left-=1
                startp=False
                pary=chary+py-chy  
            if(abs(py+int(h/2)-Oary)<int(h/2) and abs(Oarx - (px + int(w/2)))<int(w/2) ):
                Oarx=Ox+ochx-ocharx
                ip+=1
                life=100-(dec_life_p)*ip
                pygame.mixer.Sound.play(self_hit)
                starto=False
                Oary=ochary+Oy-ochy  
            if(Oarx+int(warr/2)<0):
                Oarx=Ox+ochx-ocharx
                starto=False
                Oary=ochary+Oy-ochy
            
            if(life<=0):
                gameover=True
                pygame.mixer.Sound.play(Lose)
            if(olife<=0):
                gamewin=True
                pygame.mixer.Sound.play(Win)
        else:
            gameWindow.blit(bgimg,(0,0))
            if(gameover):
                text_screen("You Lose", (0,0,250), int(2*w/3), int(h/2))
                text_screen("Press Space bar to play", (0,0,250), int(2*w/3), int(h/2)+40)
            else:
                text_screen("You Win", (0,0,250), int(2*w/3), int(h/2))
                text_screen("Press Space bar to play", (0,0,250), int(2*w/3), int(h/2)+40)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN :
                if(event.key==pygame.K_SPACE):
                    welcome()

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
