from scipy import signal,misc
from matplotlib import pyplot as plt


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

order = 5
sampling_freq = 200
cutoff_freq = 40
normalized_cutoff_freq = 2 * cutoff_freq / sampling_freq
numerator_coeffs, denominator_coeffs = signal.butter(order, normalized_cutoff_freq)

filtered_signal_l= signal.lfilter(numerator_coeffs, denominator_coeffs, left)[50:]
filtered_signal_r= signal.lfilter(numerator_coeffs, denominator_coeffs, right)[50:]

fig,ax = plt.subplots(3)
ax[0].plot(x_ax[50:],left[50:],'r-', label = 'Left')
ax[0].plot(x_ax[50:],filtered_signal_l,'g-',label = 'Filtered Left')
ax[0].legend()
ax[1].plot(x_ax[50:],right[50:],'r-', label = 'Right')
ax[1].plot(x_ax[50:],filtered_signal_r,'g-',label = 'Filtered Right')
ax[1].legend()
ax[2].plot(x_ax[50:],target[50:])
plt.show()

with open('avg_filtered.txt','w') as file:
    for i in range(50,len(x_ax)):
        temp = [x_ax[i], target[i], filtered_signal_l[i-50], filtered_signal_r[i-50]]
        temp = [str(round(elem)) for elem in temp]
        file.write(','.join(temp) +'\n')

