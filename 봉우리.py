#3_9 봉우리
dx=[-1,0,1,0]
dy=[0,1,0,-1]
N=int(input())
a=[list(map(int,input().split()))for _ in range(N)]
a.insert(0,[0]*N)
a.append([0]*N)
for x in a:
    x.insert(0,0)
    x.append(0)
cnt=0
for i in range(1,N+1):
    for j in range(1,N+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
        
