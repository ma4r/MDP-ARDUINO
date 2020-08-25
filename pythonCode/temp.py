with open('fopdt.txt','r') as file:
    txt = file.read().split('\n')

time = 0
open('fopdt.txt','w').close()
u = 300
with open('fopdt.txt','a') as file:
    for elem in txt:
        if time >= 3000:
            u = 250
        file.write(str(time)+","+str(u)+","+elem+"\n")
        time+=5