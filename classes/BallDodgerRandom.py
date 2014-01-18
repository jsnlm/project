from classes2 import *

#pre:   mode must be a positive integer from 1 to 29
#post:  the game will run. Each time the palyer gets a yellow ball, "mode" number of obsticles will appear
#Purpose:   To run the game
def RandomMode(mode):
    Block.mainDecision=True

    #-------------------Instantiate variables and other things.---------------------------
    hScore = highscore()    #initiate Highscorse

    pygame.init()

    blockList = pygame.sprite.Group()

    allSpritesList = pygame.sprite.Group()  #initiate the a  sprite class that will contain all sprites that show on the screen


    player = Player(orange, 20, 20)         #initiate the player sprite
    allSpritesList.add(player)              #add the player to the "allSpriteList" group

    star = Star(yellow, 20, 20)             #initiate the star sprite
    starGroup = pygame.sprite.Group()       #add star to all "allSpriteList" group
    starGroup.add(star)
    allSpritesList.add(starGroup)
    star.update()                           #set the position of the star sprite

    itemGroup = pygame.sprite.Group()

    clock=pygame.time.Clock()

    #-------------------Instantiate fonts that will be sued for blitted text.---------------------------
    scoreFont = pygame.font.Font(None, 36)
    itemFont = pygame.font.Font(None, 35)
    gameOverFont1 = pygame.font.Font(None, 100)
    gameOverFont2 = pygame.font.Font(None, 35)
    InstructionsFont = pygame.font.Font(None, 40)

    score = 0                               #set the players score to 0
    blockUpdateCounter = 0                  #block update counter set to 0. This is used to check how many loops must be run before obsticle is updated (moved)

    waitingTimeItem = random.randrange(1,5) #sets the first waiting time for when item appears
    currentItem = 0                         #sets  current item to 0
    itemTimer = 0

    InstructionsPic1 = image.load("resources/InstructionPic1.png")
    InstructionsPic2 = image.load("resources/InstructionPic2.png")
    explosionPic = image.load("resources/explosion.png")   #sets up the explosion image for the explosion item

    #-------------------Instantiate sounds for the game.---------------------------

    #this stuff sets up the channels for the game
    BoomSounds= pygame.mixer.Channel(0)
    VoiceSounds= pygame.mixer.Channel(1)
    #explosionchannel = pygame.mixer.Channel(1)

    #this stuff sets up the actual sound files for the game
    gameOver = pygame.mixer.Sound("resources/gameOver.wav")
    boom = pygame.mixer.Sound("resources/boom.wav")
    Nice  = pygame.mixer.Sound("resources/Nice.wav")
    Invisibility = pygame.mixer.Sound("resources/Invisibility.wav")
    goodJob  = pygame.mixer.Sound("resources/goodJob.wav")
    excellent = pygame.mixer.Sound("resources/excellent.wav")
    Invincible = pygame.mixer.Sound("resources/Invincible.wav")
    Losing = pygame.mixer.Sound("resources/Losing.wav")
    explosion = pygame.mixer.Sound("resources/explosion.wav")



    #sets done to false to start the loop that the game runs.
    done=False
    global gameover
    gameover = False
    continu= False


    while continu == False and done==False :
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True
                Block.mainDecision=False

        screen.blit(InstructionsPic1, [0, 0])

        InstructionText=InstructionsFont.render("click anywhere to Continue", True, red)
        screen.blit(InstructionText, [(screen_width/2-170), 550])

        press = pygame.mouse.get_pressed()

        if press[0] == 1:
            continu = True

        pygame.display.flip()
    continu = False

    press = pygame.mouse.get_pressed()
    while press[0] == 1:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True
                Block.mainDecision=False
        press = pygame.mouse.get_pressed()



    while continu == False and done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True
                Block.mainDecision=False
        screen.blit(InstructionsPic2, [0, 0])

        InstructionText=InstructionsFont.render("click anywhere to Continue", True, red)
        screen.blit(InstructionText, [(screen_width/2-170), 600])

        press = pygame.mouse.get_pressed()

        if press[0] == 1:
            continu = True

        pygame.display.flip()
    continu = False



    while done==False:
        pygame.mouse.set_visible(True)         #make the mouse invisible on the screen

        # -----------------This happens when player collides with an obsticle and loses.----------------------------------
        while gameover == True:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    gameover = False
                    done=True # Flag that we are done so we exit this loop
            #allSpritesList.empty()
                    Block.mainDecision=False

            #---------This will print text to the screen after the player loses
            gameOverText=gameOverFont1.render("Game Over", True, red)
            screen.blit(gameOverText, [(screen_width/2-190), (screen_height/2 - 30)])

            gameOverText=gameOverFont2.render("click anywhere to restart", True, red)
            screen.blit(gameOverText, [(screen_width/2-170), (screen_height/2 + 60)])

            press = pygame.mouse.get_pressed()

            if press[0] == 1:
                gameover = False

                star = Star(yellow, 20, 20)             #initiate the star sprite
                starGroup = pygame.sprite.Group()       #add star to all "allSpriteList" group
                starGroup.add(star)
                star.update()

                #This will reset the sprites in the game
                blockList.empty()
                allSpritesList.empty()
                allSpritesList.add(blockList)
                allSpritesList.add(starGroup)
                allSpritesList.add(player)
                waitingTimeItem = random.randrange(1,5) #sets the first waiting time for when item appears

                score = 0                               #reset the players score to 0

            pygame.display.flip()

        pygame.mouse.set_visible(False)         #make the mouse invisible on the screen

        while (gameover == False) and (done==False):
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop
                    gameover = True
                    Block.mainDecision=False
            screen.fill(black)  #set coulour of the screen


            player.update()     #updates(moves) the player

            if blockUpdateCounter%20 == 0:  #every time the loop is run 20 times, the ball will be updated (moved)
                blockList.update()
                #starGroup.update()

            blockUpdateCounter += 1


            if currentItem == 3:    #if the item is invisible, then don't check nothing will happen if player colides with obsticle
                blackBallHitList = pygame.sprite.spritecollide(player, blockList, False)

            elif currentItem == 2:    #if the item is invisible, then don't check nothing will happen if player colides with obsticle
                blackBallHitList = pygame.sprite.spritecollide(player, blockList, True)

            else :                  #if the item is NOT invisible, then hit list is updated when player colides with obsticle
                blackBallHitList = pygame.sprite.spritecollide(player, blockList, False)

            yellowBallHitList= pygame.sprite.spritecollide(player, starGroup, False)    #checks if player colided with star
            itemHitList= pygame.sprite.spritecollide(player, itemGroup, False)          #checks if player colided with item

            #-------------------what happends when player htis the yellow ball---------------------------
            if len(yellowBallHitList) != 0:
                #print "you collided with star"

                star.update()   #changes the position of the yellowball

                #This for loop will add "mode" obsticles in the game.
                for x in range(mode):

                    #This part adds a obsticle to the game
                    obsticRadius = (random.randrange(1, 8))*10                      #sets random radisus for ball
                    obstic = obsticle(neonTurquoise, obsticRadius, obsticRadius)    #makes an instant of a obsticle sprite

                    pos = pygame.mouse.get_pos()    #finds the position of the mouse
                    blockPlayerMargin = 150         #a set boundary for obsticles to spawn

                    #finds a x value that is beyond the set blockPlayerMargin
                    obstic.rect.x = random.randrange(screen_width)
                    while (obstic.rect.x<(pos[0] +blockPlayerMargin)) and (obstic.rect.x>(pos[0] -blockPlayerMargin)):
                        obstic.rect.x = random.randrange(screen_width)

                    #finds a y value that is beyond the set blockPlayerMargin
                    obstic.rect.y = random.randrange(screen_height)
                    while (obstic.rect.y<(pos[1] +blockPlayerMargin)) and (obstic.rect.y>(pos[1] -blockPlayerMargin)):
                        obstic.rect.y = random.randrange(screen_height)

                    blockList.add(obstic)           #add obsticle to blocklist
                    allSpritesList.add(obstic)      #add obsticle to all allSpritesList


                score +=1       #the player get 1 more point

                #This will play a randome congradulatory message when each time the player gets 10 yellow balls
                if score%10 == 0 and score!= 0:
                    messageNumber = random.randrange(0, 3)      #sets randm message
                    if messageNumber == 0:
                        VoiceSounds.play(Nice)                  #paly the "nice" sound
                    elif messageNumber == 1:
                        VoiceSounds.play(goodJob)               #plays the "good job" sound
                    elif messageNumber == 2:
                        VoiceSounds.play(excellent)             #plays the "excellent" sound

                waitingTimeItem -= 1                    #subtracts 1 from the waiting time for an item

                if waitingTimeItem == 0:                #if waiting time is finanly 0, the item sprite is instantiated, added to item group and allPrites class.
                    item = Item(20, 20)
                    itemGroup.add(item)
                    allSpritesList.add(itemGroup)
                    item.update()

            #-------------------what happends when player htis the item---------------------------
            if len(itemHitList) != 0:

                currentItem = item.getItemNumber()      # get the item number of the item
                itemGroup.empty()                       #gets rid of the item
                #currentItem = 2

                #---------item number = 2 = Invincible----------
                if currentItem == 2 :
                    itemTimer = 1500
                    player.setInvincibleImage()         #change player appearance to see through
                    VoiceSounds.play(Invincible)
                #---------item number = 2 = bomb----------
                if currentItem == 1 :
                    itemTimer = 50
                #---------item number = 2 = invisible----------
                if currentItem == 3 :
                    itemTimer = 3000
                    VoiceSounds.play(Invisibility)         #change player appearance to see through
                    player.setInvisibleImage()


                #Takes out all sprite groups and then adding back. This is to get rid of the itemgroup
                allSpritesList.empty()
                allSpritesList.add(blockList)
                allSpritesList.add(starGroup)
                allSpritesList.add(player)
                waitingTimeItem = random.randrange(1,10)
                #waitingTimeItem = 1

            #---------------This is to change the image of the player back to normal-------------------
            #---------------so that the player doesn't look like it has an item-------------------
            if currentItem != 0:
                if itemTimer <= 0:
                    currentItem = 0
                    player.setImageNormal()

            #---------------activates when there is a collision between player and obsticle.
            #---------------Also, the player has to have no items at the moment
            if len(blackBallHitList) != 0:
                if currentItem == 0:
                    #emptying all the sprites so that they don't show up on the screen
                    allSpritesList.empty()
                    #blockList.empty()
                    starGroup.empty()
                    itemGroup.empty()
                    #re include the player and block sprites
                    allSpritesList.add(player)
                    allSpritesList.add(blockList)

                    gameover = True

                    #play the game over sound
                    VoiceSounds.play(gameOver)

                    if score>hScore.getScore(mode):     #This will save the player's score if it is higher than the curren highscore
                        hScore.setScore(mode, score)
                        hScore.saveEverything()
                blackBallHitList = 0                    #resets the blackBallHitList


            #---------------This is what happens when the player has the bomb item---------------
            if currentItem == 1:
                if itemTimer ==50:  #this if statement happens when the player just got the item.
                    BoomSounds.play(explosion)
                    explosionPosition = pygame.mouse.get_pos()
                    for block in blockList :        #this for loop checks for the
                        if ((block.rect.x - explosionPosition[0])**2 + (block.rect.y - explosionPosition[1])**2) < (125 + block.getWidth())**2:
                            blockList.remove(block)

                    allSpritesList.empty()
                    allSpritesList.add(blockList)
                    allSpritesList.add(starGroup)
                    allSpritesList.add(player)

                #the explosion  picture will be on the screen for 50 run throughs of this loop
                screen.blit(explosionPic, [explosionPosition[0]-125, explosionPosition[1]-125])




            allSpritesList.draw(screen)         #draws the sprites to the screen

            #--------------The following prints text onto the screen


            text=scoreFont.render("Score: "+str(score), True, white)        #prints the player's score
            screen.blit(text, [10, 10])

            if score>hScore.getScore(mode):
                text=scoreFont.render("Highscore: "+str(score), True, white)#prints the highscore
            else:
                text=scoreFont.render("Highscore: "+str(hScore.getScore(mode)), True, white)        #if the player's highscore is larger than the current highscore, the player's score will be printed instead of highscore.
            screen.blit(text, [(screen_width - 200), 10])

            #----------------prints the player's item to the screen, whether it bomb, invincible or Invisible.
            if currentItem == 0:
                itemText=itemFont .render("ITEM: "+ "____", True, white)
            elif currentItem == 1:
                itemText=itemFont .render("ITEM: "+ "Bomb", True, white)
            elif currentItem == 2:
                itemText=itemFont .render("ITEM: "+ "Invincible", True, white)
            elif currentItem == 3:
                itemText=itemFont .render("ITEM: "+ "Invisible", True, white)
            screen.blit(itemText, [(screen_width/2-90), (screen_height -25)])

            #---------------This is a bar that represents that amount of time left of the player's item.
            if itemTimer >=0:
                pygame.draw.rect(screen,white,((0,(screen_height -25)),(itemTimer/6,25)), 1)


            itemTimer -= 1      #each run through of the program means the timer decreases

            pygame.display.flip()

    pygame.quit()
    Block.mainDecision=False
