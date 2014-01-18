'''
Bubble Fantasy Game

The link to the original game: http://www.pygame.org/project-pygame+bubble+shooter-1841-.html

Credits to Joel Murielle for the original game
'''


from random import choice

#import pygame, font and mixer (for sound and music)

import pygame
pygame.init()
from pygame import *
font.init()

import pygame.mixer
pygame.mixer.init()

sound=pygame.mixer.Sound('resources/pop.wav')
music=pygame.mixer.music.load('resources/music.mp3')
pygame.mixer.music.set_volume(0.1)

from math import sin,cos,atan2,degrees,radians

hole = image.load('resources/erase.png')    #disappearing effect images
effect = image.load('resources/effect.png')
effect2=image.load('resources/effect2.png')

mainclock = time.Clock()

#initialize the balls and their images
balls = {   'Red':image.load('resources/redBall.png'),
            'Blue':image.load('resources/blueBall.png'),
            'Yellow':image.load('resources/yellowBall.png'),
            'Green':image.load('resources/greenBall.png'),
            'Violet':image.load('resources/purpleBall.png')}

ball_rect = balls['Red'].get_rect()

alpha = int(cos(radians(30))*ball_rect.height)
screen = Rect(0,0,15*ball_rect.width,16*ball_rect.height+alpha)
scr = display.set_mode(screen.size)
pygame.display.set_caption('Castor Game Suite')

bg=image.load('resources/Wood-background.jpg').convert()

beta = ball_rect.centerx        #special coordinates on the game screen
gamma = ball_rect.width
delta = ball_rect.width**2*0.6
zeta = 15 * alpha
eta = 14 * alpha + ball_rect.width

ball_rect.center = scr.fill((128,128,128),(0,eta,screen.width,2*ball_rect.width)).center

#initialize different fonts used in the game and their sizes
endfont = font.Font(None,45);menufont=font.Font(None,60);menu2font = font.Font(None,30)
menu3font=font.Font(None,35);menu4font=font.Font(None,25);menu5font=font.Font(None,23)

class Arrow:

    img_origin = image.load('resources/arrow.png')  #image origin of arrow

    '''
    Pre: Position of mouse, the y-coordinate of bottom limit line
    Post: Constantly updates the position of the arrow image based on the mouse position relative to the coordinate of the bottom limit line
    Purpose: Updates the position of the arrow according to position of mouse cursor
    '''

    @staticmethod
    def update(pos,limit):
        x,y = pos
        if y > limit:
            y = limit
            mouse.set_pos((x,y))
        Arrow.image = transform.rotate(Arrow.img_origin,-degrees(atan2(y-ball_rect.centery,x-ball_rect.centerx)))
        Arrow.rect = Arrow.image.get_rect(center=(x-14,y+5))    #calibrating the cursor position and tip of arrow

#Class used to initiate a Game
class Game:
    renderClock = time.Clock()  #initiates timer used to time the amount of rendering per time interval
    renderTime = 0
    popEffectClock = time.Clock()   #initiates timer used to time how fast the disappearing effect is applied
    popEffectTime = 0
    coord = 1  # coordinate helper that determines the position of balls

    '''
    Pre: None
    Post: Returns a randomly chosen color from the available colors in colorCount, String
    Purpose: To output a random color
    '''

    @staticmethod
    def colorChoice():
        colors = ('Red','Blue','Yellow','Green','Violet')   #creates a list of all the available colors
        return choice(colors)   #returns a randomly chosen colour

    '''
    Pre: String level
    Post: A game will be initialized based on its various characteristics; only level affects certain characteristics
    Purpose: To create an instance of the Game object
    '''

    @staticmethod
    def init(level):
        Game.mainDecision=True
        Game.mainDecision2=True
        Game.pause = False
        Animation.clear()
        Game.score = 0      #initiate score and progress bar timer and main game timer
        Game.timer1=0
        Game.timer2=0
        Game.multiplier=0

        Game.bgCopy = bg.copy(); Game.bgCopy.set_alpha(100)
        Game.status = 0
        Game.colorCount = {'Red':0,'Blue':0,'Yellow':0,'Green':0,'Violet':0}    #set the different colours of ball used
        Game.d = {} #dictionary that stores the coordinates of all balls on screen
        Game.l  = []    #list that stores the positions of balls struck
        Game.l0 = []    #list that stores the position of all remaining balls
        Game.l1 = []

        if level=='Beginner': Game.progressBarSpeed=0.5; Game.multiplier=1; Game.addLine(10) #initiates progress bar speed, rows of initial balls and multiplier based on level chosen
        elif level=='Easy': Game.progressBarSpeed=0.5; Game.multiplier=1; Game.addLine(10)
        elif level=='Normal':Game.progressBarSpeed=1; Game.multiplier=2;Game.addLine(10)
        elif level=='Hard': Game.progressBarSpeed=2; Game.multiplier=4;Game.addLine(7)
        elif level=='Impossible': Game.progressBarSpeed=3.5; Game.multiplier=8; Game.addLine(5)

        Game.ball_nb = -1

        Game.coord = (min(Game.d,key=lambda x: x[1])[0]//beta)&1
        [Game.colorCount.pop(c)for c,v in list(Game.colorCount.items()) if not v]
        Game.ball = None    # initialzie
        Animation.add(Game.render)
        Game.dkeys = set(Game.d.keys()) #direction keys for menu initialized
        Game.maintime = time.get_ticks()

    '''
    *Code Credited to Original Game*

    Pre: None
    Post: Updates score, game status, and determining if lowermost ball(s) hit the white line
    Purpose: Helper function that is used in gameLoop to update various aspects of game
    '''

    @staticmethod
    def update():
        if not Game.status:
            if not Game.ball:
                if not Game.ball_nb:
                    Game.status = 1
                    return
                color = Game.colorChoice()
                Game.ball = Ball(color)
                Game.colorCount[color]+=1
            elif Game.ball.fix:
                Game.bgCopy.blit(Game.ball.img,Game.ball)
                Game.d[Game.ball.center] = Game.ball.color
                l = [Game.ball.center]
                for X,Y in l:
                    for x,y in ((-gamma,0),(-beta,-alpha),(beta,-alpha),(gamma,0),(-beta,alpha),(beta,alpha)):
                        if (X+x,Y+y)in Game.d and Game.d[(X+x,Y+y)] == Game.ball.color and (X+x,Y+y) not in l: l.append((X+x,Y+y))
                if len(l) >= 3:
                    Game.scoreN = 2
                    for x,y in l:
                        Game.d.pop((x,y))
                    Game.colorCount[Game.ball.color] -= len(l)
                    if not Game.colorCount[Game.ball.color]: Game.colorCount.pop(Game.ball.color)

                    m = Game.d.copy()
                    k = [(x,y)for x,y in m if y==beta]
                    for X,Y in k:
                        m.pop((X,Y))
                        for x,y in ((-gamma,0),(-beta,-alpha),(beta,-alpha),(gamma,0),(-beta,alpha),(beta,alpha)):
                            if (X+x,Y+y)in m and not(X+x,Y+y)in k: k.append((X+x,Y+y))
                    Game.l.extend(l)
                    for (x,y),color in m.items():
                        Game.d.pop((x,y))
                        Game.colorCount[color] -= 1
                        if not Game.colorCount[color]: Game.colorCount.pop(color)
                    Game.l.extend(m.keys())
                    if not Game.colorCount: Game.status = 1
                    Animation.add(Game.popBalls)
                elif Game.ball.bottom > eta:
                    Game.status = 1
                Game.dkeys = set(Game.d.keys())
                Game.ball = None
                Game.ball_nb -= 1
            elif Game.ball.lost:
                Game.colorCount[Game.ball.color] -= 1
                if not Game.colorCount[Game.ball.color]: Game.colorCount.pop(Game.ball.color)
                Game.ball = None
                Game.ball_nb -= 1
        elif Game.status == 1:
            if not any((Game.l,Game.l0,Game.l1)):
                if not Game.colorCount:
                    Game.status = 4
                else:
                    Game.status = 6
                Game.bgCopy.set_alpha(255)
        else:
            Game.status //= 2

    '''
    Pre: None
    Post: "Pops" the ball images by applying the disappearing effect image
    Purpose: Makes balls disappear when struck by ball shot
    '''

    @staticmethod
    def popBalls():
        Game.popEffectTime += Game.popEffectClock.tick()    #pop effect timer used to time how long pop effects last
        if Game.popEffectTime >= 15:
            if Game.l1:
                x,y = Game.l1.pop(0)    #pop the ball and apply disappearing effect
                Game.bgCopy.blit(appliesEffect(hole,bg.subsurface(x-beta,y-beta,gamma,gamma)),(x-beta,y-beta))
                Game.score += 1 #add 1 to score.. 100 will be multiplied later
            if Game.l0:
                x,y = Game.l0.pop(0)    #pop the ball and apply disappearing effect
                Game.bgCopy.blit(appliesEffect(effect,bg.subsurface(x-beta,y-beta,gamma,gamma)),(x-beta,y-beta))
                Game.l1.append((x,y))
                Game.score += 1 #add 1 to score.. 100 will be multiplied later
            if Game.l:
                x,y = Game.l.pop(0) #pop the ball and apply disappearing effect
                Game.bgCopy.blit(appliesEffect(effect2,bg.subsurface(x-beta,y-beta,gamma,gamma)),(x-beta,y-beta))
                Game.l0.append((x,y))
                Game.scoreN -= 1
                Game.score +=1  #add 1 to score.. 100 will be multiplied later
            if not Game.l0 and not Game.l1:
                Animation.remove(Game.popBalls) #remove the animation effect after the intended popped balls are gone
            Game.popEffectTime = 0  #reset the pop effect timer

    '''
    Pre: None
    Post: Constantly updates the labels, ball images and arrow image over a very short interval, based on the renderClcok
    Purpose: To update the graphics on the game screen constantly. Used as helper function
    '''

    @staticmethod
    def render():
        Game.renderTime += Game.renderClock.tick()
        if Game.renderTime >= 10:
            scr.blit(Game.bgCopy,screen)
            if Game.ball:
                scr.blit(Arrow.image,Arrow.rect)
                scr.blit(Game.ball.img,Game.ball)

            if Game.status==1:
                label = menu2font.render('Score : '+str(Game.multiplier*100*Game.score/3+(1/Game.timer1)*100000),1,(224,255,255)) #Adds time bonus to score if all balls are removed
            else: label = menu2font.render('Score : '+str(Game.multiplier*100*Game.score/3),1,(224,255,255)) #Display score and multiplier on screen
            label2=menu4font.render('Multi: x'+str(Game.multiplier),1,(135,206,250))
            label3 = label.get_rect(bottomright=screen.move(-12,-12).bottomright)
            scr.blit(label,label3)
            scr.blit(label2,(500,620))

            display.flip()
            Game.renderTime = 0
            return True

    '''
    *Code from Original Game*

    Pre: Positive integer n, determining number of lines to add to gamescreen
    Post: Adds n number of lines to gamescreen
    Purpose: To add a certain number of rows of balls to gamescreen
    '''

    @staticmethod
    def addLine(n):
        Game.bgCopy.set_alpha(255)

        for n in range(n):
            Game.d = dict([((x,y+alpha),color)for (x,y),color in Game.d.items()])
            for x in range(beta*Game.coord+beta,screen.w,gamma):
                color = Game.colorChoice()
                Game.d[(x,beta)] = color
                Game.colorCount[color] += 1
            Game.coord ^= 1
        Game.dkeys = set(Game.d.keys())
        Game.bgCopy.blit(bg,screen)
        for (x,y),color in Game.d.items():
            Game.bgCopy.blit(balls[color],(x-beta,y-beta))
            if y >= zeta: Game.status = 1
            Game.bgCopy.set_alpha(100)

    '''
    Pre: None
    Post: None
    Purpose: Pauses the game loop and the various timers
    '''

    @staticmethod
    def pauseGame():
        if Game.pause:
            Game.renderClock.tick()
            Game.popEffectClock.tick()
            if Game.ball: Game.ball.clock.tick()
            mouse.set_pos(Game.pause_mouse_pos)
            Game.maintime += time.get_ticks()-Game.pause_tick
            Game.pause = False
        else:
            Game.pause_mouse_pos = mouse.get_pos()
            Game.pause_tick = time.get_ticks()
            Game.pause = True

#Class used to initiate a ball
class Ball(Rect):

    '''
    Pre: String color (randomly generated by colorChoice
    Post: Initialize the various characteristics of Ball
    Purpose: Create an instance of a Ball
    '''

    def __init__(self,color):
        self.color = color      #initiate attributes
        self.img = Surface((0,0))
        self.px,self.py = self.cxcy = ball_rect.center
        self.cmp = 0
        self.timing = 1000000
        self.clock = time.Clock()
        Animation.add(self.appears)
        self.fix = False
        self.lost = False

    '''
    *Code from Original Game*

    Pre: None
    Post: None
    Purpose: Determines the showing up of ball to be released
    '''

    def appears(self):
        self.cmp += 1

        Rect.__init__(self,0,0,self.cmp*4,self.cmp*4)
        self.img = transform.scale(balls[self.color],self.size)
        self.center = self.cxcy
        if self.cmp == 10:
            Animation.remove(self.appears)
            Animation.add(self.release)
            self.timing = 1000000

    '''
    *Code from Original Game*

    Pre:None
    Post:None
    Purpose:To animate the shot/release of ball
    '''

    def release(self):
        if mouse.get_pressed()[0]:
            self.timing = 1
        self.timing -= 1
        if not self.timing:
            Animation.remove(self.release)  #animate the release and motion of ball
            Animation.add(self.move)
            x,y = mouse.get_pos()
            if y > eta: y = eta
            angle = atan2(y-self.centery,x-self.centerx)
            self.vx,self.vy = cos(angle)*1.5,sin(angle)*1.5

    '''
    *Code from Original Game*

    Pre: None
    Post: Moves the image of the ball based on its coordinates
    Purpose: To move the image of the ball around the game screen. Includes collision detection.
    '''

    def move(self):
        r = self.copy()
        r.center = self.px+self.vx,self.py+self.vy
        if r.top >= screen.bottom:
            Game.ball.lost = True
            Animation.remove(self.move)
            return
        if r.right > screen.right:
            self.px,self.py = screen.right-beta,self.centery+((r.centery-self.centery)/(r.centerx-self.centerx))*(screen.right-beta-self.centerx)
            self.vx = -self.vx
        elif r.left < screen.left:
            self.px,self.py = beta,self.centery+((r.centery-self.centery)/(r.centerx-self.centerx))*(beta-self.centerx)
            self.vx = -self.vx
        else:
            self.px += self.vx
            self.py += self.vy
        if r.top <= 0:
            self.px,self.py = self.centerx+((r.centerx-self.centerx)/(r.centery-self.centery))*(beta-self.centery),beta
            if self.px < beta: self.px = beta
            elif self.px > 29*beta: self.px = 29*beta
            self.px = int(self.px//beta);self.px = (self.px+(self.px&1^Game.coord))*beta;self.fix = True
        self.center = self.px,self.py
        x0 = (self.left//beta)*beta
        x1 = (self.right//beta+1)*beta+1
        y0 = ((self.top-beta)//alpha)*alpha+beta
        y1 = ((self.bottom-beta)//alpha+1)*alpha+16
        s = set([(x,y)for x in range(x0,x1,beta)for y in range(y0,y1,alpha)])
        w = Game.dkeys.intersection(s)
        for i in w:
            if (i[0]-self.centerx)**2+(i[1]-self.centery)**2 < delta:
                g = set([(i[0]+x,i[1]+y)for x,y in ((-gamma,0),(-beta,-alpha),(beta,-alpha),(gamma,0),(-beta,alpha),(beta,alpha)) if 0<i[0]+x<screen.right]).intersection(s.difference(w))
                self.center = min(g,key=lambda p:(self.centerx-p[0])**2+(self.centery-p[1])**2)
                self.fix = True
                break
        if self.fix: Animation.remove(self.move)

#Class used to keep track of animation effects
class Animation:

    animationList = []
    @staticmethod
    def update(): [method()for method in Animation.animationList]
    @staticmethod
    def add(method): Animation.animationList.append(method)
    @staticmethod
    def remove(method): Animation.animationList.remove(method)
    @staticmethod
    def clear(): Animation.animationList = []

'''
*Code from Original Game*
Pre: None
Post: Returns the image of disappearing effect
Purpose: Applies the effects on the game screen when balls are removed
'''

def appliesEffect(surface1,surface2):
    output = surface2.copy().convert_alpha()
    surfarray.pixels_alpha(output)[:] = surfarray.array_alpha(surface1)
    return output

'''
Pre: None
Post: None
Purpose: Runs the various components of the game in a continuous loop, including tracking the arrow and mouse, keyboard motion events, and updating the progress bar and game screen
'''

def gameLoop():
    decision=True
    colour=(255,255,255)
    pygame.mouse.set_visible(False)
    mouse.set_pos(screen.center)
    if Game.pause:
        pass
        Game.pauseGame()
        Game.pause = False
    while decision==True:
        print Game.status
        pygame.draw.line(scr,colour,(0,517),(600,517),1)    #draw the lines for progress bar
        Game.timer1+=1  #timer1 keeps track of overall game time
        Game.timer2+=Game.progressBarSpeed  #timer2 is increased based on progress bar's set speed
        Game.progressBarSpeed+=0.0000001  #The progress bar speed increases subtly
        if Game.timer2<6000:
            pygame.draw.rect(scr,colour,((0,517),(Game.timer2/10,6)), 0)    #the progress bar is drawn based on how fast timer2 increases
        else:
            Game.timer2=0   #reset timer2 when progress bar reaches the end
            Game.addLine(1) #add one row of new balls
        ev = event.poll()
        if ev.type == KEYDOWN and ev.key == K_ESCAPE:
            Game.pauseGame()  #pause game when ESC detected
            pygame.mouse.set_visible(False)
            decision=False
        elif ev.type == QUIT:
            quit();exit()   #quit
        elif ev.type == MOUSEMOTION:
            Arrow.update(ev.pos,eta)    #update arrow position
        elif ev.type==pygame.MOUSEBUTTONDOWN:
            sound.play()    #play pop sound when mouse is clicked
        Game.update()   #update the game
        if Game.status in (2,3):
            decision=False
        Animation.update()
        mainclock.tick(800) #determines the speed of the ball launched
        pygame.mouse.set_visible(False)

