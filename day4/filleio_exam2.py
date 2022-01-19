# # 파일쓰기  w로 쓰고 a로 내용 추가함
# f = open('writefile.txt', 'w', encoding='utf-8')

# f.write('저는 한국사람입니다.\n')

# texts = ['저는 한국사람이죠\n', '올해는 2022년이 되었습니다.\n']
# f.writelines(texts)

# f.close()


# f = open('writefile.txt', 'a', encoding='utf-8')
# f.write('내용 추가할게요!')
# f.close()

#파이썬은 가능한 부분(대부분 다른 언어는 open 했으면 close 해야하는데 여긴 부분 추가 가능)

f = open('writefile.txt', 'r', encoding='utf-8')

for line in f:
    print(line)

f.close()


