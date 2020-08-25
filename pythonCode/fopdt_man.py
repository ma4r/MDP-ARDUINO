import matplotlib.pyplot as plt
import numpy as np

with open('avg.txt','r') as file:
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

fig,ax = plt.subplots(2)
start = 0
end = 400
ax[0].plot(x_ax[start:end],left[start:end],'b-',label = 'left')
ax[0].plot(x_ax[start:end],right[start:end],'g-',label = 'right')
ax[0].legend()
start = 600
end = 1000
ax[0].plot(x_ax[start:end],left[start:end],'b-')
ax[0].plot(x_ax[start:end],right[start:end],'g-')
ax[0].legend()
start = 419
end = 420
n = 419
print(x_ax[n],left[n],right[n],target[n])
ax[1].plot(x_ax[419:430],target[419:430],'ro', label = 'left')
# ax[1].plot(x_ax[start:end],left[start:end],'bo', label = 'left')
# ax[1].plot(x_ax[start:end],right[start:end],'go',label = 'right')
plt.show()

dy_l = np.mean(left[600:1000])-np.mean(left[0:400])
dy_r = np.mean(right[600:1000])-np.mean(right[0:400])


du = np.mean(target[600:1000])-np.mean(target[0:400])

kp_l = dy_l/du
kp_r =  dy_r/du

print(kp_l,kp_r)

