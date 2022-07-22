import math

with open('26_2.txt') as f:
    n, s = map(int, f.readline().split())
    mas=[]
    for i in f:
        i=[int(x) for x in i.split()]
        mas.append(i[0]*(i[1]/100))
    mas.sort(reverse=True)

k=0
summ=0

for i in mas:
    k+=1
    summ+=i
    if summ>=s:
        break

print(k, math.ceil(summ))
