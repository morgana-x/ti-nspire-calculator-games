#This is my second ever project (technically just an upgrade of my first)
from ti_system import *
from time import *
from ti_draw import *
plyx = 0
plyy = 0
plyxspeed = 10
tick = 0
level = []
stopgame = 0
jumpheight = 40

fps = 0
fpsc = 0
fpsdelay = 0
fixedplayerx = 150
fixedplayery = 100
fixedplayersx = 10
fixedplayersy = 10


def createLevel():
  global level
  #format = x pos, y pos, sizex, size y, r, g, b
  level.append([140, 50, 10, 100, 200, 200, 200])
  level.append([150, 110, 120, 40, 20, 200, 100])
  level.append([270, 100, 120, 50, 200, 200, 100])
  level.append([285, 80, 20, 10, 100, 200, 100])
  level.append([335, 80, 20, 10, 100, 200, 100])
  level.append([310, 60, 20, 10, 100, 200, 100])
  level.append([390, 100, 100, 50, 200, 200, 200])
  level.append([500, 90, 20, 20, 0, 200, 200])
  level.append([520, 70, 30, 10, 200, 40, 40])
  level.append([550, 50, 30, 10, 200, 40, 40])
  level.append([580, 30, 30, 10, 200, 40, 40])
  level.append([610, 10, 30, 10, 200, 40, 40])
  level.append([640, -10, 50, 10, 200, 40, 40])
  level.append([710, -10, 50, 10, 200, 40, 40])
  level.append([770, 100, 300, 50, 200, 200, 200])
  level.append([1150, 100, 100, 10, 200, 200, 200])
  level.append([1095, 100,10,10,200,255,200])
  level.append([1125, 100, 10, 10, 200, 200, 200])
  level.append([1195, 120,100,200,255,0,0])
createLevel()
clockdelay = 0
def doTick():
  global tick
  global clockdelay
  tick = tick + 1
  if clock() > clockdelay:
    clockdelay = clock() + 6
    clear()
  if tick > 6:
    tick = 0
    



def processInput():
  key = get_key()
  global plyx
  global plyy
  if key == "right" or key =="6" or key == "d":
    plyx = plyx + plyxspeed
    if isPlayerCollide() == 1:
      plyx = plyx - plyxspeed
  if key == "left" or key == "4" or key == "a":
    plyx = plyx - plyxspeed
    if isPlayerCollide() == 1:
      plyx = plyx + plyxspeed
  elif (key == "up" or key == "8" or key == "w" ) and isPlayerGrounded() == 1:
      for x in range(5):
        plyy = plyy + 10
        if isPlayerCollide() == 1 and isPlayerGrounded()==0:
          plyy = plyy - 10
          break
  elif (key == "z"):
    stopgame = true


def draw():
  paint_buffer()
  use_buffer()
  #draw bg
  set_color(150,150,200)
  fill_rect(0,0,500, 500)
  
  #draw level
  for block in level:
    set_color(block[4], block[5], block[6])
    fill_rect(block[0] - plyx, block[1] + plyy, block[2], block[3] )
  
  #draw player 
  set_color(0,20,200)
  fill_rect(fixedplayerx,fixedplayery,10,10)
  draw_text(20,20,str(fps))



def isPlayerCollide():
  for block in level:
    if (fixedplayerx < block[0] - plyx + block[2] and
    fixedplayerx + fixedplayersx > block[0] - plyx and
    fixedplayery - plyy < block[1] + block[3] and 
    fixedplayersy + fixedplayery - plyy > block[1]):
      return 1
  return 0


def isPlayerGrounded():
  for block in level:
    if (fixedplayerx < block[0] - plyx + block[2] and
    fixedplayerx + fixedplayersx > block[0] - plyx and
    fixedplayery - plyy + (0.1) < block[1] + block[3] and 
    fixedplayersy + fixedplayery - plyy + (0.1) > block[1]):
      return 1
  return 0


def isPlayerTouching(x,y,w,h):
  if (fixedplayerx < x - plyx + w and
  fixedplayerx + fixedplayersx > x - plyx and
  fixedplayery - plyy < y + h and 
  fixedplayersy + fixedplayery - plyy > y):
    return 1
  return 0


lasttimeonground = 0
while 1==1:
  if stopgame == 1:
    break
  doTick()
  if isPlayerGrounded() == 0:
    plyy = plyy - 2
  if plyy < -50:
    plyx, plyy = 0,0
  draw()
  processInput()
  fpsc = fpsc +1
  if clock() >= fpsdelay:
     fpsdelay = clock() + 1
     fps = fpsc
     fpsc = 0
