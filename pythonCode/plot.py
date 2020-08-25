import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


with open('avg_filtered.txt','r') as file:
    output = file.read().split('\n')
    del output[-1]

x_ax = []
right = []
left = []
target = []
const = 106762
for elem in output:
    valA = elem.split(',')
    x_ax.append(int(valA[0]))
    target.append(int(valA[1]))
    left.append(int(valA[2]))
    right.append(int(valA[3]))
    #left.append(const/int(valA[2]))
    #right.append(const/int(valA[3]))

dy_l = np.mean(left[600:1000])-np.mean(left[0:400])
dy_r = np.mean(right[600:1000])-np.mean(right[0:400])
print(dy_l,dy_r)
fig,ax = plt.subplots(2)
reg_start = 372
reg_end = 400

start = 0
end = 900
ax[0].plot(x_ax[start:end],target[start:end],'b-',label = 'input')
ax[0].legend()
ax[1].plot(x_ax[start:end],left[start:end],'rx', label = 'left')
ax[1].plot(x_ax[start:end],[np.mean(left[600:1000])]*(end-start),'r-', label = 'left')
ax[1].plot(x_ax[start:end],[np.mean(left[0:400])]*(end-start),'r-', label = 'left')
ax[1].plot(x_ax[start:end],[np.mean(right[0:400])]*(end-start),'g-', label = 'right')
ax[1].plot(x_ax[start:end],[np.mean(right[600:1000])]*(end-start),'g-', label = 'right')
ax[1].plot(x_ax[start:end],right[start:end],'gx',label = 'right')
ax[1].legend()
plt.show()


t = np.array(x_ax[reg_start:reg_end])
reg_l = linregress(t,left[reg_start:reg_end])
reg_r = linregress(t,right[reg_start:reg_end])

fig,ax = plt.subplots(2)
ax[0].plot(x_ax[start:end],target[start:end],'b-',label = 'input')
ax[0].legend()
ax[1].plot(x_ax[start:end],left[start:end],'rx', label = 'left')
ax[1].plot(x_ax[start:end],right[start:end],'gx',label = 'right')

ax[1].plot(t,t*reg_l[0]+reg_l[1],'r-', label = 'left')
ax[1].plot(t,t*reg_r[0]+reg_r[1],'g-', label = 'right')

ax[1].legend()
plt.show()

print(reg_l[0],reg_r[0])
print((t*reg_l[0]+reg_l[1])[:-1])

