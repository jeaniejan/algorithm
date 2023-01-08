#대표값
N=int(input())
a=list(map(int,input().split()))
avg=int((sum(a)/N)+0.5)
min=a[0]
for idx,x in enumerate(a):
    tmp=abs(x-avg)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(avg,res)