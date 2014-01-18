#-------------------------------------------------------------------------------
# Name:                 Classes 2
# Purpose:              This file is a series of classes and other things related to the game.
#                       They are the utilities of the game containing all important classes, pygame settings, colurs, Mixers, etc.
# Date                  May, 30, 2013
# To be Submitted to:   Ms. Wun
# Created by:           Jason Lam
#-------------------------------------------------------------------------------

#importing different libraries that wil be used including pygame, random and time
import pygame
import random
import time
from pygame import *


#----------presetting colors for the program.
#----------This makes it easier to change colours of sprites and to write down colour names
#colour = red green blue
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
purple   = ( 255, 120, 255)
red      = ( 255,   0,   0)
yellow      = ( 255,   255,   0)
neonTurquoise = (0, 255, 255)
orange = (255, 127, 0)

#----------Setting up graphic variables
global screen_width
global screen_height
screen_width=600
screen_height=663
screen=pygame.display.set_mode([screen_width,screen_height])
global highscores

#-----------Mixer is set up to allow sound in the game
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.mixer.init()




#The block class is a sprite class that all other sprites inherit from
#This sets up a default image, and basic sprite functions - getWidth & getHeight
class Block(pygame.sprite.Sprite):


    #pre: colour must be a colour code, width and height must be resonable to relative to screen size and other Sprites.
    #post: sprite is initiated with correct parameters.
    #Purpose: To initiate a Black Sprite
    def __init__(self, color, width, height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height], pygame.SRCALPHA,32)
        #self.image.fill(color)
        pygame.draw.circle(self.image,color,(width/2,height/2),width/2,1)
        self.rect = self.image.get_rect()

        self.height = height
        self.width = width
    #pre:
    #post: self.width is returned
    #Purpose:to find the width of the sprite
    def getWidth(self):
        return self.width
    #pre:
    #post: self.height is returned
    #Purpose:to find the height of the sprite
    def getHeight(self):
        return self.height

class obsticle(Block):
    #pre: colour must be a colour code, width and height must be resonable to relative to screen size and other Sprites.
    #post:Obsticleis initiated. This includes the random placement and direction of the Sprite
    #Purpose:TO initiate and obsticle with random position and velocity.
    def __init__(self, color, width, height):
        Block.__init__(self, color, width, height)
        self.y = random.randrange(0, 2)     #to set whether the obsticle is starts off moving up or down
        self.x = random.randrange(0, 2)     #to set whether the obsticle is starts off moving left or right
        self.xMovement = random.randrange(1, 3) #to set x speed of obsticle
        self.yMovement = random.randrange(1, 3) #to set y speed of obsticle

    #pre:
    #post: To move the obsticle. This includes bouncing off walls, and moving at the set speed.
    #Purpose: to move the obsticle

    def update(self):

        #---------------this part will update the x direction---------------
        if  self.x == 0:    #what happens when x direction is set to "right"
            self.rect.x +=  self.xMovement      #positon is moved "right" by the movement distance
            if self.rect.x > screen_width - self.width: #if the obsticle has reached the wall, it must change direction
                self.x = 1
        elif  self.x == 1:    #what happens when x direction is set to "left"
            self.rect.x -=  self.xMovement      #positon is moved "left" by the movement distance
            if self.rect.x < 0:             #if the obsticle has reached the wall, it must change direction
                self.x = 0


        if  self.y == 0:    #what happens when x direction is set to up
            self.rect.y +=  self.yMovement#positon is moved up by the movement distance
            if self.rect.y > screen_height - self.height:#if the obsticle has reached the wall, it must change direction
                self.y = 1
        elif  self.y == 1:  #what happens when x direction is set to down
            self.rect.y -=  self.yMovement #positon is moved down by the movement distance
            if self.rect.y < 0:             #if the obsticle has reached the wall, it must change direction
                self.y = 0

#the player class is inherites from the block class
#it represents the player in the ball dodger game
class Player(Block):
    #pre: colour must be a colour code, width and height must be resonable to relative to screen size and other Sprites.
    #post:Obsticle is initiated. This includes images that represent different power ups.
    #Purpose:TO initiate and obsticle with various images( for when there are different items)
    def __init__(self, color, width, height):
        Block.__init__(self, color, width, height)
        self.invincibleImage = image.load('resources/Invincible.png')                  #inivincible image is loaded from file
        self.normalImage = pygame.Surface([width, height], pygame.SRCALPHA,32)      #Normal image is set. This is just a filled in orange
        self.invisibleImage = pygame.Surface([width, height], pygame.SRCALPHA,32)   #invisible image is set. This is just a hollow orange
        pygame.draw.circle(self.image,color,(width/2,height/2),width/2,0)
    #pre: mouse must be plugged int othe computer
    #post:  This will move the player to the position of the mouse
    #Purpose:To make the player follow the mouse.
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    #pre:
    #post: image is set to self.normalImage
    #Purpose:to set the image of the player sprite to normal
    def setImageNormal(self):
        self.image = self.normalImage
        pygame.draw.circle(self.image,orange,(20/2,20/2),20/2,0)
        self.rect = self.image.get_rect()
    #pre:
    #post: image is set to self.invisibleImage
    #Purpose:to set the image of the player sprite to hollow orange circle (invisibleImage)
    def setInvisibleImage(self):
        self.image = self.invisibleImage
        pygame.draw.circle(self.image,orange,(20/2,20/2),20/2,1)
        self.rect = self.image.get_rect()
    #pre:
    #post: image is set to self.invincibleImage
    #Purpose:to set the image of the player sprite to 'Invincible.png'
    def setInvincibleImage(self):
        self.image = self.invincibleImage
        self.rect = self.image.get_rect()

    #pre:
    #post: x position of player is returned
    #Purpose:x position of player is returned
    def getXPosition(self):
        return self.rect.x

    #pre:
    #post: y position of player is returned
    #Purpose:y position of player is returned
    def getYPosition(self):
        return self.rect.y

#This is the star class
#note: it is called star because that was the original plan for the image of now, yellow circle
#this inherits from the block class
class Star(Block):
    #pre:
    #post:  moves the star to a random position on the screen.
    #Purpose:   Changed the position of the star after player has come in contact with it
    def update(self):
        self.rect.x=random.randrange(screen_width - 15)     #sets random value for x position
        self.rect.y=random.randrange(40, screen_height - 55)      #sets random value for y position

#this is the item class
class Item(Block):
    #pre: Width and height must be resonable to relative to screen size and other Sprites.
    #post:item is initiated. The image is also set to 'item.png'and the item powerup is randomised as well.
    #Purpose:TO initiate an item class with the picture, "item.png"
    global numItems
    numItems = 4

    def __init__(self, width, height):
        Block.__init__(self, white, width, height)
        self.itemNumber = random.randrange(1, numItems)
        self.image = image.load('resources/item.png')
    #pre:
    #post: updates the position of the item to a random position on the screen
    #Purpose: To have the item appear somewhere random on the screen
    def update(self):
        self.rect.x=random.randrange(screen_width - 15)
        self.rect.y=random.randrange(40, screen_height - 55)
    #pre:
    #post:  To get the item number. Each item number from 1-3 represents a different item
    #Purpose:   To find the item that the item class represented
    def getItemNumber(self):
        return self.itemNumber
    #pre:
    #post:      To set the item number to a random number between 1 and 3
    #Purpose:   To change the poweru contained within the item class
    def setItemNumber(self):
        self.itemNumber = random.randrange(1, numItems )

class highscore():
    maxBalls = 30
    #pre:   highscores.txt SHOULD exist with a series of numbers. Each number is in its own line
    #post:  highscore will be initialised with the saved highscores from highscores.txt
    #       if highscores.txt does not exist, then a blank highscores will be created
    #Purpose: To load, or initialise a highscores for the game
    def __init__(self):
        self.mainDecision=True
        self.mainDecision2=True
        try:
            f = open("resources/ballDodgerHighScores.txt", "r")

            self.highscores = []

            self.highscores = f.readlines()     #read the lines in the textfile and put them in a list

            for x in range(len(self.highscores)):   #take that list and change all each element int he list to an integer
                self.highscores[x] = int(self.highscores[x].strip("\n"))

            f.close()
            print "file was read"
        except:
            #if the textfile is not found, or can not be read properly, a list containing only 0s will be created.
            #in other words, all scores are reset to 0
            self.highscores = []
            for x in range(self.maxBalls):
                self.highscores.append(0)
            print "file didn't exist"

    #pre: self.highscores must be a list
    #post:self.highscores will be saved in highscores.txt. Each highscore will be be in the text file, a  separate line for each score.
    #Purpose:To save the highscores
    def saveEverything(self):
        f=open("resources/ballDodgerHighScores.txt","w")
        for x in self.highscores:
            f.write(str(x) + "\n")
    #pre:score scoreIndex must be between 1-29
    #post:  The highscore at index "scoreIndex" will be returned
    #Purpose:   To get a highscore for the mode,"scoreIndex"
    def getScore(self, scoreIndex):
        return self.highscores[scoreIndex]
    #pre:score scoreIndex must be between 1-29. newScore must be a positive integer. However, this method will function if a integer is inputted
    #post:  This highscore at index, "scoreIndex" will be set to newScore
    #Purpose: TO change one of the highscores to "newScore"
    def setScore(self, scoreIndex, newScore):
        self.highscores[scoreIndex] = newScore



