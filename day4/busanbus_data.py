# 부산버스 노선별 이용건수
import csv #표준라이브러리

file_name = '부산버스정보.csv'
f = open('./부산버스정보.csv',mode='r', encoding='utf-8')

reader = csv.reader(f, delimiter=',')   #delimiter 구분자 여기선 ',' 사용
next(reader)   # 헤더를 없애는 역학
for line in reader:
    print(line)

f.close()
