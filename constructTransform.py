# Gole, Karteek P.
# kpg3522
# 2019-03-02

def constructTransform(w, v, width, height) :
#---------#---------#---------#---------#---------#--------#

 ##################################################
 # Put your Python code for computing fx, fy, gx, gy, sx, sy,
 # ax, and ay here.
 # Return ax, ay, sx, and sy as a tuple.
 ##################################################

#---------#---------#---------#---------#---------#--------#

  fx = -(w[0])
  fy = -(w[1])
  gx = width*v[0]
  gy = height*v[1]
  sx = ((width*(v[2]-v[0]))/(w[2]-w[0]))
  sy = ((height*(v[3]-v[1]))/(w[3]-w[1]))
  ax = fx*sx + gx
  ay = fy*sy + gy
  return(ax,ay,sx,sy)


def _main():
  w = (-1.0, -2.0, 4.0, 5.0)
  v = (0.15, 0.15, 0.85, 0.85)
  width = 500
  height = 400

  values= constructTransform(w, v, width, height)
  ax, ay, sx, sy = values

  print(f'Values          : {values}')
  print(f'Test transform  : ax {ax}, ay {ay}, sx {sx}, sy {sy}')


if __name__ == '__main__':
  _main()

