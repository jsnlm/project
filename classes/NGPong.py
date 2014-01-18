import random, math, pygame, pygame, string, sys, time
from pygame import *

pygame.init()

#Creates variable which has the value of RBG
black = [0,0,0]
white = [255,255,255]
yellow = [255,255,0]
red = [255,0,0]
orange = [255,69,0]
grey = [105,105,105]
purple = [72,61,139]
magenta = [255, 0, 255]
dgreen = [0,100,0]
Window = [500,400]

#Creates a Ball class
class Ball(pygame.sprite.Sprite):

    #Creates a ball with the picture and outputs the ball on to the window
    def __init__(self, x, y,obt, x_velocity):
        self.xv = x_velocity+0.0
        self.yv = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = image.load("resources/pongball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x+0.0
        self.rect.y = y+0.0
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.obs=obt

    #Updates the location of the ball as well as its velocity
    def update(self):
        #Boucing off the top and bottom boarder
        if self.rect.y<=0:
            self.yv=-self.yv
            self.rect.y=0
        elif self.rect.y>=285:
            self.yv=-self.yv
            self.rect.y=285

        #Boucing off the paddle 1
        if self.xv<0:
            if self.rect.x<=(paddle.rect.x+10.0) and self.rect.x>=(paddle.rect.x+5.0):
                if self.rect.y>=(paddle.rect.y-15.0) and self.rect.y<=(paddle.rect.y+50.0):
                    self.rect.x=paddle.rect.x+10.0
                    self.xv=-self.xv

                    if self.rect.y>=(paddle.rect.y-15.0) and self.rect.y<(paddle.rect.y+15):
                        diff=math.fabs(math.fabs(paddle.rect.y-15.0)-math.fabs(self.rect.y))
                        self.yv=(self.yv+5*(((30-math.fabs(diff))/30)))
                        if self.yv<0:
                            self.yv=-self.yv
                    elif self.rect.y>=(paddle.rect.y+20) and self.rect.y<(paddle.rect.y+50.0):
                        diff=math.fabs(math.fabs(paddle.rect.y+50.0)-math.fabs(self.rect.y))
                        self.yv=(self.yv-2*(((30-math.fabs(diff))/30)))
                        if self.yv>0:
                            self.yv=-self.yv

            #Bouncing off the obstable from the right
            if self.obs==True:
                if self.rect.x<=(obst.rect.x+10) and self.rect.x>=(obst.rect.x):
                        if self.rect.y>=(obst.rect.y-15.0) and self.rect.y<=(obst.rect.y+50.0):
                            self.rect.x=obst.rect.x+10.0
                            self.xv=-self.xv



        #Boucing off the paddle 2
        elif self.xv>0:
            if (self.rect.x+15.0)<=(paddle2.rect.x+5.0) and (self.rect.x+15.0)>=(paddle2.rect.x+0.0):
                if self.rect.y>=(paddle2.rect.y-15.0) and self.rect.y<=(paddle2.rect.y+50.0):
                    self.xv=-self.xv
                    if self.rect.y>=(paddle2.rect.y-15.0) and self.rect.y<(paddle2.rect.y+15):
                        diff=math.fabs(math.fabs(paddle2.rect.y-15.0)-math.fabs(self.rect.y))
                        self.yv=(self.yv+5*(((30-math.fabs(diff))/30)))
                        if self.yv<0:
                            self.yv=-self.yv
                    elif self.rect.y>=(paddle2.rect.y+20.0) and self.rect.y<(paddle2.rect.y+50.0):
                        diff=math.fabs(math.fabs(paddle2.rect.y+50.0)-math.fabs(self.rect.y))
                        self.yv=(self.yv-2*(((30-math.fabs(diff))/30)))
                        if self.yv>0:
                            self.yv=-self.yv

            #Bouncing off the obstable from the left
            if self.obs==True:
                if self.rect.x+15.0<=(obst.rect.x+10) and self.rect.x+15.0>=(obst.rect.x):
                        if self.rect.y>=(obst.rect.y-15.0) and self.rect.y<=(obst.rect.y+50.0):
                            self.rect.x=obst.rect.x-15
                            self.xv=-self.xv


        #Getting rid of zero velocity
        if self.yv>-1.0 and self.yv<=0.0:
            self.yv=-1.0
        elif self.yv>0.0 and self.yv<1.0:
            self.yv=1.0
        self.rect.x += self.xv
        self.rect.y -= self.yv

        #Outputs onto the screen
        screen.blit(self.image, (int(self.rect.x), int(self.rect.y)))


#Creates a player 1 class
class Player_1(pygame.sprite.Sprite):

    #Create a paddle with the rectangle module and locates it at assigned spot
    def __init__(self,x,y):
        self.pyv = 0
        pygame.sprite.Sprite.__init__(self)
        self.pos = [x,y]
        self.rect = Rect((self.pos), (10, 50))
        pygame.draw.rect(screen, yellow, self.rect)

    #Updates the location of the paddle as well as its velocity
    def update(self):
        if event.type==KEYDOWN:
            if event.key==K_w:
                self.pyv = +3
            elif event.key==K_s:
                self.pyv = -3
        elif event.type==KEYUP:
            if event.key==K_w:
                self.pyv = 0
            elif event.key==K_s:
                self.pyv = 0
        self.rect.y -= self.pyv
        if self.rect.y<0:
            self.rect.y=0
        elif self.rect.y>250:
            self.rect.y=250
        pygame.draw.rect(screen, yellow, self.rect)

#Creates a player 1 class
class Player_2(pygame.sprite.Sprite):

    #Create a paddle with the rectangle module and locates it at assigned spot
    def __init__(self,x,y):
        self.pyv2 = 0
        pygame.sprite.Sprite.__init__(self)
        self.pos = [x,y]
        self.rect = Rect((self.pos), (10, 50))
        pygame.draw.rect(screen, yellow, self.rect)

    #Updates the location of the paddle as well as its velocity
    def update(self):
        if event.type==KEYDOWN:
            if event.key==K_UP:
                self.pyv2 = +3
            elif event.key==K_DOWN:
                self.pyv2 = -3
        elif event.type==KEYUP:
            if event.key==K_UP:
                self.pyv2 = 0
            elif event.key==K_DOWN:
                self.pyv2 = 0
        self.rect.y -= self.pyv2
        if self.rect.y<0:
            self.rect.y=0
        elif self.rect.y>250:
            self.rect.y=250
        pygame.draw.rect(screen, yellow, self.rect)

#Creates a bot class
class Bot(pygame.sprite.Sprite):

    #Create a paddle with the rectangle module and locates it at assigned spot
    def __init__(self,x,y,level):

        self.speed=level
        self.pyv3 = 0
        pygame.sprite.Sprite.__init__(self)
        self.pos=[x,y]
        self.rect=Rect((self.pos),(10,50))
        pygame.draw.rect(screen,yellow,self.rect)

    #Updates the location of the paddle as well as its velocity
    def update(self):
        if ball.rect.y<self.rect.y+15:
            self.pyv3 = +self.speed
        elif ball.rect.y>=self.rect.y+15 and ball.rect.y<self.rect.y+35:
            self.pyv3 = 0
        elif ball.rect.y>self.rect.y+35:
            self.pyv3 = -self.speed
        self.rect.y -= self.pyv3
        if self.rect.y<0:
            self.rect.y=0
        elif self.rect.y>250:
            self.rect.y=250
        pygame.draw.rect(screen, yellow, self.rect)

#Creates an obstacle class
class Obstacle(pygame.sprite.Sprite):

    #Create a paddle with the rectangle module and locates it at assigned spot
    def __init__(self,x,y,level):
        self.speed=level
        self.pyv4 = self.speed
        pygame.sprite.Sprite.__init__(self)
        self.pos=[x,y]
        self.rect=Rect((self.pos),(10,50))
        pygame.draw.rect(screen,orange,self.rect)

    #Updates the location of the paddle as well as its velocity
    def update(self):
        self.rect.y -= self.pyv4
        if self.rect.y<0:
            self.rect.y=0
            self.pyv4=-self.pyv4
        elif self.rect.y>250:
            self.rect.y=250
            self.pyv4=-self.pyv4
        pygame.draw.rect(screen, orange, self.rect)

class GGame():
    def __init__():
        GGame.mainDecision=True
        GGame.mainDecision2=True

#Creates the main game class
def PongGame():
    #Creates global variables
    GGame.mainDecision=True
    GGame.mainDecision2=True
    global score1
    global score2
    global screen
    global ball
    global paddle
    global paddle2
    global event
    global obst

    score1=0
    score2=0

    pspeed=0
    bspeed=1
    oblv=1
    bv=-1
    bx=400
    by=135

    game=False
    mousecolor1=red
    mousecolor2=red
    mousecolor3=red
    mousecolor4=red

    titlefont=pygame.font.Font(None,100)
    font = pygame.font.Font(None, 40)
    textfont=pygame.font.Font(None,25)

    mainwin=True
    win1=False
    win2=False
    win3=False
    win4=False
    lap=False

    #Instructions for the game
    intro=["GOAL","The game, Pong, is a two-dimensional game, which ","simulates table tennis. Players use the paddles to hit a","ball back and forth.The aim is for a player to earn more",
    "points than the opponent; points are earned when one","fails to return the ball to the other.","_______________________________________________","CONTROLS","Player 1:","Up = [W]        Down = [D]","Player 2:","Up = [UP]      Down = [Down]",
    "_______________________________________________","SCORING","First player to score 10 Wins!!!"]

    bot = False
    obstacle = False
    pause=False
    #GGame.__init__()
    #Creates main window where user can decide either to play the game, see the instruction, or quit game
    while GGame.mainDecision==True and GGame.mainDecision2==True:
        score1=0
        score2=0
        pygame.init()
        pygame.font.init()

        screen = pygame.display.set_mode(Window)
        screen.fill(black)

        background = pygame.Surface((500,400))
        background = background.convert()
        pback = pygame.Surface((140,160))
        pback = pback.convert()

        clock = pygame.time.Clock()

        background.fill(black)
        pback.fill(purple)

        while mainwin==True:
            screen.blit(background, (0, 0))

            mousex,mousey=pygame.mouse.get_pos()

            if mousex>176 and mousex<324 and mousey>200 and mousey<230:
                mousecolor1=grey
            else:
                mousecolor1=white
            if mousex>218 and mousex<282 and mousey>250 and mousey<280:
                mousecolor2=grey
            else:
                mousecolor2=white
            if mousex>0 and mousex<240 and mousey>0 and mousey<17:
                mousecolor3=grey
            else:
                mousecolor3=white
            if mousex>176 and mousex<324 and mousey>300 and mousey<325:
                mousecolor4=grey
            else:
                mousecolor4=white
            print pygame.mouse.get_pos()
            screen.blit(titlefont.render("NG Pong",True,orange),[106,50])
            screen.blit(font.render("Play Game",True,mousecolor1),[176,200])
            screen.blit(font.render("Help",True,mousecolor2),[218,250])
            screen.blit(font.render("Quit Game",True,mousecolor4),[176,300])
            screen.blit(textfont.render('Return to Game Suite Menu',True,mousecolor3),[0,0])


            pygame.display.update()
            for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if mousex>176 and mousex<324 and mousey>200 and mousey<230:
                                mainwin=False
                                win1=True
                            elif mousex>218 and mousex<282 and mousey>250 and mousey<280:
                                mainwin=False
                                win2=True
                            elif mousex>0 and mousex<240 and mousey>0 and mousey<17:
                                GGame.mainDecision2=False
                                screen = pygame.display.set_mode([600,674])
                                screen = Rect(0,0,600,674)
                                mainwin=False
                            elif mousex>176 and mousex<324 and mousey>300 and mousey<325:
                                GGame.mainDecision=False
                                mainwin=False


        #Creates window 1 where user can either choose to play classic or advanced mode
        while win1==True:
            screen.blit(background, (0, 0))

            mousex,mousey=pygame.mouse.get_pos()

            if mousex>200 and mousex<300 and mousey>200 and mousey<230:
                mousecolor1=grey
            else:
                mousecolor1=white
            if mousex>182 and mousex<318 and mousey>250 and mousey<280:
                mousecolor2=grey
            else:
                mousecolor2=white
            if mousex>217 and mousex<283 and mousey>300 and mousey<330:
                mousecolor3=grey
            else:
                mousecolor3=white


            screen.blit(titlefont.render("NG Pong",True,orange),[106,50])
            screen.blit(font.render("Classic",True,mousecolor1),[200,200])
            screen.blit(font.render("Advanced",True,mousecolor2),[182,250])
            screen.blit(font.render("Back",True,mousecolor3),[217,300])

            pygame.display.update()
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mousex>200 and mousex<300 and mousey>200 and mousey<230:
                            win1=False
                            win3=True
                            obstacle=False
                        elif mousex>182 and mousex<318 and mousey>250 and mousey<280:
                            win1=False
                            win3=True
                            obstacle=True
                        elif mousex>217 and mousex<283 and mousey>300 and mousey<330:
                            win1=False
                            mainwin=True

        #Creates window 2 where user can see the instructions and go back to the previouse window
        while win2==True:
            screen.blit(background, (0, 0))

            mousex,mousey=pygame.mouse.get_pos()

            if mousex>430 and mousex<500 and mousey>5 and mousey<30:
                mousecolor1=grey
            else:
                mousecolor1=white



            screen.blit(titlefont.render("Help",True,yellow),[5,5])
            screen.blit(font.render("Back",True,mousecolor1),[430,5])
            counter=80
            for x in range (0,len(intro)):
                screen.blit(textfont.render(intro[x],True,mousecolor3),[13,counter])
                counter+=20

            pygame.display.update()
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mousex>430 and mousex<500 and mousey>5 and mousey<30:
                            win2=False
                            mainwin=True

        #Creates window 3 where user can choose either single or multiplayer mode
        while win3==True:
            screen.blit(background, (0, 0))

            mousex,mousey=pygame.mouse.get_pos()

            if mousex>158 and mousex<342 and mousey>200 and mousey<230:
                mousecolor1=grey
            else:
                mousecolor1=white
            if mousex>172 and mousex<328 and mousey>250 and mousey<280:
                mousecolor2=grey
            else:
                mousecolor2=white
            if mousex>217 and mousex<283 and mousey>300 and mousey<330:
                mousecolor3=grey
            else:
                mousecolor3=white


            screen.blit(titlefont.render("NG Pong",True,orange),[106,50])
            screen.blit(font.render("Single Player",True,mousecolor1),[158,200])
            screen.blit(font.render("Multiplayer",True,mousecolor2),[172,250])
            screen.blit(font.render("Back",True,mousecolor3),[217,300])

            pygame.display.update()
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mousex>158 and mousex<342 and mousey>200 and mousey<230:
                            win3=False
                            win4=True
                            bot=True
                        elif mousex>172 and mousex<328 and mousey>250 and mousey<280:
                            win3=False
                            bot=False
                            game=True
                            bspeed=2
                            if obstacle==True:
                                oblv=1
                        elif mousex>217 and mousex<283 and mousey>300 and mousey<330:
                            mousecolor3=grey
                            win3=False
                            win1=True

        #Creates window 4 where user can choose difficulties
        while win4==True:
            screen.blit(background, (0, 0))

            mousex,mousey=pygame.mouse.get_pos()

            if mousex>218 and mousex<282 and mousey>200 and mousey<225:
                mousecolor1=grey
            else:
                mousecolor1=white
            if mousex>197 and mousex<303 and mousey>230 and mousey<255:
                mousecolor2=grey
            else:
                mousecolor2=white
            if mousex>217 and mousex<283 and mousey>260 and mousey<285:
                mousecolor3=grey
            else:
                mousecolor3=white
            if mousex>217 and mousex<283 and mousey>310 and mousey<335:
                mousecolor4=grey
            else:
                mousecolor4=white


            screen.blit(titlefont.render("NG Pong",True,orange),[106,50])
            screen.blit(font.render("Easy",True,mousecolor1),[218,200])
            screen.blit(font.render("Medium",True,mousecolor2),[197,230])
            screen.blit(font.render("Hard",True,mousecolor3),[217,260])
            screen.blit(font.render("Back",True,mousecolor4),[217,310])

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mousex>218 and mousex<282 and mousey>200 and mousey<225:
                        win4=False
                        game=True
                        pspeed=3
                        bspeed=1
                        if obstacle==True:
                            oblv=1

                    elif mousex>197 and mousex<303 and mousey>230 and mousey<255:
                        win4=False
                        game=True
                        pspeed=5
                        bspeed=2
                        if obstacle==True:
                            oblv=1.5

                    elif mousex>217 and mousex<283 and mousey>260 and mousey<285:
                        win4=False
                        game=True
                        pspeed=7
                        bspeed=3
                        if obstacle==True:
                            oblv=2
                    elif mousex>217 and mousex<283 and mousey>310 and mousey<335:
                        win4=False
                        win3=True


        #Create the game window where user can play in their chosen preferences
        while game==True:
            paddle=Player_1(10,125)
            if bot==True:
                paddle2=Bot(480,125,pspeed)
            else:
                paddle2=Player_2(480,125)
            obst=Obstacle(245,100,oblv)
            ball=Ball(bx,by,obstacle,bv)
            ball.xv=ball.xv*bspeed
            lap=True
            while lap==True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYDOWN:
                        if event.key==K_ESCAPE:
                            if pause==False:
                                pause=True
                            else:
                                pause=False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pause==True:
                            if mousex>215 and mousex<285 and mousey>175 and mousey<190:
                                pause=False

                            elif mousex>218 and mousex<280 and mousey>200 and mousey<215:
                                score1=0
                                score2=0
                                pause=False
                                lap=False

                            elif mousex>203 and mousex<296 and mousey>225 and mousey<240:
                                pause=False
                                lap=False
                                game=False
                                mainwin=True

                if pause==False:
                    screen.blit(background, (0, 0))

                    ball.update()
                    paddle.update()
                    paddle2.update()
                    if obstacle==True:
                        obst.update()

                    if ball.rect.x<=-25:
                        score2=score2+1
                        bx=100
                        by=135
                        bv=1
                    elif ball.rect.x>=500:
                        score1=score1+1
                        bx=400
                        by=135
                        bv=-1

                    sc1=font.render(str(score1), True, red,)
                    sc2=font.render(str(score2), True, red,)

                    pygame.draw.rect(background,white,(0,0,250,300),5)
                    pygame.draw.rect(background,white,(250,0,250,300),5)

                    screen.blit(font.render("Player 1", True, red,),[70, 305])
                    screen.blit(font.render(str(score1), True, red,),[118, 345])
                    screen.blit(font.render(":", True, red,),[246, 320])
                    screen.blit(font.render("Player 2", True, red,),[320, 305])
                    screen.blit(font.render(str(score2), True, red,),[368, 345])
                    screen.blit(textfont.render("Press ESC to PAUSE", True, purple,),[165, 375])

                #Creates pause menu
                elif pause==True:
                    screen.blit(pback, (180, 100))
                    mousex,mousey=pygame.mouse.get_pos()
                    if mousex>215 and mousex<285 and mousey>175 and mousey<190:
                        mousecolor1=grey
                    else:
                        mousecolor1=white
                    if mousex>218 and mousex<280 and mousey>200 and mousey<215:
                        mousecolor2=grey
                    else:
                        mousecolor2=white
                    if mousex>203 and mousex<296 and mousey>225 and mousey<240:
                        mousecolor3=grey
                    else:
                        mousecolor3=white

                    screen.blit(font.render("Paused", True, orange,),[200, 110])
                    screen.blit(textfont.render("Resume", True, mousecolor1,),[215, 175])
                    screen.blit(textfont.render("Restart", True, mousecolor2,),[218, 200])
                    screen.blit(textfont.render("Main Menu", True, mousecolor3,),[203, 225])

                clock.tick(100)
                pygame.display.update()
                if ball.rect.x<=-25 or ball.rect.x>=500:
                    lap=False
                if score1==10 or score2==10:
                    if score1==10:
                        screen.blit(font.render("Win", True, magenta,),[100, 142])
                        screen.blit(font.render("Lose", True, dgreen,),[350, 142])
                    else:
                        screen.blit(font.render("Win", True, magenta,),[350, 142])
                        screen.blit(font.render("Lose", True, dgreen,),[100, 142])
                    pygame.display.update()
                    time.sleep(3)
                    lap=False
                    game=False
                    mainwin=True

    if GGame.mainDecision2==True:
        quit()
        pygame.quit()


