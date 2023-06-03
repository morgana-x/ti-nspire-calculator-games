#silly little program
from ti_draw import *
from ti_system import *
from time import *
from random import *
from math import *
from ti_image import *



ljs = 0
def draw():
  clear()
  use_buffer()
  set_color(0,0,0)
  fill_rect(0,0,320,350)
  a =  get_time_ms() - ljs
  if a <255:
    if a <0:
      a = 0
    set_color(a,0,0)
    fill_rect(0,0,320,350)
    set_color(0,0,0)
    #set_pen("thick","solid")
    draw_text(150,100,"hi")
  paint_buffer()
def jmp():
  global ljs
  ljs = get_time_ms()
while True:
  draw()
  if get_key() == "a":
    jmp()
  if randint(0,10000) < 10:
    jmp()
