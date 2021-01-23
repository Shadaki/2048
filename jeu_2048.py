from ion import *
from kandinsky import *
from random import *

squares=[[0]*4 for i in range(4)]
squaresTmp=[[-1]*4 for i in range(4)]
colors=["#a0a0a0","#aaaac8","#f0a0a0","#f08c8c","#e66e6e","#f06464","#ff5050","#dcdc3c","#d2d232","#cdcd23","#c3c314","#b4b400","#32b464"]+["black"]*500
d=-1
score=0
hScore=26548

fill_rect(220,7,94,207,"#787878")
draw_string("Score",240,65,"white","#787878")
draw_string("Highscore",222,120,"white","#787878")

def addSquare():
  a=randint(0,15)
  while squares[a//4][a%4]!=0:
    a=randint(0,15)
  b=randint(0,9)
  if b==0: squares[a//4][a%4]=2
  else: squares[a//4][a%4]=1
addSquare()
addSquare()

while True:
  draw_string(str(score),265-5*len(str(score)),83,"white","#787878")
  draw_string(str(hScore),265-5*len(str(hScore)),138,"white","#787878")  
  for x in range(4):
    for y in range(4):
      sq=squares[x][y]
      if sq!=squaresTmp[x][y]:
        fill_rect(7+y*52,7+x*52,51,51,colors[sq])
        if sq!=0: draw_string(str(2**sq),y*52+33-5*len(str(2**sq)),x*52+24,"white",colors[sq])
  squaresTmp=[squares[i][:] for i in range(4)]
  
  dTmp=d;d=-1
  if keydown(0): d=0
  elif keydown(1): d=1
  elif keydown(2): d=2
  elif keydown(3): d=3
  else: continue
  if d==dTmp: continue
  
  for x in range(4):
    if d==0: row=squares[x][:]
    elif d==3: row=squares[x][::-1]
    elif d==1: row=[squares[i][x] for i in range(4)]
    elif d==2: row=[squares[3-i][x] for i in range(4)]
    noFusion=-1
    for y in range(1,4):
      if row[y]==0: continue
      if row[y] in row[y-1::-1]:
        compY=(y-1)-row[y-1::-1].index(row[y])
        if row[compY+1:y]==[0]*(y-compY-1) and noFusion!=compY:
          score+=2*2**row[y]
          noFusion=compY
          row[compY]+=1
          row[y]=0
      if 0 in row[:y]:
        fSpace=row[:y].index(0)
        row[fSpace]=row[y]
        if fSpace!=y: row[y]=0
    if d==0: squares[x]=row[:]
    elif d==3: squares[x]=row[::-1]
    elif d==1:
      for i in range(4):
        squares[i][x]=row[i]
    elif d==2:
      for i in range(4):
        squares[3-i][x]=row[i]
  if squares!=squaresTmp:
    addSquare()
