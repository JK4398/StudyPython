# 예외처리 가장중요함. 프로그램의 신뢰성 문제
from logging import exception

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multi(a,b):
    return a*b
    
def divide(a,b):
    res = a/b
    return res

print('사칙연산 시작')
a , b = 4, 1  #f9 누르면 브레이킹 포인트 또는 마우스로 숫자 앞 클릭 17라인 전 실행
numbers = [3,6,9]  # 리스트 생성

try:
    print(f'나누기 결과: {divide(a,b)}')
    res = int(numbers[1]) *8
    num = int(input('수를 입력하세요'))

except ZeroDivisionError as e:
    print(f'나누기 예외. 추가처리1 {e}')
except IndexError as e:
    print(f'나누기 예외. 추가처리2 {e}')
except ValueError as e:
    print(f'제발 숫자만 넣어!')
except Exception as e:
    print(f'알수 없는 예외. 추가처리5 {e}')
    
finally:   # 예외가 발생에 상관없이 값 나오게함.
    print(f'곱하기 결과: {multi(a,b)}')
    print(f'빼기 결과: {minus(a,b)}')
    print(f'더하기 결과: {add(a,b)}')


print('사칙연산 종료')

