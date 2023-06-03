# Self explanatory, uses entity system cause that's cool
# Geometry Graphics
#================================
from ti_draw import *
from ti_system import *
from math import *
from random import *
#================================
ents = []
s1 = 0
s2 = 0

class entity():
  def init(s):
    s.x = 150
    s.y = 100
  def __init__(s):
    ents.append(s)
    s.x = 0
    s.y =0
    s.t = 0
    s.w = 0
    s.h = 0
    s.init()
  def think(s):
    s.a = 1
  def draw(s):
    fill_rect(s.x,s.y,s.w,s.h)
  def setpos(s,x,y):
    s.x = x
    s.y = y
  def collide(s,e):
    return s.x < e.x+e.w and s.x>e.x and s.y>e.y and s.y<e.y+e.h
class cursor(entity):
  def init(s):
    s.x = 0
    s.y = 0
    s.w = 5
    s.h = 5
  def think(s):
    m = get_mouse()
    s.x = m[0]
    s.y = m[1]
class ball(entity):
  def init(s):
    s.x = 150
    s.y = 100
    s.w = 8
    s.h = 8
    s.dirx = 1
    s.diry = 0
  def draw(s):
    fill_circle(s.x+s.w/2,s.y-s.h/2,s.w)
    #fill_rect(s.x,s.y-s.h,s.w,s.h)
  def think(s):
    global s1
    global s2
    s.x = s.x + s.dirx
    s.y = s.y + s.diry
    if s.x < s.w:
      s.dirx = 1
      s.x  = 150
      s.y = 100
      s.diry = 0
      s2 = s2+1
    if s.x > 320-s.w:
      s.dirx = -1
      s.x = 150
      s.y = 100
      s.diry = 0
      s1 = s1 + 1
    if s.y < s.h:
      s.diry = 1
    if s.y > 210 - s.h:
      s.diry = -1
    for e in ents:
      if e == s:
        continue
      if s.collide(e):
        s.dirx = s.dirx*-1
        yd = 1
        if randint(0,1) ==1:
          yd = -1
        s.diry = (s.diry or 1 )*yd
class paddle(entity):
  def init(s):
    s.w = 10
    s.h = 30
  def __init__(s,x,y,dk,uk):
    s.x = x
    s.y = y 
    s.dk = dk
    s.uk = uk
    ents.append(s)
    s.init()
  def draw(s):
    fill_rect(s.x,s.y,s.w,s.h)
def draw():
  use_buffer()
  set_color(0,0,0)
  fill_rect(0,0,400,250)
  set_color(255,255,255)
  set_pen("thin","dashed")
  draw_line(160,0,160,250)
  set_pen("thin","solid")
  for e in ents:
    e.draw()
  draw_text(150,20,str(s1))
  draw_text(165,20,str(s2))
  paint_buffer()
b = ball()
c = cursor()
p1 = paddle(10,90,"7","4")
p2 = paddle(300,90,"9","6")
while True:
  draw()
  for e in ents:
    e.think()
  k = get_key()
  if k == p1.uk:
    p1.y = p1.y + 13
  if k == p1.dk:
    p1.y = p1.y - 13
  if k == p2.uk:
    p2.y = p2.y + 13
  if k == p2.dk:
    p2.y = p2.y - 13
