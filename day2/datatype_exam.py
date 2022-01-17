# 자료형
from cgi import print_directory
from operator import truediv


print(None)
print(type(None))

print(0 == None)
a = None
print(a)
print(type(a))

# 숫자형
금액 = 12_345_666  #천단위로 헷갈리지 않게 끊어서 기록
print(금액)

# 문자열
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)


bruce_eckel = 'Life is short.\nYou need Python'  #\n (한 줄 밑으로) 탈출문자 escape character
print(bruce_eckel)

bruce_eckel = 'Life is short.\\You need Python'  #\\ 역슬래시를 그대로 사용하고 싶으면 \\ 
print(bruce_eckel)

bruce_eckel = '''Life is short.
You need Python.
난 필요없어...''' 
print(bruce_eckel)  #여러줄일때는 \n  필요없음

# 불형 
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 999)
#print(val_sum == 10)

bl_true = True
print(type(bl_true))
print(bl_true == True)
print(bl_true is True)

print(a is None)  #True
print(val_sum is 1000)  #True

# 의미가 있는 bool 
print(bool(1))  #True
print(bool(0))  #False


# list
b = [1,2,3,4,5,6,7,8,9,10]
print(b)


arr2 = ['Life', 'is', 'short', 'U', 'need', 'Python',3]
print(arr2)

arr3 = [[1,2,3], [4,5,6]]
print(arr3)

# 빈 리스트 생성
arr4 = list()
print(arr4)


# 튜플
tuple1 = (1,2,3,4,5)
print(tuple1)

# 딕셔너리
spiderman = {'name': '피터 파커', 
             'age' :18,
             'weapon' : '웹슈터' }
print(spiderman)

# 집합  중복 제거에 좋음, 잘 사용되지않음
set_int = set([1,2,3,4,5,6,7,1,2,2])
print(set_int)