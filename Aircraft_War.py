#import models
import time  #control the frequency
import pygame
from pygame.locals import * #observe incidents, like keyboard motion
import sys #use to stop the game
import random #control the enemy's bullets 

#player aircraft:
#properties： window, position, image, bullets list, movement status
#methods: display, movement, fire
class Player():
  #only the screen value need to pass from parameter, others are default
  def __init__(self, screen):
    #represent the player screen
    self.screen=screen
    self.x=600
    self.y=700
    #player image, read via pygame
    self.img=pygame.image.load("player.png")
    #bullet list default null, player has not fire yet. when fire, need to add bullets into the list
    self.bulletlist=[]
    #move left, 0 is going to stop, 1 is going to move
    self.moveleftstate=0
    #move right, 0 is going to stop, 1 is going to move
    self.moverightstate=0
  def display(self):
    #show in the screen, and all properties show as default
    self.screen.blit(self.img,(self.x, self.y))
    self.img=pygame.transform.scale(self.img, (100, 100))
  def move(self):
    pass
  def fire(self):
    pass

#player bullets category:
#properties：window, position, image
#methods: display, movement
class Playerbullet():
  #need to pass player position
  def __init__(self, screen, x, y):
    self.screen=screen
    #x axis, bullet initial position, need to follow the aircraft
    self.x=x+40
    #y axis, bullet initial position, need to follow the aircraft
    self.y=y-20
    #player bullet image
    self.img=pygame.image.load("Bullet_blue.png")
  def display(self):
    pass
    #self.img=pygame.transform.scale(self.img, (30, 30))
  def move(self):
    pass

#enemy aircraft:
#properties： window, position, image, bullets list, movement status
#methods: display, movement, fire
class Enemy():
  #only the screen value need to pass from parameter, others are default
  def __init__(self, screen):
    self.screen=screen
    #x, y axis, bullet initial position
    self.x=0
    self.y=0
    self.img=pygame.image.load("playerEnemy.png")
    #Enemy bullet list
    self.bulletlist=[]
    #0 is going to left, 1 is going to right
    self.movestate=1 
  def display(self):
    #show in the screen, and all properties show as default
    self.screen.blit(self.img,(self.x, self.y))
    self.img=pygame.transform.scale(self.img, (60, 60))
  def move(self):
    if self.movestate==1:
      self.x+=10
    elif self.movestate==0:
      self.x-=10
    #when reaching the boundary， reverse backward
    if self.x<20:
      self.movestate=1
    if self.x>1200:
      self.movestate=0
  def fire(self):
    pass

#enemy bullets category:
#properties：window, position, image
#methods: display, movement
class Enempbullet():
  def __init__(self, screen, x, y):
    self.screen=screen
    #x y axis, bullet initial position, need to follow the enemy aircraft 
    self.x=x+22
    self.y=y+32
    self.img=pygame.image.load("Bullet_gray.png")
  def display(self):
    pass
    #self.img=pygame.transform.scale(self.img, (30, 30))
  def move(self):
    pass

#keyboard control: capture user actions
def key_control(player):
  #loop all the event once
  for event in pygame.event.get():
    #capture is player quit the screen
    if event.type==QUIT:
      print("Quit the game")
      #force to quit the game
      sys.exit(0)

#main method
class main():
  #create game screen, screen size depend on background image
  screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  background=pygame.image.load("background.jpg")
  #create an object player and pass into screen
  player=Player(screen)
  #create an object enemy and pass into screen
  enemy=Enemy(screen)

  #show all all the objects
  while 1==1:
    #show background
    screen.blit(background,(0,0))
    #show player
    player.display()
    #show enemy
    enemy.display()
    #enemy movement
    enemy.move()
    key_control(player)
    #keep reflash screen
    pygame.display.update()
    time.sleep(0.05)
    
#--------------------------------------------------
if __name__ == '__main()__':
  main()