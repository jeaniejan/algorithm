#K번째 큰 수
N,K=map(int,input().split())
a=list(map(int,input().split()))
res=set()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res.add(a[i]+a[j]+a[k])
res=list(res)
res.sort(reverse=True)
print(a[K-1])