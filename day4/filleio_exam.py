# # 파일입출력

# # 파일 출력 open 했는데 close 하지않으면 큰일 남 
# f = open('newfile.txt', 'w')
# f.close()

# ## 파일 생성
# f = open('C:\\Sources\\Sample\\test.txt', 'w')
# f.close()
# print('파일이 생성되었습니다')

# newfile.txt 파일입력(읽어오기)
f = open('newfile.txt', 'r', encoding= 'utf-8')
while True:
    line = f.readline()
    if not line:
        break

    print(line)

f.close()


#동일한 값 for 문
lines = f.readlines()
for line in lines:
    
    print(line)

f.close()


