'''
Bubble Fantasy Game

The link to the original game: http://www.pygame.org/project-pygame+bubble+shooter-1841-.html

Credits to Joel Murielle for the original game
'''


from classes.bubbleFantasy_game import *
from toolbox.lib.slidemenu import menu

'''
Pre: None
Post: Outputs message when game is over, and saves high score into text file if new high score is obtained by calling up saveHighScore()
Purpose: Outputs message when game is over, and saves high score into text file is new high score is obtained by calling up saveHighScore()
'''

def endGame():
    oldHighScore=int(readHighScore())
    if Game.status==1:
        label = endfont.render('New High Score: '+str(Game.multiplier*100*Game.score/3+(1/Game.timer1)*1000000) if (Game.multiplier*100*Game.score/3)> oldHighScore else'Game Over!' ,1,(255,255,255)) #Adds time bonus
    else: label = endfont.render('New High Score: '+str(Game.multiplier*100*Game.score/3) if (Game.multiplier*100*Game.score/3)> oldHighScore else'Game Over!' ,1,(255,255,255))
    rlabel = label.get_rect(center=ball_rect.center)
    scr.blit(label,rlabel)
    display.flip()
    if (Game.multiplier*100*Game.score/3)>oldHighScore and Game.status==1:
        saveHighScore(str(Game.multiplier*100*Game.score/3)+(1/Game.timer1)*1000000)
    elif (Game.multiplier*100*Game.score/3)>oldHighScore:
        saveHighScore(str(Game.multiplier*100*Game.score/3))
    if (Game.multiplier*100*Game.score/3)>0:
        addScore(str(Game.multiplier*100*Game.score/3))

'''
Pre: None
Post: Returns integer highScore read from text file
Purpose: Helper Function that reads in original high score
'''

def readHighScore():
    try:
        f=open('resources/bubbleFantasy_highScore.txt','r')
    except IOError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    else:
        highScore=f.read()
        f.close()
        return highScore

'''
Pre: Integer newHighScore
Post: Saves newHighScore into text file
Purpose: Saves new high score into text file
'''

def saveHighScore(newHighScore):
    try:
        f=open('resources/bubbleFantasy_highScore.txt','w')
    except IOError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    else:
        f.write(newHighScore)
        f.close()

'''
Pre: None
Post: Displays the text in help.txt on game screen
Purpose: Helper function that reads the content of help.txt and displays the text on game screen
'''

def help():
    label=[]
    counter=30
    try:
        f=open('resources/bubbleFantasy_help.txt','r')
    except IOError:
        print "resources/bubbleFantasy_help.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    else:
        lines=f.read().splitlines()
        for i in range (0,len(lines)):
            label.append(menu5font.render(lines[i],1,(255,255,255)))
            scr.blit(label[i],(30,counter))
            counter+=15
            display.flip()

'''
Pre: None
Post: Sorted list
Purpose: Helper function that sorts the scores
'''

def selectionSort (list): # Selection Sort Algorithm
    for i in range ( 0, len (list)):
        minimum = i
        for j in range ( i+1, len(list)):
            if list[j] < list[minimum] :
                minimum = j
        list[i], list[minimum] = list[minimum], list[i]
    return list

'''
Pre: String newScore
Post: Adds each score when game is over to bubbleFantasy_scoreList.txt
Purpose: Helper function that adds scores to bubbleFantasy_scoreList.txt
'''

def addScore(newScore):
    try:
        f=open('resources/bubbleFantasy_scoreList.txt','r')
    except IOError:
        print "resources/bubbleFantasy_scoreList.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    scoreList=[]
    scoreList=f.read().splitlines()
    f.close()
    scoreList.append(newScore)
    for i in range (0,len(scoreList)):
        scoreList[i]=int(scoreList[i])
    scorelList=selectionSort(scoreList)
    try:
        g=open('resources/bubbleFantasy_scoreList.txt','w')
    except IOError:
        print "resources/bubbleFantasy_scoreList.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    else:
        for j in range(0,len(scoreList)):
            g.write(str(scoreList[len(scoreList)-j-1]))
            g.write('\n')
        g.close()

'''
Pre: None
Post: Clears the text in bubbleFantasy_highScore.txt and bubbleFantasy_scoreList.txt
Purpose: Clear all saved scores
'''

def clearScores():
    try:
        f=open('resources/bubbleFantasy_scoreList.txt','w')
    except IOError:
        print "resources/bubbleFantasy_scoreList.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    else:
        f.write('')
        f.close()

    try:
        g=open('resources/bubbleFantasy_highScore.txt','w')
    except IOError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    else:
        g.write('0')
        g.close()

'''
Pre: None
Post: Displays the high scores from bubbleFantasy_scoreList.txt on game screen
Purpose: Displays high scores saved on text file onto game screen, called up when player needs to see high scores
'''

def viewHighScores():
    label=[]
    counter=50
    try:
        f=open('resources/bubbleFantasy_scoreList.txt','r')
    except IOError:
        print "resources/bubbleFantasy_scoreList.txt Not Found"
    except TypeError:
        print "resources/bubbleFantasy_highScore.txt Not Found"
    else:
        lines=f.read().splitlines()
        if len(lines)<15 and len(lines)!=0:#display all scores if number of scores less than 15
            for i in range(0,len(lines)):
                label.append(menu3font.render(lines[i],1,(224,255,255)))
                scr.blit(label[i],(270,counter))
                counter+=30
                display.flip()
        elif len(lines)>15: #only display the top 15 scores
            for i in range(0,15):
                label.append(menu3font.render(lines[i],1,(224,255,255)))
                scr.blit(label[i],(270,counter))
                counter+=30
                display.flip()
        else:
            noScore=menu2font.render('No Score Yet',1,(245,245,245))
            scr.blit(noScore,(240,300))
            display.flip()

'''
Pre: None
Post: Display game screen, initialize Game and run the main game loop
Purpose: To run the game and keep the game looping until the user quits
'''

def runGame():
    Game.mainDecision=True
    Game.mainDecision2=True

    decision = True
    decision2 = True
    decision3=False
    pygame.mixer.music.play(100,0.0)

    while Game.mainDecision==True and Game.mainDecision2==True:

        if decision==True and decision2==True:
            scr.blit(bg,screen)     #initialize screen
            gameTitle = menufont.render('Bubble Fantasy',1,(135,206,235))
            highScore=menu2font.render('High Score: '+readHighScore(),1,(245,245,245))
            scr.blit(gameTitle,(140,150))
            scr.blit(highScore,(190,200))
            display.flip()

            menu_ = ('Start Game','Help','View High Scores','Return to Game Suite Menu','Quit')   #Main menu
            pygame.mouse.set_visible(True)
            choice = menu(menu_,color1=(175,238,238),light=10,speed=300)[0]
            if choice == 'Quit': Game.mainDecision=False

            elif choice=='Return to Game Suite Menu':
                Game.mainDecision2=False
                pygame.mixer.music.stop()

            elif choice == 'Start Game':    #Initialize the game based on the difficulty chosen by player
                scr.blit(bg,screen)
                display.flip()
                help()
                menu_=('Continue to Game','','')
                choice5=menu(menu_,pos='bottomleft',font1=menu3font, color1=(200,200,200),light=10,justify=False,speed=0)[0]
                if choice5=='Continue to Game':
                    scr.blit(bg,screen)
                    display.flip()
                    title=menu2font.render('Choose a Difficulty Level',1,(135,206,235))
                    scr.blit(title,(180,200))
                    display.flip()
                    menu_ = ('Beginner','Easy','Normal','Hard','Impossible')#Let user choose difficulty level
                    choice3=menu(menu_,pos='center',font1=menu2font, color1=(200,200,200),light=10,justify=False,speed=0)[0]
                    if choice3!='Beginner' and choice3!='Easy' and choice3!='Normal' and choice3!='Hard' and choice3!='Impossible':
                        Game.mainDecision=False
                    else:
                        Game.init(choice3)
                        gameLoop()
                        if Game.status == 2:    #Ends game when the game's status indicates game over or new high score
                            print "A"
                            endGame()
                            decision2=False
                        elif Game.status in (2,3): print "B"; endGame(); decision2=False; decision3=True
                else: Game.mainDecision=False

            elif choice=='Help':    #Displays help for the player by calling up the function help()
                scr.blit(bg,screen)
                display.flip()
                help()
                menu_=('Return to Main Menu','','')
                choice4=menu(menu_,pos='bottomleft',font1=menu3font,color1=(200,200,200),light=10,justify=False,speed=0)[0]
                if choice4=='Return to Main Menu':
                    scr.blit(bg,screen)
                    display.flip()

            elif choice=='View High Scores':#Displays a list of the top 15 high scores
                title=menu2font.render('Top 15 High Scores',1,(245,245,245))
                scr.blit(bg,screen)
                scr.blit(title,(222,20))
                display.flip()
                viewHighScores()
                menu_=('Return to Main Menu','Clear All Scores','')#Allows user to clear all scores
                choice4=menu(menu_,pos='bottomleft',font1=menu3font,color1=(200,200,200),light=10,justify=False,speed=0)[0]
                if choice4=='Return to Main Menu':
                    scr.blit(bg,screen)
                    display.flip()
                elif choice4=='Clear All Scores':
                    clearScores()
                else:
                    Game.mainDecision=False

            else: Game.mainDecision=False

        if choice!='Help' and choice!='View High Scores':
            decision=False

        if Game.mainDecision==True and Game.mainDecision2==True and decision==False and decision2==True: #In-game pause menu, when game is not over
            menu_ = ('Resume Game','Restart Game','Help','Main Menu')
            pygame.mouse.set_visible(True)
            choice2 = menu(menu_,pos='bottomleft',font1=menu3font,color1=(200,200,200),light=10,justify=False,speed=0)[0]
            if choice2 == 'Main Menu':
                scr.blit(bg,screen)
                display.flip(); choice = None; decision=True
            elif choice2=='Resume Game':    #Resumes main game loop
                gameLoop()
                if Game.status == 2:
                    endGame(); decision2=False
                elif Game.status in (2,3): endGame(); decision2=False; decision3=True
            elif choice2=='Help':   #Displays help for the player by calling up the function help()
                scr.blit(bg,screen)
                display.flip()
                help()
                menu_=('Return to Game','','')
                choice4=menu(menu_,pos='bottomleft',font1=menu3font,color1=(200,200,200),light=10,justify=False,speed=0)[0]
                if choice4=='Return to Game':
                    scr.blit(bg,screen)
                    display.flip()
                    gameLoop()
                    if Game.status == 2:    #Ends game when the game's status indicates game over or new high score
                        endGame(); decision2=False
                    elif Game.status in (2,3): endGame(); decision2=False; decision3=True
            elif choice2=='Restart Game': #Re-initializes game and main loop if user wants to restart the game
                scr.blit(bg,screen)
                title=menu2font.render('Choose a Difficulty Level',1,(135,206,235))
                scr.blit(title,(180,200))
                display.flip()
                menu_ = ('Beginner','Easy','Normal','Hard','Impossible')#Let user choose difficulty level
                choice3=menu(menu_,pos='center',font1=menu2font, color1=(200,200,200),light=10,justify=False,speed=0)[0]
                if choice3!='Beginner' and choice3!='Easy' and choice3!='Normal' and choice3!='Hard' and choice3!='Impossible':
                    Game.mainDecision=False
                else:
                    Game.init(choice3)
                    gameLoop()
                    if Game.status == 2:    #Ends game when the game's status indicates game over or new high score
                        print "C"; endGame()
                    elif Game.status in (2,3): print "D"; endGame(); decision2=False

            else: Game.mainDecision=False

        elif Game.mainDecision==True and Game.mainDecision2==True and decision2==False: #In-game menu when game is over
            menu_ = ('Restart Game','Main Menu','')
            pygame.mouse.set_visible(True)
            if decision3==True: decision2=True
            choice2 = menu(menu_,pos='bottomleft',font1=menu3font,color1=(200,200,200),light=10,justify=False,speed=0)[0]
            if choice2 == 'Main Menu':  #Displays the main menu
                scr.blit(bg,screen)
                display.flip()
                choice = None;decision2=True;decision=True
            elif choice2=='Restart Game': #Re-initializes game and main loop if user wants to restart the game
                scr.blit(bg, screen)
                title=menu2font.render('Choose a Difficulty Level',1,(135,206,235))
                scr.blit(title,(180,200))
                display.flip()
                menu_ = ('Beginner','Easy','Normal','Hard','Impossible')#Let user choose difficulty level
                choice3=menu(menu_,pos='center',font1=menu2font, color1=(200,200,200),light=10,justify=False,speed=0)[0]
                if choice3!='Beginner' and choice3!='Easy' and choice3!='Normal' and choice3!='Hard' and choice3!='Impossible':
                    Game.mainDecision=False
                else:
                    Game.init(choice3)
                    gameLoop()
                    if Game.status == 2:    #Ends game when the game's status indicates game over or new high score
                        print "E"; endGame(); decision2=True
                    elif Game.status in (2,3):
                        print "F"; endGame(); decision2=False
            else: Game.mainDecision=False

    if Game.mainDecision2==True:
        quit()
        pygame.quit()


#For Testing Purposes#
#runGame()