import matplotlib.pyplot as plt
import numpy as np
import itertools

a = [0.05,0.5,0.46,-0.47,0.43,0.42]
b = [0,0,-0.15,-0.15,0.28,0.26]
c = [0,0,0.39,0.17,-0.25,-0.35]
d = [0.6,-0.5,0.38,0.42,0.45,0.31]
e = [0,0,0,0,0,0]
f = [0,1,0.6,1,1,0.7]
p = [0.1,0.1,0.2,0.2,0.2,0.2]

x = np.linspace(0,5,500)
y = np.linspace(0,5,500)

initial = []

for x,y in zip(x,y):
    initial.append([0,y])
    initial.append([5,y])
    initial.append([x,0])
    initial.append([x,5])

initial = np.array(initial)


iters = 10000
fig = plt.figure(figsize=(10,10))

j=0

for i in range(iters):
  temp = []
  
  for x,y in initial:
    rnd = np.random.choice([0,1,2,3,4,5], p=p)
    nx = a[rnd]*x+b[rnd]*y+e[rnd]
    ny = c[rnd]*x+d[rnd]*y+f[rnd]
    temp.append([nx,ny])
  initial = np.array(temp)

  if (i+1)%1000==0:  
    xs,ys = initial[:,0],initial[:,1]
    ax = fig.add_subplot(5,2,j+1)
    ax.scatter(xs,ys,s=1)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_title('iteration '+str(i+1))
    j+=1

plt.show()

x,y = initial[:,0],initial[:,1]

plt.scatter(x,y,s=1)
plt.xticks([])
plt.yticks([])
plt.show()