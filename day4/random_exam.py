# random 함수
import random 

print(random.choice(range(1,7)))  # 주사위

#lottery 복권
numbers = list(range(1,46))
# print(numbers) 확인절차
lottery = [] #list()

for i in range(6):
    lottery.append(random.choice(numbers))    # 값을 추가할 때 append 함수

print(lottery)

### 같은 결과 다른 코드
from random import * 

print(random.choice(range(1,7)))  # 주사위

#lottery 복권
numbers = list(range(1,46))
# print(numbers) 확인절차
lottery = [] #list()

for i in range(6):
    lottery.append(choice(numbers))    # 값을 추가할 때 append 함수

print(lottery)