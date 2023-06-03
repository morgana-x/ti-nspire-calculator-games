# Very broken dodgy silly raytracing project, if you fork and fix it I will kiss you :pleading:
# Followed online tutorial, I got it working in c++, think issue is with my vector 3 class that I made
# Also this takes 10 years to render on the calculator
from math import *
from ti_system import *
from ti_draw import *
#from vec3 import *
maxraydepth = 3

class vec3:
  def __init__(self,x,y,z):
    self.x = x or 0
    self.y = y or 0
    self.z = z or 0
  def __mul__(self,o):
    if not isinstance(o, self.__class__):
      return self.__class__(self.x*o,self.y*o,self.z*o)
    return self.__class__(self.x*o.x,self.y*o.y,self.z*o.z)
  def __add__(self,o):
    if isinstance(o,self.__class__):
      return self.__class__(self.x + o.x, self.y + o.y, self.z + o.z)
    return vec3(self.x + o, self.y + o, self.z + o)
  def __div__(self,o):
    if isinstance(o,self.__class__):
      return vec3(self.x/o.x,self.y/o.y,self.z/o.z)
    return vec3(self.x/o,self.y/o,self.z/o)
  def __truediv__(self,other):
    return self * 1/other
  def __radd__(self,o):
    return self.__add__(o)
  def __sub__(self,o):
    if isinstance(o,self.__class__):
      return self.__class__(self.x-o.x,self.y-o.y,self.z-o.z)
    return self.__class__(self.x-o,self.y-o,self.z-o)
  def __rsub__(self,o):
    return self.__add__(o)
  def __rmul__(self,o):
    return self.__mul__(o)
  def length_squared(self):
    return self.x*self.x+self.y*self.y+self.z*self.z
  def length(self):
    return sqrt(length_squared)
  def __gt__(self,o):
    return(o.x+o.y+o.z)<(self.x+self.y+self.z)
def dot(v1,v2):
  return v1.x*v2.x+v1.y*v2.y+v1.z*v2.z
class point3(vec3):
  pass
class color(vec3):
  pass
class hitlist (list):
  def hit(r,tmin,tmax,rec):
    r = r
class ray:
  def __init__(self,o,d):
    self.og = o
    self.dr = d
  def origin(self):
    return self.og
  def direction(self):
    return self.dr
  def at(self,t):
    return self.og +( t * self.dr)
def unit_vector(v):
  o = vec3(v.x/v.x,v.y/v.y,v.z/v.z)
  return o
def hitsphere(c,ra,r):
  oc = r.origin() - c
  a = dot(r.direction(),r.direction())
  b = 2 * dot(oc,r.direction())
  c = dot(oc,oc) - ra * ra
  dis = b*b - 4*a*c
  print(dis.x)
  return (dis>vec3(0,0,0))
def ray_color(r):
  o = point3(0,0,-1)
  if (hitsphere(o,0.5,r)):
    print("yay")
    return color(255,0,0)
  unit_dr =r.dr
  t = 0.5 * (unit_dr.y+1.0)
  return color(150,150,200)#(1.0-t)*color(1.0,1.0,1.0) + t*color(0.5,0.7,1.0)
def sp(x,y,c):
  set_color(c.x or 0,c.y or 0,c.z or 0)
  fill_rect(x,y,1,1)




#main

#image
aspectratio = 4/3
imgw = 320
imgh = 240#(imgw/aspectratio)
#camera
viewporth = 2
focallen = 1
viewportw = aspectratio * viewporth
origin = point3(0,0,0)
horizontal = vec3(viewportw,0,0)
vertical = vec3(0,viewporth,0)
hh = horizontal
vv = vertical
h2 = vec3(hh.x/2,hh.y/2,hh.z/2)
v2 = vec3(vv.x/2,vv.y/2,vv.z/2)
lowerleftc = origin - h2 - v2 - vec3(0,0,focallen)
for j in range(imgh):
  for i in range(imgw):
    u = i / (imgw-1)
    v = j / (imgh-1)
    r = ray(origin,lowerleftc+u*horizontal+v*vertical-origin)
   # print(j)
    sp(j, i, ray_color(r))
a = 1
while get_key() != "esc":
  #xaxaxa 
  a = 1
