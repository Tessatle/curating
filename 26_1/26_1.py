with open('26_1.txt') as f:
    n=int(f.readline())
    mas=[int(x) for x in f]
    mas.sort(reverse=True)

def isprime(n):
    d=2
    while d*d<=n:
        if n%d==0:
            return False
        d+=1
    return True

mas_pr=[]
s1, s2 = 0, 0

for i in mas:
    if isprime(i):
        mas_pr.append(i)
    else:
        s1+=i
        s2+=i

k1=len(mas_pr)//4
k2=len(mas_pr)//2

if k1!=0:
    for i in mas_pr[k1::]:
        s1+=i
if k2!=0:
    for i in mas_pr[:k2:]:
        s2+=int(i//2)
    for i in mas_pr[k2::]:
        s2+=i

print(min(s1, s2), max(s1, s2)-min(s1, s2))
