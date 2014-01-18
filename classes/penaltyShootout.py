import sys, pygame, math
from pygame import*

class Decision():
    def __init__():
        Decision.decision=True

def main():
    pass

#Pre: N/A
#Post: Runs the game, Pentaly Shootout, by using pygame (Graphic User Interface). Pops up a seperate screen.
#Purpose: In order to efficiently run the program.

def SoccerGame():                                       # a function named "SoccerGame", which has other functions that is needed to run the program
    white    = (255, 255, 255)                          # making a variable with colour information, white
    black    = (  0,   0,   0)                          # making a variable with colour information, black
    red      = (255,   0,   0)                          # making a variable with colour information, red
    blue     = (  0,   0, 205)                          # making a variable with colour information, blue
    yellow   = (255, 255,   0)                          # making a variable with colour information, yellow
    pink     = (255,  20, 147)                          # making a variable with colour information, pink
    lime_green = (0,  255,  0)                          # making a variable with colour information, lime green
    orange_red = (255, 69,  0)                          # making a variable with colour information, orange red
    grey  =  (105,  105,  105)                          # making a variable with colour information, grey


    windowWidth = 980                                   # width of the program's window, in pixels
    windowHeight = 653                                  # height of the program's window, in pixels

    pointHorizontal = int(windowWidth / 2) + 7          # to set a point in the window of the program <horizontal>
    pointVertical = int(windowHeight * 9/10)            # to set a point in the window of the program <horizontal>

    pygame.init()                                       #initializing pygame

    screen = pygame.display.set_mode((windowWidth, windowHeight))                   # setting a screen size according to the window height & width

    background = image.load('resources/soccerfield.jpg').convert_alpha()            # loading image of the "background", made the image transparent
    ball = image.load('resources/Ball_1.png').convert_alpha()                       # loading image of the "ball", made the image transparent
    goalkeeper = image.load('resources/Goalkeeper.png').convert_alpha()             # loading image of the "goalkeeper", made the image transparent
    mouse = image.load('resources/Mouse.png').convert_alpha()                       # loading image of the "mouse", made the image transparent
    logo = image.load('resources/Logo.png').convert_alpha()                         # loading image of the "logo", made the image transparent
    soccernet = image.load('resources/Soccernet.png').convert_alpha()               # loading image of the "soccernet", made the image transparent

    running = 1                                                                     # a variable that indicates if the program should keep run or not
    score = 0                                                                       # a variable that keeps the score of the user
    level = 1                                                                       # a variable that shows the current level of the user
    instruction_page = 1                                                            # the initial number of insturction pages at first
    posOfGoalkeeper = 330                                                           # the initial position of the goalkeeper
    speedOfGoalkeeper = 300                                                         # the initial speed of the goalkeeper
    clock = pygame.time.Clock()                                                     # a variable that holds the functions of pygame "clock"
    font_gameover = pygame.font.Font(None, 100)                                     # the font specification of the game_over text
    game_over = False                                                               # a boolean value that shows if the game is over or not
    scored = False                                                                  # a boolean value that shows if the use scored or not
    done = False                                                                    # loop until the user clicks the close button
    pause = False
    display_instructions = True                                                     # a boolean value that shows if the program should show the instruction on the screen or not
    font = pygame.font.Font(None, 36)                                               # the details of the font used in the program

    class Soccernet(pygame.sprite.Sprite):                                          # a class named "Soccernet" which holds the positions of the soccernet

        def __init__(self):
            # Call the parent class (Sprite) constructor
            pygame.sprite.Sprite.__init__(self)
            self.image = soccernet
            self.rect = self.image.get_rect()
            self.rect.x = 312                                                       # the position of the soccernet (horizontal)
            self.rect.y = 23                                                        # the position of the soccernet (vertical)

    class Goalkeeper(pygame.sprite.Sprite):                                         # a class named "Goalkeeper" which holds the positions of the goalkeeper

        def __init__(self):
            # Call the parent class (Sprite) constructor
            pygame.sprite.Sprite.__init__(self)
            self.image = goalkeeper
            self.rect = self.image.get_rect()
            self.rect.x = posOfGoalkeeper                                           # the position of the soccernet (horizontal)
            self.rect.y = 30                                                        # the position of the soccernet (vertical)

    class Player(pygame.sprite.Sprite):                                             # a class named "Player" which holds the image of the player

        def __init__(self):
            self.mainDecision = True
            self.mainDecision2 = True
            # Call the parent class (Sprite) constructor
            pygame.sprite.Sprite.__init__(self)
            self.image = image.load('resources/Soccer_player.png').convert_alpha()  # loading image of the "soccer player", made the image transparent
            self.rect = self.image.get_rect()

    class Ball(pygame.sprite.Sprite):                                             # a class named "Ball" which holds the image of the player

        def __init__(self):
            # Call the parent class (Sprite) constructor
            pygame.sprite.Sprite.__init__(self)
            self.image = image.load('resources/Ball_1.png').convert_alpha()         # loading image of the "ball", made the image transparent
            self.rect = self.image.get_rect()

    all_sprites_list = pygame.sprite.Group()                                        # a variable that holds the information of all sprites (to check if it collides or not)
    ball_list = pygame.sprite.Group()                                               # a variable that holds the information of ball <sprite> (to check if it collides or not)
    soccernet_list = pygame.sprite.Group()                                          # a variable that holds the information of soccernet <sprite> (to check if it collides or not)
    player = Player       ()                                                        # calls up the "Player" class
    all_sprites_list.add(player)                                                    # adds the player <sprite> to the all_sprites_list
    net = Soccernet()                                                               # calls up the "Soccernet" class
    keeper = Goalkeeper()                                                       # calls up the "Goalkeeper" class

    while done == False and display_instructions:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
                Decision.decision = False
            if event.type == pygame.MOUSEBUTTONDOWN:                                # if the user presses down a mouse button
                instruction_page += 1                                               # adding one more page to the instruction page
                if instruction_page == 3:                                           # when the instruction page becomes page 3
                    display_instructions = False                                    # set the boolean value to false
        screen.fill(black)                                                          # Set the screen background
        if instruction_page == 1:
            # Draw instructions, page 1
            text=font.render("Welcome to the Soccer Penalty Shoot-Out Game", True, white)
            screen.blit(text, [10, 10])                                             # shows the text on the screen
            text=font.render("This game is part of the Ball Game Suite, a game suite made by Castor.", True, white)
            screen.blit(text, [10, 40])                                             # shows the text on the screen
            text=font.render("Click to move on. ->", True, white)
            screen.blit(text, [10, 130])                                             # shows the text on the screen
        if instruction_page == 2:
            # Draw instructions, page 2
            text=font.render("This program is made by Phillip Lee.", True, white)
            screen.blit(text, [10, 10])                                             # shows the text on the screen
            text=font.render("Here are the instruction for this game.", True, white)
            screen.blit(text, [10, 40])                                             # shows the text on the screen
            text=font.render("The main objective of this game is to score the soccer ball into the net.", True, white)
            screen.blit(text, [10, 70])                                             # shows the text on the screen
            text=font.render("First of all, you can move your mouse to adjust the position of the forward/ball.", True, white)
            screen.blit(text, [10, 100])                                             # shows the text on the screen
            text=font.render("You can click your mouse to shoot the ball.", True, white)
            screen.blit(text, [10, 130])                                             # shows the text on the screen
            text=font.render("You should try to avoid the goalkeeper who will block the ball.", True, white)
            screen.blit(text, [10, 160])                                             # shows the text on the screen
            text=font.render("The level of the game will get harder for every 5 goals you score.", True, white)
            screen.blit(text, [10, 190])                                             # shows the text on the screen
            text=font.render("Good luck~!. And enjoy the game!", True, white)
            screen.blit(text, [10, 220])                                             # shows the text on the screen
            text=font.render("Click to begin the game. ->", True, white)
            screen.blit(text, [10, 310])                                             # shows the text on the screen
        clock.tick(20)                                                            # Limit to 20 frames per second
        pygame.display.flip()                                                     # update the screen

    Decision.decision = True
    Player.mainDecision = True
    Player.mainDecision2 = True

    while Player.mainDecision==True and Player.mainDecision2==True:                                                                # if the program is still running. boolean value of "running" is 1.
        mousePosX, mousePosY = pygame.mouse.get_pos()                             # gets the position of the mouse cursor
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            Decision.decision=False
            running = 0
        if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        if pause==False:
                            pause=True
                            posOfGoalkeeper = 330
                        else:
                            pause=False
                            posOfGoalkeeper = 330
        elif event.type == pygame.MOUSEBUTTONDOWN and pause == False:                                # if the user presses down a mouse button
            ball = Ball()                                                         # calls up the "Ball" class
            ball.rect.x = player.rect.x                                           # gets the size of the ball
            ball.rect.y = player.rect.y                                           # gets the size of the ball
            all_sprites_list.add(ball)                                            # adds the ball <sprite> to the all_sprites_list
            ball_list.add(ball)                                                   # adds the ball <sprite> to the ball_list
            soccernet_list.add(ball)                                              # adds the ball <sprite> to the soccernet_list

        if len(pygame.sprite.spritecollide(net, soccernet_list, True))!= 0 :      # if the ball collides with the soccernet
            scored = True                                                         # set the value of boolean "scored" to True
            game_over = False                                                     # set the value of boolean "game_over" to False
            score = score + 1                                                     # score goes up by 1
        elif len(pygame.sprite.spritecollide(keeper, soccernet_list, True))!= 0 : # if the ball collides with the goalkeeper
            game_over = True                                                      # set the value of boolean "game_over" to True
            scored = False                                                        # set the value of boolean "scored" to False

        if pause == False:
            if score < 5:                                                             # if the score is less than 5
                current_level = font.render("Level" + "<"+ str(level) + ">", True, lime_green)  #gets the current level
                milli = clock.tick()
                seconds = milli/1000.                                                    # the speed of the goalkeeper
                dm = seconds * speedOfGoalkeeper
                posOfGoalkeeper += dm
            elif score < 10:                                                             # if the score is less than 10
                level = 2                                                                # level two
                current_level = font.render("Level" + "<"+ str(level) + ">", True, lime_green)  #gets the current level
                milli = clock.tick()
                seconds = milli/800.                                                     # the speed of the goalkeeper
                dm = seconds * speedOfGoalkeeper
                posOfGoalkeeper += dm
            elif score < 15:                                                             # if the score is less than 15
                level = 3                                                                # level three
                current_level = font.render("Level" + "<"+ str(level) + ">", True, lime_green)  #gets the current level
                milli = clock.tick()
                seconds = milli/600.                                                     # the speed of the goalkeeper
                dm = seconds * speedOfGoalkeeper
                posOfGoalkeeper += dm
            elif score < 20:                                                             # if the score is less than 20
                level = 4                                                                # level four
                current_level = font.render("Level" + "<"+ str(level) + ">", True, lime_green)  #gets the current level
                milli = clock.tick()
                seconds = milli/400.                                                     # the speed of the goalkeeper
                dm = seconds * speedOfGoalkeeper
                posOfGoalkeeper += dm

            elif score < 25:                                                             # if the score is less than 25
                level = 5                                                                # level five
                current_level = font.render("Level" + "<"+ str(level) + ">", True, lime_green)  #gets the current level
                milli = clock.tick()
                seconds = milli/200.                                                     # the speed of the goalkeeper
                dm = seconds * speedOfGoalkeeper
                posOfGoalkeeper += dm

            elif score > 24:
                game_over = True                                                         # set the value of boolean "game_over" to True

            pos = pygame.mouse.get_pos()                                                 # the position of the mouse
            player.rect.x = pos[0]                                                       # moves the player to the position of the mouse's position
            player.rect.y = 550                                                          # the vertical position of the player is always constant

        else:
            posOfGoalkeeper += 0
            if pause == False:
                posOfGoalkeeper = 330

        keeper = Goalkeeper()                                                        # calls up the "Goalkeeper" class

        if posOfGoalkeeper > 660:                                                    # if the position of the goalkeeper is more than 660
            speedOfGoalkeeper = -300                                                 # the direction of the goalkeeper is reversed
        if posOfGoalkeeper < 330:                                                    # if the position of the goalkeeper is less than 330
            speedOfGoalkeeper = 300                                                  # the direction of the goalkeeper is reversed

        for ball in ball_list:
            ball.rect.y -= 1.2                                                       # Move the ball up

        screen.blit(background,(0,0))                                                # displays the image "background" at a certain position on the window screen
        screen.blit(logo,(770,25))                                                   # displays the image "logo" at a certain position on the window screen
        screen.blit(soccernet,(312,23))                                              # displays the image "soccernet" at a certain position on the window screen
        screen.blit(goalkeeper, (posOfGoalkeeper, 50))                               # displays the image "goalkeeper" at a certain position on the window screen
        screen.blit(mouse,(mousePosX-15, mousePosY-15))                              # displays the image "mouse" at a certain position on the window screen
        screen.blit(current_level, [50, 50])                                         # displays the text "current_level" at a certain position on the window screen
        current_score = font.render("You have scored "+ str(score) + " goal(s)!", True, blue)
        screen.blit(current_score, [20, 600])                                        # displays the text "current_score" at a certain position on the window screen
        all_sprites_list.draw(screen)                                                # displays all the sprites onto the screen

        if scored:                                                                   # if the user scored
            if score < 25:                                                           # when the score is less than 25
                text = font_gameover.render("Goal!", True, yellow)
                text_rect = text.get_rect()
                text_x = screen.get_width()/2 - text_rect.width/2
                text_y = screen.get_height()/2 - text_rect.height/2
                screen.blit(text, [text_x, text_y])
        if game_over:                                                                # if the game is over (by winning the game)
            if score > 24:                                                           # when the score is more than 24
                text = font_gameover.render("You Won!!", True, red)
                text_rect = text.get_rect()
                text_x = screen.get_width()/2 - text_rect.width/2
                text_y = screen.get_height()/2 - text_rect.height/2
                screen.blit(text, [text_x, text_y])
                running = 0                                                          # stop the program to run by setting the variable "running" to 0
            else:                                                                    # if the game is over (by collision with the goalkeeper)
            # If game over is true, draw game over
                text = font_gameover.render("Game Over", True, red)
                text_rect = text.get_rect()
                text_x = screen.get_width()/2 - text_rect.width/2
                text_y = screen.get_height()/2 - text_rect.height/2
                screen.blit(text, [text_x, text_y])
                final_score = font.render("Your final score is " + str(score) + "!", True, orange_red)
                screen.blit(final_score, [50, 550])                                  # displays the text "final_score" at a certain position on the window screen
                mousex,mousey=pygame.mouse.get_pos()
                pause = True
        if pause == False:
            pygame.display.flip()
                                                                    # updates the screen
        else:
            mousex,mousey=pygame.mouse.get_pos()
            if mousex>110 and mousex<203 and mousey>300 and mousey<319:
                mousecolor1=black
            else:
                mousecolor1=white
            if mousex>110 and mousex<361 and mousey>325 and mousey<342:
                mousecolor2=black
            else:
                mousecolor2=white
            screen.blit(font.render("Resume", True, mousecolor1,),[110, 300])
            screen.blit(font.render("Return to Main Menu", True, mousecolor2,),[110, 325])
            pygame.display.flip()
            for event in pygame.event.get(): # User did something
                if event.type == pygame.MOUSEBUTTONDOWN and pause==True:                                # if the user presses down a mouse button
                    if mousex>110 and mousex<203 and mousey>300 and mousey<319:
                        pause=False
                        posOfGoalkeeper = 330
                    elif mousex>110 and mousex<361 and mousey>325 and mousey<342:
                        screen = pygame.display.set_mode([600,674])
                        screen = Rect(0,0,600,674)
                        Player.mainDecision2=False

    if Player.mainDecision2==True:
        Decision.decision=False


if __name__ == '__main__':
    main()
    SoccerGame()