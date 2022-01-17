# 변수 - 파이선의 변수에는 제약이 거의없다
from re import A


a = '헬로우'
print(a) 

a = 3.141592
print(a) 

a = 10
print(a)

a = 999999999999999
print(a)

a = 1 / 10
print(a)


# 변수값을 지정(할당) - assign 방법
a = 3
# 3 = a  # left value 는 어떤 값을 담는 통이 되야함(변수)
b = 3.141592
c = 'python'
d = (1,2,3) #튜플
e = [1,2,3,4] #리스트
f = [7, '8', '$', a] # 파이썬의 장점(모든지 담을 수 있음)

# 변수명(숫자,특수문자 먼저 시작x, 영문자(띄워쓰기x,_로사용))
val = 10
val2 = 20
val4 = 30
#4val = 40
#-val = 5-
#*val = 60
#val_of change =99
chain_reaction = 108
chainReaction = 109
#chain Reaction = 109
#val- = 11
#val$ = 99
val_ = 999
Val_ = 9080 #대소문자 구분
print(val_)
print(Val_)
MyAcoountOfBank = 1
은행계좌금액 = 1

print(id(val_))
print(id(Val_))


# 변수타입 확인
print(type(val_))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

