#Broken blackjack game
# Random Simulations
#================================
from math import *
from random import *
from ti_system import *
from ti_draw import *
#================================
key = ""
money = 0
def savemoney():
  store_value("bj_money",money)
def loadmoney():
  global money
  money = recall_value("bj_money")
def addmoney(a):
  global money
  money = money + a
  savemoney()
loadmoney()

game = False
stand = False
win = False
ds = 0
ps = 0
bet = 100
lh = 0
def drawui():
  set_color(0,255,0)
  draw_text(10,25,"$"+ str(money))
  if lh > get_time_ms():
    if win:
      draw_text(50,50,"u won")
      return
    draw_text(50,50,"u lost")
  if not game:
    draw_text(150,100,"press 9 to start")
    return
  draw_text(25,50,"dealer: "+ str(ds))
  draw_text(25,75,"you: " + str(ps))
def draw():
  set_color(0,0,0)
  fill_rect(0,0,400,300)
  drawui()
def hit():
  return randint(1,10)
def input(k):
  global stand
  global game
  global ps
  if not game:
    if k != "":
      stand = False
      game = True
    return
  if stand:
    return
  if k == "9":
    ps = ps + hit()
  if k == "6":
    stand = True
lh = 0
def ai():
  global lh
  global game
  global stand
  global win
  global ds
  global ps
  if get_time_ms() < lh:
    return
  lh = get_time_ms() + 2
  if ds < 18:
    ds = ds + hit()
  if ds >= 21:
    win = True
    game = False
    stand = False
    ds = 0
    ps = 0
    addmoney(bet)
    return
  if ds > ps:
    win = False
    game = False
    stand = False
    ds = 0
    ps = 0
    addmoney(-1*bet)
def think():
  key = get_key()
  input(key)
  if game and stand:
    ai()
  use_buffer()
  draw()
  paint_buffer()
while True:
  think()
savemoney()
