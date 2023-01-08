#k번째 약수출력

N,K=map(int,input().split())
n=0

for i in range(1,N+1):
    if N%i==0:
        n+=1
    if(n==K):
        print(i)
        break
else:
    print('-1')