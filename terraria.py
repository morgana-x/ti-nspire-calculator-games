from ti_system import *
from time import *
from math import *
from ti_draw import *
from random import *


plyx = 0
plyy = 0
plyxspeed = 1
plb = 0
tick = 0
level = []
stopgame = 0
jumpheight = 5

bsize = 4
scrpx = 0
scrpy = 0
blockcolour = [
[100,255,100],#bright green
[100,55,50],#brown
[200,200,200],#grey
[250,200,100],#sand
[0,200,100],# dark green
[250,100,100], #blood
[0,0,0],
[200,50,255], #purple
[255,255,255] #white
]
entities = []
class entity():
  x = 0
  y = 0
  w = 2
  h = 1
  c = 0
  def init(s):
    s.a = 1
  def __init__(s):
    entities.append(s)
    s.init(s)
  def draw(s):
    s.a = 1
  def think(s):
    s.a = 1
biomes = []
class biome():
  grass = 0
  dirt = 1
  stone = 2
  ores = [5,4]
  tree = [1,4]
  mobs = False
  def __init__(s):
    biomes.append(s)
    s.a = 0
biome_grass = biome()
biome_desert = biome()
biome_desert.tree = False
biome_desert.grass = 3
biome_desert.dirt =5
biome_hell = biome()
biome_hell.grass = 5
biome_hell.tree = [2,5]
biome_forest = biome()
biome_forest.grass = 4
biome_mushroom = biome()
biome_mushroom.grass = 7
biome_mushroom.tree =[8,[8,5]]
fps = 0
fpsc = 0
fpsdelay = 0
fixedplayerx = 150
fixedplayery = 150
fixedplayersx = 10
fixedplayersy = 10
plyyspn = 0
plyspnx = 0
plychunk = 0
chunksize = 20
lft = 0
curt = 0
pmenu = False
#chunk = 50 x 255
#block data = [x,y,type]
def save(name):
  store_list(name,level)
  wlist =recall_list("levels")
  wlist.append(name)
  store_value("levels",wlist)
def load(name):
  load =recall_list(name)
  level =[]
  for x in range(load.len()):
    level.append([x,x,load[x]])
def ctree(px,py,c,l,w):
  #l = l or 1 #wood
  #w = w or 4 #leaf default 0
  #if randint(1,4)==4:
  #  w = 5
  c.append([px,py,l])
  c.append([px,py+1,l])
  c.append([px,py+2,l])
  leaf = [
  [0,3],
  [-1,3],
  [1,3],
  [0,4]
  ]
  for o in leaf:
    h = 0
    #print(type(w))
    if type(w) == list:
      h = w[randint(0,len(w)-1)]
    else:
      h = w
    c.append([px+o[0],py+o[1],h])
def chouse(px,py,c):
  sx = 6
  sy = 5
  bt = 3
  btt= 2
  for x in range(sx+1):
    c.append([px +x,py,bt])
    c.append([px+x,py+sy,btt])
  for y in range(sy):
    c.append([px + sx,py+y,bt])
  for y in range(sy - 2):
    c.append([px,py+2+y,bt])
def createLevel():
  global level
  global plyx
  global plyy
  global plychunk
  global plyspnx
  global plyyspn
  
  levelwidth = 200
  lh = 0
  x = 0
  for c in range(0,levelwidth / chunksize):
   chunk=[]
   biomec = randint(0,len(biomes)-1)
   biome = biomes[biomec]
   for b in range(x,x + chunksize):
     x = b
     height = floor(uniform(20,sin(x) + lh))
     lh = height
     if biome.tree and (randint(1,6) ==3):
       ctree(x,lh,chunk,biome.tree[0],biome.tree[1])
     if biome.mobs and (randint(1,6)==3):
       m = randint(0,len(biome.mobs))
       mob = biome.mobs[m]()
       mob.x = x
       mob.y = lh+1
       mob.c = chunk
     #elif randint(1,50) ==5:
       #chouse(x,lh,chunk)
     for y in range(height):
       # addblock 
       t = biome.grass
       if -y+height > 3:
         t = biome.dirt
       if -y+height> 10:
         t = biome.stone
         if randint(1,55)==50:
           t = biome.ores[0]
         #t = randint(floor(sin(y-(10))),ceil(cos(y-(10))))
       #if t >3:
         #t = 2
       chunk.append([b,y,t])
     if x == levelwidth /2:
       plyx = x
       plyy = 1 + height
       plyyspn = height + 1
       plyspnx = x
       plychunk = c
   level.insert(c,chunk)
createLevel()
clockdelay = 0
def doTick():
  global clockdelay
  if clock() > clockdelay:
    clockdelay = clock() + 6
    #clear()
selectblock = 0
def drawhot():
  sx = len(blockcolour)*10
  xp = 155 - sx /2
  yp = 200
  
  for x in range(len(blockcolour)):
    c = blockcolour[x]
    set_color(c[0],c[1],c[2])
    fill_rect(xp+(x*10),yp,10,10)
  set_color(255,255,255)
  draw_rect(xp,yp,sx,10)
  set_pen("medium","solid")
  draw_rect(xp + (plb*10),yp,10,10)
  set_pen("thin","solid")
def drawpmenu():
  if not pmenu:
    return
  set_color(100,100,100)
  fill_rect(0,0,100,100)
def processInput():
  key = get_key()
  global plyx
  global plyy
  global plb
  global stopgame
  if key == "right" or key =="6" or key == "d":
    plyx = plyx + plyxspeed
    if isPlayerCollide() == 1:
      plyx = plyx - plyxspeed
  elif key == "left" or key == "4" or key == "a":
    plyx = plyx - plyxspeed
    if isPlayerCollide() == 1:
      plyx = plyx + plyxspeed
  elif (key == "up" or key == "8" or key == "w" ) and isPlayerGrounded() == 1:
      for jump in range(jumpheight):
        plyy = plyy +1
        if isPlayerCollide() == 1:
          plyy = plyy - 1
          break
  elif (key=="0"):
    global bsize
    bsize = bsize -1
    if (bsize < 1):
      bsize = 4
  elif(key=="9"):
    m=get_mouse()
    mx = (m[0] / (10*bsize)) + (scrpx/(10*bsize))+1+plyx - (30/bsize)
    mx = floor(mx) 
    my = ((m[1] / (10*bsize)) - (scrpy/(10*bsize)) -plyy -1)*-1
    my = floor(my)
    hitb = 0
    for ch in range(plychunk-2,plychunk+2):
      if ch <0 or ch >= len(level):
         continue
      c = level[ch]
      for b in c:
        if b[0] == mx and b[1]==my:
          c.remove(b)
          hitb == 1
          return
    if hitb==0:
      level[floor(mx/chunksize)].append([mx,my,plb])
  if (key == "1"):
    plb = plb -1
    if (plb <0):
      plb = len(blockcolour)-1
  if (key == "3"):
    plb = plb + 1
    if plb > len(blockcolour)-1:
      plb = 0
  elif (key == "z"):
    stopgame = True


def draw():
  paint_buffer()
  use_buffer()
  #dt = sin(clock())
  #draw bg
  set_color(150,150,255)
  fill_rect(0,0,500, 500)
  
  #draw level
  #add chunkselect
  for c in range((plychunk -2), (plychunk+1)):
    if c<0 or c >=len(level):
      continue
    chunk = level[c]
    if c > plychunk:
      continue
    skip = False
    bc = 0
    sx = 10*bsize
    for block in chunk: 
      if plyy - block[1]> (7/bsize) or plyy - block[1]<-(17/bsize) or plyx - block[0] >(16/bsize) or plyx - block[0]<-(16/bsize):
        continue
      pos1 = scrpx +block[0] *(10*bsize) - plyx*(10*bsize)
      pos2 = scrpx+block[1] *-(10*bsize) + plyy*(10*bsize)
      set_color(blockcolour[block[2]][0], blockcolour[block[2]][1], blockcolour[block[2]][2])
      fill_rect(pos1, pos2, sx, 10*bsize )
  mx,my=floor(get_mouse()[0]),floor(get_mouse()[1])
  #draw_rect(ceil(mx),my,10,10)
  for e in entities:
    e.draw()
  #draw player 
  set_color(0,20,200)
  fill_rect(scrpx,scrpy,10*bsize,10*bsize)
  
  drawpmenu()
  draw_text(5,15,str(fps))
#  draw_text(20,40,"chunk: " + str(plychunk))
  drawhot()


def isPlayerCollide():
  global plychunk
  plyx2 = floor(plyx)
  plyy2 = floor(plyy)
  for c in range(plychunk - 1, plychunk + 1):
    if c<0 or c >= len(level):
      continue
    for block in level[c]:
      if plyx2 == block[0] and plyy2 == block[1]:
        return 1
  return 0


def isPlayerGrounded():
  global plychunk
  for c in range(plychunk - 1, plychunk+1):
    if c<0 or c >=len(level):
      continue
    for block in level[c]:
      if plyy - 1 - block[1] >1:
        continue
      if plyx == block[0] and plyy - 1 == block[1]:
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
lbsize = 0
while get_key() != "esc":
  if stopgame == True:
    break
  curt = lft - clock()
  doTick()
  plychunk = floor(plyx/chunksize)+1
  draw()
  if isPlayerGrounded() == 0:
    plyy = (plyy - 1)
  if plyy < -50:
    plyx, plyy = plyspnx,plyyspn
  processInput()
  if lbsize != bsize:
    lbsize = bsize
    scrpx = fixedplayerx-(ceil((10*bsize)/2))
    scrpy = fixedplayery-(ceil((10*bsize)/2))
    for e in entities:
      e.think()
  fpsc = fpsc +1
  lft = clock()
  if clock() >= fpsdelay:
     fpsdelay = clock() + 1
     fps = fpsc
     fpsc = 0
