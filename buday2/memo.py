# R 버젼 변경시는 반드시 제거하고 프로그램 설치된 폴더에서 잔여폴더 제거하고 R 다른버전으로 설치
# R 설치후에 R스튜디오 설치해야함.
# R은 인터페이스가 별로, 메모리 사용량이 R스튜디오보다 작다

# R에서는 명목형 변수의 factor가 있다.
# 자료형 확인은 str(변수명)으로 확인가능.
# factor는 자료split안되지만, 유니크한 레벨을 갖고 있음.
# => plot(변수)했을때 count집계가 가능함.
# 문자자료를 factor로 변경하는 방법은 as.factor(변수)임.
#  