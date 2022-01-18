# 기본 for문

arr = [1,2,3,4,5] # = list(range(1,6))

for i in arr: 
    print(f'{i:2.1f}')  # f'{i:0.00f} 는 소수점으로 출력하겠다는 뜻


# 튜플로 for 문
# arr2 = ('me', 'my', 'friend', 'jane')

# for item in arr2:
#     print(f'{item:>10}')

# 합게 for문 
numbers = list(range(1,11,2)) # 1~10 까지 홀수만

res = 0
for item in numbers:
    res += item 

print(f'{numbers[-1]} 까지의 총 합은 {res} 입니다.')


# 홀수 짝수 구분
numbers = list(range(1,21))

for item in numbers:
    if item % 2 == 1: # item % 2 == 0 짝수, item % 2 == 1 홀수
        print(f'{item}은 홀수')

# 13이상이면 탈출 break
numbers = list(range(1,21))

for item in numbers:
    if item > 12: 
        break   # 값이 위 조건일 경우에 탈출, 값이 안 나옴

    if item % 2 == 1: # item % 2 == 0 짝수, item % 2 == 1 홀수
        print(f'{item}은 홀수')

# 해당 값을 빼고 계속 되는 것 continue
for item in numbers:
    if item == 15: 
        continue   # 15를 빼고 계속 수행하는것

    if item % 2 == 1: # item % 2 == 0 짝수, item % 2 == 1 홀수
        print(f'{item}은 홀수')

## 구구단
print('구구단 프로그램')
for i in range(2,10): # 2~9 까지
    print(f'{i}단 시작')
    for j in range(1,10): #1~9 까지 
         print(f'{i}x{j} = {i*j:2d}', end='  ')
    print('')  # = print() 각 단마다 줄을 바꿀 수 있도록 설정하는것(print는 한줄 내리는 것)

# inline for 문
a = [1,2,3,4]
result = [i* 3 for i in a]
print(result)

#기존 for 문, 위와 동일
t=[]
for i in a:
    t.append(i*3)

print(t)


