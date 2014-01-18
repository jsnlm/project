from classes.bubbleFantasy_game import *
from classes.mainBallDodger import *
from classes.bubbleFantasy_run import *
from classes.penaltyShootout import *
from classes.NGPong import *
from toolbox.lib.slidemenu import menu

'''
Castor Game Suite

This file runs the menu that allows you to play all the available games in
the suite. The games are Bubble Fantasy, Ball Dodger, Pong and Penalty Shootout.
'''
menuDecision=True

while menuDecision==True:
    title=menufont.render('Castor Game Suite',1,(255,255,255))
    title2=menu5font.render('Pick any of the games below to get started',1,(255,255,255))
    scr.blit(bg, screen)
    scr.blit(title,(105,80))
    scr.blit(title2,(135,130))
    display.flip()
    menu_=('Bubble Fantasy','Ball Dodger','Pong', 'Penalty Shootout')
    pygame.mouse.set_visible(True)
    choice = menu(menu_,color1=(255,255,255),light=10,speed=300)[0]
    if choice=='Ball Dodger':
        scr.blit(bg,screen)
        display.flip()
        pygame.display.set_caption('Ball Dodger')
        menu_=('Easy','Medium','Hard')
        choice2=menu(menu_,color1=(175,238,238),light=10,speed=300)[0]
        if choice2!='Easy' and choice2!='Medium' and choice2!='Hard':
            menuDecision=False
        else:
            scores = highscore()
            ballDodgerRun(choice2, scores )
            if scores.mainDecision==False:
                menuDecision=False
    elif choice=='Bubble Fantasy':
        pygame.display.set_caption('Bubble Fantasy')
        runGame()
        if Game.mainDecision==False:
            menuDecision=False
    elif choice=='Pong':
        pygame.display.set_caption('Pong')
        PongGame()
        if GGame.mainDecision==False:
            menuDecision=False
    elif choice=='Penalty Shootout':
        pygame.display.set_caption('Penalty Shootout')
        SoccerGame()
        if Decision.decision==False:
            menuDecision=False
    else: menuDecision=False

quit()
pygame.quit()

