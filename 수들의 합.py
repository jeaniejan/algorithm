#3_5 수들의 합
N,M=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
for i in range(len(a)):
    sum=a[i]
    for j in range(i+1,len(a)):
        if sum!=M:
            sum+=a[i]
        if sum==M:
            cnt+=1
            break
print(cnt)
    

