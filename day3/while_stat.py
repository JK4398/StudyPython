# while 문  값에 맞으면 계속 반복함
hit = 0

while hit < 19: # 이 값이 참인 동안
    hit = hit +1 # hit += 1 동일함
   
    if hit > 10:
         break
    print(f'나무를 {hit}번 찍습니다.')

    
# for문 
for hit in range(0,101):
    print(f'나무를 {hit}번 찍습니다.')
