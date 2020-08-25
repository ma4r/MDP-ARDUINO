import numpy as np
import matplotlib.pyplot as plt
with open('straight250.txt','r') as file:
    output = file.read().split('\n')
    del output[-1]

x_ax = []
right = []
left = []
target = []
const = 106762
for elem in output[100:]:
    valA = elem.split(',')
    x_ax.append(int(valA[0]))
    target.append(int(valA[1]))
    left.append(int(valA[2]))
    right.append(int(valA[3]))

mean_r = np.mean(right)
pred_r = np.linspace(mean_r,mean_r,len(right))
print(mean_r)

mean_l = np.mean(left)
pred_l = np.linspace(mean_l,mean_l,len(left))
print(mean_l)

fig,ax = plt.subplots(2)
ax[0].plot(x_ax,pred_l,'r-',label = 'input')
ax[0].plot(x_ax,left,'g-',label = 'left')
ax[0].legend()
ax[1].plot(x_ax,pred_r,'r-', label = 'Line')
ax[1].plot(x_ax,right,'g-',label = 'right')
ax[1].legend()
plt.show()

