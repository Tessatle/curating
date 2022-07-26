with open('26_1.txt') as f:
    n, k = list(map(int, f.readline().split()))
    mas=[int(x) for x in f]
    mas.sort(reverse=True)
    
def isprime(n):
    d=2
    while d*d<=n:
        if n%d==0:
            return False
        d+=1
    return True

summ=0
p=0

for i in range (k):
    if isprime(mas[i]):
        summ+=(mas[i]+1)
        p+=1
    else:
        summ+=mas[i]
        
print(summ, p)
