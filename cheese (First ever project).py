#First ever program, before I knew how stuff worked (This is was basicPlatformer, my second project, is based off)
from ti_system import *
from ti_draw import *
plyx = 0
plyy = 0
tick = 0
while 1==1:
  key = get_key()
  tick = tick + 1
  if tick > 5:
    tick = 0
    clear()
  if key =="6":
    plyx = plyx + 10
  elif key == "4":
    plyx = plyx - 10 
  elif key == "z":
    break
  #draw bg
  set_color(255,0,0)
  #fill_rect(150-(plyx/2),100,100, 50)
  
  #draw level
  set_color(0,255,0)
  fill_rect(100-plyx,110,50,50)
  set_color(52,52,52)
  fill_rect(150-plyx,110,400,50)
  
  #draw player 
  set_color(0,20,200)
  fill_rect(150,100,10,10)
