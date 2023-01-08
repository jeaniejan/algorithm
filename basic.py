
a=2
print(a)
A=3
print(a,3)
a,b,c=1,2,3
print(a,b,c)

#값 교환
a,b=10,20
print(a,b)
a,b=b,a
print(a,b)

#자료형
a=123456789123456789
print(a)
a=12.3456789123456789
print(a)
a='student' #따옴표 꼭 붙여야 함!
print(type(a))

#출력방식
a,b,c=10,20,30
print(a,b,c)
print(a,b,c,sep=', ')
print(a,b,c,sep='\n')

print(a,end=' ') #줄바꿈 없음
print(b,end=' ')
print(c)

'''
변수입력과 연산자
'''
a,b=input("숫자를 입력하세요: ").split()
print(a+b) #a,b는 문자
a=int(a)
b=int(b)#a,b=map(int,input("숫자를 입력하세요: ").split())
print(type(a))
print(a+b)
print(a//b)#몫
print(a%b)#나머지
print(a**b)#거듭제곱

'''
조건문 if(분기,중첩)
'''
x=10
if(x==10):
    print("성공!")

x=13
if(x>10):
    if(x%2==1):
        print("10 이상의 홀수")



x=7
if 0<x<10:
    print("10 미만의 자연수")




x=10
if x>0:
    print("양수")
else:
    print("음수")


x=93
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')


'''
반복문(for,while)
'''
a=range(10)
print(list(a))#a는 0~9

a=range(1,11)
print(list(a))#a는 1~10

for i in range(10):
    print(i)

for i in range(10,0,-2):#10부터 1까지 2씩 작아짐
    print(i)

i=1
while i<=10:
    print(i)
    i=i+1

i=10
while i>=1:
    print(i)
    i=i-1

i=1
while True: #무한반복
    print(i)
    i+=1
    if(i>=10):
        break#특정조건에서 멈춤


for i in range(1,11):
    if i%2==0:
        continue #1부터 10까지의 홀수만 출력
    print(i)


for i in range(1,11):
    print(i)
    if i>15:
        break;  #for-else
else:           #for문이 정상적으로 종료되면 else문을 출력하고, 중간에 break를 당하면 출력안 
    print(11)


#1부터 n까지 홀수출력하기
    n=input("숫자 입력: ")
    n=int(n)#정수로 변환
    for i in range(1, n+1):
        if i%2==1:
            print(i)

#1부터 n까지의 합 구하기
    a=0
    n=int(input())
    for i in range(1,n+1):
        a+=i
        i+=1
    print(a)
        

#n의 약수 출력하기
    n=int(input())
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
            i+=1

'''
중첩 반복문(2중 for문)
'''
for i in range(5):
    print('i:',i,sep=' ',end=' ')
    for j in range(5):
        print('j:',j,sep=' ',end=' ')
    print()




for i in range(5):
    for j in range(5):
        print('*',end='')
    print()


for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()


for i in range(5):
    for j in range(i+1,6): #    for j in range(5-i):
        print('*',end='')
    print()



'''
문자열과 내장함수
'''
msg='It is Time'
print(msg.upper())#대문자화
print(msg.lower())#소문자화
print(msg)

tmp=msg.upper()
print(tmp)
print(tmp.find('T'))#첫번째로 검색된 인덱스 반환
print(tmp.count('T'))#검색된 횟수 반환

print(msg)
print(msg[:2])#2번 전까지 출력
print(msg[3:5])#3번부터 5번전까지

print(len(msg))
for i in range(len(msg)):#한글자씩 출력
    print(msg[i],end='')
print()


for x in msg:#msg의 문자열에 차례차례 접근
    print(x,end=' ')
print()


for x in msg:
    if x.isupper():#x가 대문자이면 참,소문자이면 거짓
        print(x,end='')
print()


for x in msg:
    if x.islower():#x가 소문자이면 참,대문자이면 거짓
        print(x,end='')
print()


for x in msg:
    if x.isalpha():#x가 알파벳이면 참,공백이면 거짓
        print(x,end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x))#아스키넘버로 변환

tmp='az'
for x in tmp:
    print(ord(x))#아스키넘버로 변환

tmp=66
print(chr(tmp))#아스키넘버를 문자로 변환


'''
리스트와 내장함수(1)
'''
import random as r
a=list()
print(a)

b=[1,2,3,4,5]
print(b)
print(b[0])

a=list(range(1,11))
print(b)

c=a+b
print(c)

print(b)
b.append(6)
print(b)

b.insert(3,7)
print(b)

b.pop()#뒤에서부터 제거
print(b)
b.pop(3)#선택한 인덱스의 숫자 제거
print(b)

b.remove(4)#숫자 4를 제거
print(b)

print(b.index(5))#숫자 5의 인덱스 번호 반환


b=list(range(1,11))
print(b)
print(sum(b))
print(max(b))
print(min(b))

print(min(3,6,1))

print(b)
r.shuffle(b)#b를 무작위로 섞음
print(b)

b.sort(reverse=True)#내림차순 정렬
print(b)

b.sort()#오름차순 정렬
print(b)

b.clear()#배열의 요소들 모두 삭제
print(b)


'''
리스트와 내장함수(2)
'''
a=[23,12,36,53,19]
print(a[:3])#인덱스 0부터 3전까지 출력
print(a[1:4])#인덱스 1부터 4전까지 출력
print(len(a))


for i in range(len(a)):
    print(a[i],end=' ')
print()

#둘이 같은 결과임

for x in a:
    print(x,end=' ')
print()


for x in enumerate(a): #튜플 출력
    print(x)

b=(1,2,3,4,5)
print(b[0])
#b[0]=7  #에러/튜플은 수정불가
#print(b[0])


for x in enumerate(a):
    print(x[0],x[1])
print()

for index,value in enumerate(a):
    print(index,value)
print()


if all(x<60 for x in a):#괄호 안의 조건에 모두 통과해야 참
    print('yes')
else:
    print("no")

if any(x<11 for x in a):#괄호 안의 조건에 하나라도 맞는게 있으면 
    print('yes')
else:
    print('no')


'''
2차원 리스트의 생성과 접근
'''
a=[0]*3
print(a)

a=[[0]*3 for _ in range(3)]
print(a)
a[0][1]=1
a[1][1]=2
print(a)


for x in a:
    print(x)

for x in a:
    for y in x:
        print(y,end=' ')
    print()




'''
함수 만들기
'''
def add(a,b):
    c=a+b
    print(c)

add(3,2)


def add(a,b):
    c=a+b
    return c

x=add(3,2)
print(x)


def add(a,b):
    c=a+b
    d=a-b
    return c,d

print(add(3,2))#튜플로 값 두개 반환



def isPrime(x):#소수출력 함수
    for i in range(2,x):
        if x%i==0:
            return False
    return True
        
    
a=[12,13,7,9,19]

for y in a:
    if isPrime(y):
        print(y,end=' ')



'''
람다 함수
'''
def plus_one(x):
    return x+1

print(plus_one(2))


plus_two=lambda x:x+2
print(plus_two(1))

a=[1,2,3]
print(list(map(plus_one,a)))
print(list(map(lambda x:x+1,a)))