# 리스트 연산 arr arrange
from mmap import PROT_READ
from traceback import print_tb


arr = list(range(8))
print(arr)

arr = list(range(1,6))  # 1부터 내가 만들고 싶은 숫자 x (1,x-1)
print(arr)

arr = list(range(2,101, 2))  # 2부터 100까지 짝수만
print(arr)

print(arr[0] + arr[5])

