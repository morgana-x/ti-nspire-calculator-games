# Space invaders but the collision logic is terrible
# Geometry Graphics
#================================
from ti_draw import *
from ti_system import *
from math import *
from random import *

#================================
def iscollide(x1,y1,w1,h1,x2,y2,w2,h2):
  if x1 < x2+w2 and x1>x2 and y2 <y1+h1 and y2>y1:
     return True
  return False

class World():
  def __init__(s):
    s.ents = []
world = World()
class entity():
  def init(s,a,b,c):
    s.init = 1
  def __init__(s,a,b,c):
    world.ents.append(s)
    s.x = 0
    s.y = 0
    s.hbw = 0
    s.hbh = 0
    s.w = 0
    s.h = 0
    s.init(a,b,c)
  def think(s):
    s.a = 1
  def remove(s):
    for e in world.ents:
      if e == s:
        world.ents.remove(s)
        break
  def collided(s,o):
    return iscollide(s.x,s.y,s.hbw,s.hbh,o.x,o.y,o.hbw,o.hbh)
class laser(entity):
  def init(s,x,y,d):
    s.x = x
    s.y = y + (d*2)
    s.d = d
    s.hbw = 4
    s.hbh = 4
  def think(s):
    s.y = s.y + (s.d*2)
    if s.y > 200:
      s.remove()
    if s.y <0:
      s.remove()
    for e in world.ents:
      if s.collided(e):
        e.remove()
        s.remove()
  def draw(s):
    set_color(255,0,0)
    fill_rect(s.x,s.y,s.hbw,s.hbh)
class block(entity):
  def init(s,x,y,a):
    s.x = x
    s.y = y
    s.w = 6
    s.h = 6
    s.hbw = s.w
    s.hbh = s.h
  def draw(s):
    set_color(0,0,255)
    fill_rect(s.x,s.y,s.w,s.h)
class invader(entity):
  def init(self,x,y,row):
    self.x = x
    self.y = y
    self.dir = 1
    self.row = row or 0
    self.hbw = 5
    self.hbh = 5
  def shoot(s):
    l = laser(s.x,s.y+4,1)
  def think(s):
    if s.row == 4 and randint(1,50) == 5:
      s.shoot()
  def draw(self):
    set_color(0,200,0)
    fill_rect(self.x,self.y,self.hbw,self.hbh)
class invs(entity):
  def init(self,a,b,c):
     self.rw = 8
     self.rh = 5
     self.ofs = 10
     self.ofsy = 20
     self.hbw = 0
     self.hbh = 0
     self.x = 0
     self.y = 0
     self.iv = []
     for x in range(self.rw):
       for y in range(self.rh):
         self.iv.append(invader(self.ofs+(x*10),self.ofsy+(y*10),y))
  def move(s,x,y):
    l = s.iv
    s.x = s.x + (x or 0)
    s.y = s.y + (y or 0)
    for i in l:
      i.x = i.x + (x or 0)
      i.y = i.y + (y or 0)
  def think(self):
    if self.x <=0:
      self.dir = 1
      self.move(0,4)
    elif self.x >= 210:
      self.dir = -1
      self.move(0,4)
    self.move(self.dir*2,0)
  def draw(s):
    s.a=1

class player(entity):
  def init(s,a,b,c):
    s.x = 100
    s.y = 200
    s.hbw = 6
    s.hbh = 10
  def draw(s):
    set_color(0,0,255)
    fill_rect(s.x,s.y,s.hbw,s.hbh)
  def shoot(s):
    l = laser(s.x,s.y-(s.hbh/2),-1)
  def think(s):
    k = get_key()
    if k == "6":
      s.x = s.x +8
    if k == "4":
      s.x = s.x - 8
    if k == "9":
      s.shoot()
inv = invs(1,2,3)
pl = player(1,2,3)
def draw():
  clear()
  use_buffer()
  set_color(0,0,0)
  fill_rect(0,0,350,250)
  for e in world.ents:
    e.draw()
  paint_buffer()
for a in range(4):
  for x in range(4):
    for y in range(3):
      b = block(1,1,1)
      b.x = (x + (b.hbw*x)) + a *98
      b.y = 170 + (y + (b.hbh*y))
while True:
  draw()
  for e in world.ents:
    e.think()
