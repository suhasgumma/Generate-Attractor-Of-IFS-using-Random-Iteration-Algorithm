import matplotlib.pyplot as plt
import numpy as np

def w1(x,y):
  a = (x*0.5)-(y*0.5)
  b = 0.5
  return [a,b]

def w2(x,y):
  a =( x*0.5) + (y*0.5)+ 1
  b =( x*90 )+ (y*90)
  return [a,b]

def w3(x,y):
  a = (x*0.5) + (y*0.5)
  b = 0.5
  return [a,b]

def w4(x,y):
  a =( x*0.25) + (y*0.25) + (0.75)
  b = 0.75
  return [a,b]


x = np.linspace(0,1,300)
y = np.linspace(0,1,300)

initial = []

for x,y in zip(x,y):
    initial.append([0,y])
    initial.append([5,y])
    initial.append([x,0])
    initial.append([x,5])

initial = np.array(initial)


iters = 7

fig = plt.figure(figsize=(10,10))
colormap = np.array(['r', 'g', 'b','c'])


for i in range(iters):
  print('iteration number : ',str(i+1))
  temp = []
  ifs = []
  for x,y in initial:
    # appending new points
    temp.append(w1(x,y))
    temp.append(w2(x,y))
    temp.append(w3(x,y))
    temp.append(w3(x,y))
    # assigning different colors
    ifs.append(0)
    ifs.append(1)
    ifs.append(2)
    ifs.append(3)

    
  initial = np.array(temp)
  a,b = initial[:,0],initial[:,1]
  
  #plotting fractal at each iteration
  ax = fig.add_subplot(4,2,i+1)
  ax.scatter(a,b,s=1,c = colormap[ifs])
  ax.set_title('iteration '+str(i+1))

  
#displaying th fractal evolution
plt.show()

print("************************************")

x,y = initial[:,0],initial[:,1]

plt.scatter(x,y,s=1)
plt.show()