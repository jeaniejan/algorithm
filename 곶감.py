#3_8 곶감(모래시계)
N=int(input())
a=[list(map(int,input().split()))for _ in range(N)]
M=int(input())
for i in range(M):
    r,t,k=map(int,input().split()) # 행,방향,k개
    if t==0:
        for _ in range(k):
            a[r-1].append(a[r-1].pop(0))
    else:
        for _ in range(k):
            a[r-1].insert(0,a[r-1].pop())
            
res=0
s=0
e=N-1

for i in range(N):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<N//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
    