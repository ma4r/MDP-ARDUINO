import serial
import time
import matplotlib.pyplot as plt

output = []


COM = 'COM4'# /dev/ttyACM0 (Linux)
BAUD = 115200
ser = serial.Serial(COM, BAUD, timeout = .1)

time.sleep(3)

end_t = time.time()+5

while time.time()<end_t:
	#print("running")
	val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	output.append(val)

print('done')

n = int(input('Select sample no:'))
with open('straight250.txt','w') as file:
	for elem in output:
		file.write(elem+'\n')

x_ax = []
right = []
left = []
target = []

for elem in output:
	valA = elem.split(',')
	x_ax.append(int(valA[0]))
	target.append(int(valA[1]))
	left.append(int(valA[2]))
	right.append(int(valA[3]))

plt.plot(x_ax,target,'b-',label = 'input')
plt.plot(x_ax,left,'r-', label = 'left')
plt.plot(x_ax,right,'g-',label = 'right')
plt.legend()
plt.show()