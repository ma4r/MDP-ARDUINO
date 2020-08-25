from os import listdir

records = [f for f in listdir('.') if f[:6] == 'output']

count = len(records)

arr = []
for i in range(count):
    with open('output'+str(i)+'.txt', 'r') as file:
        temp = file.read().split('\n')
    del temp[-1]
    arr.append(temp)
result = []
for i in range(len(arr[0])):

    timeA = []
    for j in range(count):
        timeA.append(int(arr[j][i].split(',')[0]))
    time = max(set(timeA), key=timeA.count)
    time = str(time)

    input_signalA = []
    for j in range(count):
        input_signalA.append(int(arr[j][i].split(',')[1]))
    input_signal = max(set(input_signalA), key=input_signalA.count)
    input_signal = str(input_signal)

    sum_l = 0
    for j in range(count):
        sum_l += int(arr[j][i].split(',')[2])
    l = str(int(sum_l / count))

    sum_r = 0
    for j in range(count):
        sum_r += int(arr[j][i].split(',')[3])
    r = str(int(sum_r / count))

    temp = ','.join([time, input_signal, l, r])
    result.append(temp)

with open('avg.txt', 'w') as file:
    for elem in result:
        file.write(elem+'\n')
