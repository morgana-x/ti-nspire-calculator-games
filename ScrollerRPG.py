#Test of creating top down rpg maps, never finished levels / fighting, just a cool looking house and neighborhood you can explore
from time import *
from ti_system import *
from ti_draw import *
from ti_image import *

stopgame = 0

plyspeed = 5

plyx = 0
plyy = 0

fixplyx = 150
fixplyy = 100
fixplyw = 10
fixplyh = 10

plyhp = 100
plymaxhp = 100
plylvl = 1

tickc = 0
framec = 0
fpsc = 0
fps = 0

fclrdly = 0

level = []
currentscene = 0

BattleActive = False

def scenescripts():
  global currentscene
  global plyx
  global plyy
  if currentscene == 0:
    if (plyx == 45) and (plyy == -30):
      plyx, plyy = 0,40
      currentscene = 1
  elif currentscene == 1:
    if (plyx == -110 and plyy == 30):
      currentscene = 2
      plyx, plyy = 50,35
    elif (plyx == 0) and (plyy == 50):
      currentscene = 0
      plyx, plyy = 40, -30
  elif currentscene == 2:
    if (plyx ==50) and plyy == 40:
      currentscene = 1
      plyx, plyy = -100, 30
    if (plyx > 0) and plyy == -95:
      currentscene = 3
      plyy = 90
  elif currentscene == 3:
    if plyy == 95:
      currentscene = 2
      plyy = -90

def generatelevel():
  scene0 = []
  sc0lvl = []
  #level (walls, non interactive stuff in general):
  #drawtypes: 1= fill, 2=sprite, 3=outline
  #format: drawtype collide xpos ypos width height r g b
  sc0lvl.append([1, 0, 50, 0, 150, 150, 200, 255, 200])
  sc0lvl.append([1, 1, 50, 0, 150, 50, 100, 90, 54])
  sc0lvl.append([1, 1, 100, 50, 30, 20, 200, 100, 100])
  sc0lvl.append([1, 0, 130, 50, 10, 20, 200, 200, 200])
  sc0lvl.append([1, 1, 100, 20, 50, 20, 100, 110, 255])
  sc0lvl.append([1, 1, 50, 150, 150, 5, 100, 90, 54])
  sc0lvl.append([1, 1, 50, 0, 5, 150, 100, 90, 54])
  sc0lvl.append([1, 1, 200, 0, 5, 130, 100, 90, 54])
  sc0lvl.append([1, 1, 200, 140, 5, 15, 100, 90, 54])
  scene0.insert(0,sc0lvl)
  sc0int = []
  #interactables, interactive stuff
  #interaction types: 1: Press button to int, when in range
  # 2: activate when in range
  #template:
  #int type, solid, xpos, ypos, w,h,r,g,b, range func
  scene0.insert(1, sc0int)
  sc0enemies = []
  #enemies, will chase player and activate battle
  # xpos, ypos, w, h, name, lvl, possible enemies []
  scene0.insert(2, sc0enemies)
  level.append(scene0)
  scene1 = [
  #level
  [
  #drawtypes: 1= fill, 2=sprite, 3=outline
  #format: drawtype collide xpos ypos width height r g b
  [1, 0, 50, 0, 300, 150, 220, 200, 50], #floor
  [1, 1, 50, 0, 300, 50, 220, 100, 50], #backwall
  [1, 0, 150, 30, 10, 20, 0, 0, 0],
  #table
  [1, 1, 230, 100, 30, 20, 100, 90, 70],[1, 0, 230, 120, 2, 10, 100, 90, 70],[1, 0, 258, 120, 2, 10, 100, 90, 70],

  [1, 1, 50, 150, 300, 10, 220, 100, 50], #frontwall
  [1, 1, 350, 0, 10, 160, 220, 100, 50], #rightwall
  [1, 1, 40, 0, 10, 70, 220, 100, 50], #leftwall1
  [1, 1, 40, 80, 10, 80, 220, 100, 50] #leftwall2
  
  ],
  
  #Interactiables
  [],
  
  #enemies
  #enemies, will chase player and activate battle
  #xpos, ypos, w, h, name, lvl, possible enemies []
  []
  ]
  level.insert(1,scene1)
  scene2 = [
  #level

  [
  #drawtypes: 1= fill, 2=sprite, 3=outline, 4 = none
  #format: drawtype collide xpos ypos width height r g b
  #collisionboundries
  [4,1,0,0,400,1,0,0,0],
  [4,1,140,0,10,400,100,50,50],
  [4,1,400,0,10,400,100,50,50],
  [4,1,0,-50,600,50,100,50,50],
  #grass,sidewalk,road
  [1, 0, 150, 0, 400, 100, 220, 240, 220], [1, 0, 150, 95, 400, 100, 200, 200, 200],  [1, 0, 150, 110, 400, 70, 0, 0, 0],
  [1, 0, 200, 150, 100, 50, 0, 0, 0],
  #yourhouse
  [1,1,160,10,70,50, 255,240,240],
  [1,1,150,0,90,30, 255,100,100],
  [1,0,160,60,70,20, 230,220,0],
  [1,0,200,40,10,20,0,0,0],
  #house2
  [1,1,270,10,70,50, 240,255,240],
  [1,1,260,0,90,30, 100,100,255],
  [1,0,270,60,70,20, 230,220,0],
  [1,0,310,40,10,20,0,0,0],
  
  #house3
  [1,1,380,10,70,50, 240,255,240],
  [1,1,370,0,90,30, 100,255,100],
  [1,0,380,60,70,20, 230,220,0],
  [1,0,420,40,10,20,0,0,0],
  ],
  
  
  
  #Interactiables
  [],
  
  #enemies
  #enemies, will chase player and activate battle
  #xpos, ypos, w, h, name, lvl, possible enemies []
  [
   [150, 150, 10, 10, "Thief", 1, []]
  ]
  ]
  level.insert(2,scene2)
  scene3 = [
  #level

  [
  #drawtypes: 1= fill, 2=sprite, 3=outline, 4 = none
  #format: drawtype collide xpos ypos width height r g b
  #collisionboundries
  [4,1,0,0,400,1,0,0,0],
  [4,1,140,0,10,400,100,50,50],
  [4,1,400,0,10,400,100,50,50],
  [4,1,0,400,400,50,100,50,50],
  #grass,sidewalk,road
  [1, 0, 150, 0, 400, 100, 220, 240, 220], [1, 0, 150, 100, 400, 100, 200, 200, 200],  [1, 0, 150, 120, 400, 70, 0, 0, 0],
  [1, 0, 200, 0, 100, 400, 0, 0, 0],
  #yourhouse
  [1,1,130,35,70,50, 255,240,240],
  [1,1,120,25,90,30, 255,100,100],
  [1,0,130,85,70,20, 230,220,0],
  [1,0,170,65,10,20,0,0,0],
  #house2
  [1,1,310,35,70,50, 240,255,240],
  [1,1,300,25,90,30, 100,100,255],
  [1,0,310,85,70,20, 230,220,0],
  [1,0,350,65,10,20,0,0,0],
  
  #house3
  [1,1,420,35,70,50, 240,255,240],
  [1,1,410,25,90,30, 100,255,100],
  [1,0,420,85,70,20, 230,220,0],
  [1,0,480,65,10,20,0,0,0],
  ],
  
  
  
  #Interactiables
  [],
  
  #enemies
  #enemies, will chase player and activate battle
  #xpos, ypos, w, h, name, lvl, possible enemies []
  [
   [150, 150, 10, 10, "Thief", 1, []]
  ]
  ]
  level.insert(3,scene3)
generatelevel()
def tick():
  global tickc
  global fpsc
  global fps
  global framec
  global fclrdly
  tickc = tickc + 1
  if tickc > 60:
    tickc = 0
  if clock() > fclrdly :
    fclrdly = clock() + 6
    clear()
  if clock() >= fpsc:
    fpsc = clock() + 1
    fps = framec
    framec = 0
  scenescripts()
  frame()
def enemythink():
  global BattleActive
  if len(level[currentscene][2]) <1 or BattleActive:
    return
  for enemy in level[currentscene][2]:
    dirx = 0
    diry = 0
    if enemy[0] - plyx - fixplyx > 70 or enemy[1] + plyy - fixplyy > 70:
      continue
    calcx = (enemy[0] - plyx)
    calcy = (enemy[1] + plyy)
    if fixplyx > calcx:
      dirx = -1
    elif fixplyx < calcx:
      dirx = 1
    if fixplyy > calcy:
      diry = 1
    elif fixplyy < calcy:
      diry = -1
    enemy[0] = enemy[0] - dirx
    enemy[1] = enemy[1] + diry
    if isCollide(enemy[0],enemy[1],enemy[2],enemy[3]):
      enemy[1] = enemy[1] - diry
      enemy[0] = enemy[0] + dirx
    if isPlayerTouching(enemy[0],enemy[1],enemy[2],enemy[3]):
      BattleActive = True
def frame():
  global framec
  enemythink()
  draw()
  processinput()

  #fps counter goes at the end
  framec = framec + 1

def draw():
  use_buffer()
  paint_buffer()
  #drawbg
  set_color(0,0,0)
  fill_rect(0,0,400,400)
  #drawlevel
  for item in level[currentscene][0]:
    set_color(item[6],item[7],item[8])
    if item[0] == 1:#fill
      fill_rect(item[2] - plyx, item[3] + plyy, item[4], item[5])
    if item[0] == 3: #outline
      draw_rect(item[2] - plyx, item[3] + plyy, item[4], item[5])
  #drawenemies
  for enemy in level[currentscene][2]:
    set_color(255,0,0)
    fill_rect(enemy[0] - plyx, enemy[1] + plyy, 10, 10)
  #drawplayer
  set_color(200,200,255)
  fill_rect(fixplyx,fixplyy,fixplyw,fixplyh)
  #drawforeground
  
  #hud etc
  
  #health and level
  set_color(100,100,100)
  fill_rect(20, 160, 60, 40)
  set_color(100,255,100)
  draw_text(25, 180, "LVL: " + str(plylvl))
  draw_text(25, 200, "HP: " + str(plyhp))
  set_color(255,240,100)
  draw_text(150, 20, "x: " + str(plyx) + " y: " + str(plyy))
  #draw at end so its on top
  set_color(255,200,100)
  draw_text(20,20, fps)

def processinput():
  global stopgame
  global plyy
  global plyx
  key = get_key()
  if (key == "6") or (key == "d"):
    plyx = plyx + plyspeed
    if isPlayerCollide():
      plyx = plyx - plyspeed
  elif (key == "4") or (key == "a"):
    plyx = plyx - plyspeed
    if isPlayerCollide():
      plyx = plyx + plyspeed
  elif (key == "w") or (key == "8"):
    plyy = plyy + plyspeed
    if isPlayerCollide():
      plyy = plyy - plyspeed
  elif (key == "s") or (key == "2"):
    plyy = plyy - plyspeed
    if isPlayerCollide():
      plyy = plyy + plyspeed
  elif (key == "z"):
    stopgame = 1
def isPlayerCollide():
  for item in level[currentscene][0]:
    if not item[1] == 1:
      continue
    if (fixplyx < item[2] - plyx + item[4] and
    fixplyx + fixplyw > item[2] - plyx and
    fixplyy - plyy < item[3] + item[5] and 
    fixplyh + fixplyy - plyy > item[3]):
      return True
  return False

def isPlayerTouching(x,y,w,h):
  if (fixplyx < x - plyx + w and
  fixplyx + fixplyw > x - plyx and
  fixplyy - plyy < y + h and 
  fixplyh + fixplyy - plyy > y):
    return True
  return False
def isCollide(x,y,w,h):
  for item in level[currentscene][0]:
    if not item[1] == 1:
      continue
    if (x - plyx < item[2] - plyx + item[4] and
    x - plyx + w  > item[2] - plyx and
    y < item[3] + item[5] and 
    h + y > item[3]):
      return True
  return False
def isTouching(x,y,w,h, x2,y2,w2,h2):
  if (x2 < x - plyx + w and
  x2 + w2 > x - plyx and
  y2 - plyy < y + h and 
  h2 + y2 - plyy > y):
    return True
  return False

while get_key() != "esc":
  if stopgame == 1:
    break
  else:
    tick()
