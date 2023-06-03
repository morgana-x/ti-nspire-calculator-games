# Very dodgy particle "simulator"
# Geometry Graphics
#================================
from random import *
from ti_system import *
from time import *
from math import *
from ti_draw import *
#================================
ents = []
grlvl = 210
def collide(a,b):
  ap = a.y#abs(a.y+a.vy)
  bp = abs(b.y-b.vy)
  if a.x + a.vx >= b.x and a.x<= (b.x+b.vx) and ap >= bp and ap <=bp:
    return True
  return False
def ground(a):
  if a.y >= grlvl:
    return True
  for e in ents:
    if e == a:
      continue
    if collide(a,e):
      a.y = a.y - a.vy
      e.vy = e.vy + (a.vy/5)
      a.vy = e.vy - (a.vy/5)
      return True
  a.vy = a.vy +1
  a.y = a.y - a.vy
  return False
types =[ [[255,100,100],1.5],[[40,255,100],1.5]]  #{"c" = 2}#[255,100,150]}
class p(): #particle
  x = 0
  y = 0
  vy = 0
  vx = 0
  g = 0
  type = 0
  def __init__(s):
    ents.append(s)
  def remove(s):
    ents.remove(s)
  def collide(s):
    for e in ents:
      if e == s:
        continue
      if e.x -s.x > s.vx:
        continue
      if e.x - s.x > e.vx:
        continue
      if e.y - s.y > s.vy:
        continue
      if collide(s,e):
        return e
    return False
  def think(s):
    s.vy = (s.vy -1 and s.vy >0) #or (s.vy + 1.5 and s.vy <0)
    #s.vx = s.vx -1.5
    #s.vy = (0 and (s.vy <=0)) or s.vy
    if not ground(s):
      s.vy = s.vy +2
    s.x = s.x + s.vx
    s.y = s.y + s.vy
    e = s.collide()
    if e:
       s.x = s.x - s.vx
       s.y = s.y - s.vy
       s.vy = e.vy
       e.vy = e.vy +( s.vy/2)
       #s.vx = (randint(-1,1)*0.5)
    if s.y >grlvl+1:
      s.vy = 0
      s.y = grlvl
  def draw(s,scale): 
    c = types[s.type][0]
    set_color(c[0],c[1],c[2])
    xx = (s.x+scale)
    yy = (s.y+scale)
    fill_rect(xx,yy,1*scale,1*scale)
    #draw_line(s.x,s.y,s.x,s.y)
    #plot_xy(s.x,s.y,3)
br = 1
mx,my = 0,0
selt = 0
def draw():
  set_color(0,0,0)
  fill_rect(0,0,350,300)
  for e in ents:
    e.draw(1)
  c = types[selt][0]
  set_color(c[0],c[1],c[2])
  draw_circle(mx,my,br)
def think():
  for e in ents:
    e.think()
def mk(x,y,t):
  b = p()
  b.x = x
  b.y = y
  b.t = t or 0
for x in range(10):
  for y in range(2):
    b = p()
    b.x = 200 + x
    b.type = randint(0,len(types)-1)
    b.y = y
k = ""
while True:
  use_buffer()
  draw()
  paint_buffer()
  think()
  #mk(randint(100,200),randint(1,20),0)
  k = get_key()
  mx,my = get_mouse()
  if k == "6":
    selt = selt + 1
    if selt >= len(types):
      selt = 0
  if k == "7":
    br = br + 5
  if k == "4":
    br = br - 5
    if br < 1:
      br = 1
  if k == "9":
    #mx,my = get_mouse()
    if br == 1:
      mk(mx,my,selt)
    else:
      for x in range(br*2):
        pa = p()
        pa.x = mx + x - br
        pa.y = my + y
        pa.type = selt
