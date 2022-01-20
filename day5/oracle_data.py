# oracle_data
# cx_oracle 설치 : pip install cx_oracle
import cx_Oracle as ora # 이름을 ora 로 바꿈

# # makedsn('호스트명/ip주소', portnum, '서비스명')
# dsn = ora.makedsn('localhost', 1521, service_name='orcl')  # 내꺼라 localhost 만약 다른거를 할꺼면 ip/url 작성(보안상)
# #connect(user,password,dsn,encoding)
# conn = ora.connect(user= 'scott', password='tiger', dsn=dsn, encoding='utf-8')

# cur = conn.cursor()

# try:
#     for row in cur.execute('SELECT * FROM emp'):
#         print(row)
# # cur.execute('SELECT COUNT(*) FROM emp')
# # result - cur.fetchone()
# # print(result)
# except ora.DatabaseError as e:
#     print(f'쿼리문이 잘못되었습니다. 13번라인 확인요: {e}')
# finally:
#     cur.close() # 커서 닫고
#     conn.close() # 접속 닫음





#Oracle_data
#cx_oracle 설치 : pip install cx_oracle
from sqlite3 import DatabaseError
from unittest import result
import cx_Oracle as ora
#dse = data source explorer , localhost- 내컴퓨터
#makedsn ('호스트명/ip주소', portnumber, '서비스명')
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
#connect(user, password, dsn, encoding)    utf-8을 넣어야 한글로 나옴
conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'UTF-8')

# DB접속이 성공하면 Connection 부터 cursor() 메서드를 호출하여 객체를 가져옴
cur = conn.cursor()  # 실행결과 데이터를 담을 메모리 객체
try:
    for row in cur.execute('SELECT COUNT(*) FROM emp'):
        print(row)
# cur.execute('SELECT COUNT(*) FROM emp')
# result = cur.fetchone()
# print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 13번라인 확인요 : {e}')
finally:
    cur.close() #커서 부터 먼저 닫고 
    conn.close() # 그다음 DB 접속 닫아야함