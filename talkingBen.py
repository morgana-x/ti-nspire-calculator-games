from ti_system import *
from random import *
re = ["no","yes"]
rr = ["boo","hohohoho", "maybe"]
clear_history()
print("ben: ben.")
while get_key() != "esc":
  t = input()
  c = randint(0,10)
  r = randint(0,1)
  z = re[r]
  if (c > 7):
    z = rr[r]
  print("ben: "+z)
