# 연산자
a = 11
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #정수로 나누기
print(a%b) #나머지


# 문자열 연산
stat1 = 'Hello'
stat2 = 'world'
res = stat1 + stat2
print(res)
res = stat1, stat2
print(res)

# 문자열 연산 + * 만 있음

print(stat1, stat2)
print(stat1+ stat2)
# print(stat1 - stat2) #문자열은 - 안됨
print(stat1*4)
# print(stat1/4) # 문자열 나누기 안됨

# 문자열 길이 
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스(인덱스는 순서 무조건 0부터 시작), 리스트와 동일한 작업
# 한번에 주석처리하기 선택 후 ctrl + /, 해제는 한번더 클릭
# print(stat3[0])
# print(stat3[1])
# print(stat3[2])
# print(stat3[3])
# print(stat3[4])
# print(stat3[5])  # 5글자인 경우 0부터 4까지임

print(stat3[-1])  # 거꾸로 순서로 -1 부터 시작 이번 경우는 5글자로 -5까지 있음
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

# 문자열 자르기
일시 = '2022-01-17 14:39:25'

print(일시[:5], '년')  # 0은 시작이라서 생략가능



print(일시[:4], '년')  # 0은 시작이라서 생략가능
print(일시[5:7], '월')
print(일시[8:10], '일')
print(일시[11:13], '시')
print(일시[14:16], '분')
print(일시[17:], '초')  #마찬가지로 19도 마지막이라 생략가능

print(일시[-5:-3], '분')

list_a = [1,2,3,4,5]
list_a[1] = 19
print(list_a)  # 1번째(실제로는 두번째)자리에 둠

print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)

## 문자열 포맷팅 (게임또는 이메일에서 같은 내용의 메세지를 다른 사람에게 보낼 때 사용자 이름부분을 바꿔줄 수 있는 기능)
첫번째  = '투'
두번째  = '유'
str1 = "i'm so happy {0} U.are {1}?".format(첫번째,두번째)
print(str1)

str2 = f"i'm so happy {첫번째} U.are {두번째}?"  # 가장 간단하고 많이 사용됨
print(str2)
## 숫자 천단위 콤마
money = 10000000000
print(format(money, ',d'))

from datetime import datetime
from traceback import print_tb

now = datetime.now() # 현재 일시생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))  

import math

myPi = math.pi
print(myPi)

print('{0}'. format(myPi))
print('{0:0.2f}'.format(myPi))
print(f'{myPi:0.6f}')

full_name = 'Woojin Kim'
age = 31
greeting = f'''안녕하세요. 저는 {full_name}입니다. 나이는 {age:0.1f}살 이구요.'''

print(greeting)

part_name = full_name.split()
print(part_name)

test = 'Hey, guys'
print(test.split(','))


# |
code = 'TEST|2022|01|17|F45678'
split_codes = code.split('|')
print(split_codes)

# 단어교체
print(full_name.replace('Woojin Kim', 'Ashley'))

# strip == 오라클의 trim이랑 동일
aaa = '   Hello, world ' 
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.lstrip())

# 글자수 찾는거
print(full_name.index('W'))
print(full_name.index('o'))
print(full_name.index('j'))
print(full_name.index('K'))


print(full_name.find('K'))


print(full_name.count('o'))

print('-'. join(full_name))


print(full_name.upper())
print(full_name.lower())  # 오라클의 이니캡처럼 첫 글자만 대문자화 없음


