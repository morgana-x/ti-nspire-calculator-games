#An edit of the raycast system program, just has yellow walls, very optimised for higher frame rate as such
from ti_system import *
from ti_draw import *
from ti_image import *
from time import *
from math import *


fpscounter = 0
fps = 0
fpstimer = 0
refreshtimer = 0

scrW = 318
scrWh = scrW / 2
scrH = 240
scrHh = scrH / 2
posx = 4
posz = 7
posy = 0

dscale = 50#5.025 #higher the number the worse r
#qaulity, + perfor
fov = 60
halffov = fov/2
plyangle = 90
raycastincangle = fov / scrW
raycastprecision = 20

map = [
[1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,1,0,0,1,1,1,2,2,1,1,1,1],
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,1,0,0,0,2,2,4,0,0,2,2,2,1],
[1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,3,3,3,0,3,3,3,1,1,1,1],
[3,3,3,3,3,3,3,3,0,0,3,3,3,0,0,0,3],
[3,3,3,3,0,0,0,0,0,0,0,0,0,3,3,3,3],
[3,0,0,0,0,3,3,3,3,3,3,3,0,3,0,0,3],
[3,0,3,3,0,0,0,0,0,0,3,0,0,3,0,0,3],
[3,0,0,3,3,0,3,3,3,0,3,0,3,3,0,0,3],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
textcol = [
[200,200,200],
[250,200,200],
[50,200,50],
[250,220,170],
[240,220,170]
]
texturesize = 6
textures = [
[
[0,1,1,0,1,1],
[0,0,0,0,0,0],
[1,1,0,1,1,0],
[0,0,0,0,0,0],
[0,1,1,0,1,1],
[0,0,0,0,0,0]
],
[
[2,0,2,2,2,0],
[0,2,0,2,2,0],
[0,2,2,0,0,2],
[0,0,0,2,0,0],
[0,0,0,2,2,2],
[0,0,2,2,0,0]
],
[
[3,4,4,4,4,3],
[4,4,3,4,3,4],
[3,4,4,4,4,4],
[4,4,4,4,3,4],
[4,3,4,4,4,3],
[4,4,4,4,3,4]
],
[
[0,0,0,0,0,0],
[0,0,3,3,0,0],
[0,3,3,3,3,0],
[0,3,3,3,3,0],
[0,3,3,3,3,0],
[0,3,3,3,3,0]
]
]
def drawtexture(x,wallh,tposx,texture):
  yinc = (wallh*2)/texturesize
  y = scrHh - wallh
  t = texture
  for i in range(texturesize):
    tc = textcol[t[i][tposx]]
    if t[i][tposx] == -1:
      continue
    set_color(tc[0],tc[1],tc[2])
    fill_rect(x,y,dscale,yinc+1)
    y = y + yinc
def degreeToRadians(degree):
  return degree * pi / 180
def raycast():
  rayAngle = plyangle - halffov
  for rayCount in range(0,scrW/dscale,1):
    ray = [posx, posz]
    dra = degreeToRadians(rayAngle)
    rayCos = cos(dra) / raycastprecision
    raySin = sin(dra) / raycastprecision
    wall = 0
    while (wall == 0):
      ray[0] = ray[0] + rayCos
      ray[1] = ray[1] + raySin
      wall = map[floor(ray[1])][floor(ray[0])]
    dist = sqrt(pow(posx - ray[0], 2) + pow(posz - ray[1],2))
    odist = ceil(dist)
    ldist = dist
    dist = dist * cos(degreeToRadians(rayAngle-plyangle))
    wallheight = floor(scrHh / dist)
    texture = textures[wall-1]
    tposx = floor((texturesize*(ray[0]+ray[1]))%texturesize)
    set_pen("thick","solid")
    #set_color(200,250,200)
    #draw_line(rayCount,0,rayCount,scrHh - wallheight)
    set_color(255-ceil(ldist/2),230-ceil(ldist),100-ceil(odist))
    #draw_line(rayCount*dscale, scrHh, rayCount*dscale, wallheight)
    fill_rect(rayCount*dscale,scrHh-wallheight,dscale,wallheight*2)
    #drawtexture(rayCount*dscale, wallheight,tposx,texture)
    #set_color(200,200,255)
    #draw_line(rayCount, scrHh + wallheight, rayCount, scrH)
    rayAngle = rayAngle + raycastincangle*dscale

def processinput():
  global posz
  global posx
  global posy
  global plyangle
  key = get_key()
  if key == "w" or key == "8":
    plycos = cos(degreeToRadians(plyangle)) *0.5
    plysin = sin(degreeToRadians(plyangle))*0.5
    nx = posx + plycos
    nz = posz + plysin
    if map[floor(nz)][floor(nx)] == 0:
      posx = nx
      posz = nz
  if key =="s" or key == "2":
    plycos = cos(degreeToRadians(plyangle))*0.5
    plysin = sin(degreeToRadians(plyangle))*0.5
    nx = posx - plycos
    nz = posz - plysin
    if map[floor(nz)][floor(nx)] == 0:
      posx = nx
      posz = nz
  if key == "a" or key == "4":
    plyangle = plyangle - 15
  if key == "d" or key == "6":
    plyangle = plyangle + 15
set_window(0,scrW,0,scrH)
def frame():
  set_color(220,200,100)
  fill_rect(0,0,scrW,scrH)
  set_color(240,230,100)
  fill_rect(0,scrHh,scrW,scrHh)
  set_color(235,250,255)
  #fill_rect(150-plyangle - posz,200+sin(posx)*10,10,10)
  use_buffer()
  raycast()
  draw_text(10,10,"fps: "+str(fps))
  paint_buffer()
  processinput()
while True:
  frame()
  if clock() >fpstimer:
    fpstimer = clock() + 1
    fps = fpscounter
    fpscounter = 0
  if clock() > refreshtimer:
    clear_rect(0,0,scrW,scrH)
    refreshtimer = clock() + 6
  if get_key() == "z":
    break
  fpscounter = fpscounter + 1
