# mycar.py
from vehicle import Car


if __name__== '__main__':
    mycar = Car('98항 5678', '흰색')
    # mycar.차량번호 = '98항 5678'
    # mycar.색상 = '흰색'
    mycar.연료 = '경유'
    # mycar.__제조사 = '기아'
    mycar.출고년도 = 1999
    # mycar.기어단수 = '7단'

    # print(mycar.__제조사)
    # print(mycar.연료)
    # print(mycar.기어단수)
    mycar.제조사입력('쌍용')
    mycar.제조사확인()

    mycar.전진한다(2)
    print(mycar)