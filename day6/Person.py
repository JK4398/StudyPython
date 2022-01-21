# Person.py
# Person 클래스
class Person: 
    name = '무명이'  #아직 이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''


    # 생성자
    def __init__(self, name, age) -> None:
        self.name = name
        self.age =  age
        print('Person이 생성 되었습니다.')

    def 소개한다(self) -> None:
        greeting = f'''안녕하세요.저는 {self.name} 입니다.
        {self.gender}구요. {self.age}살입니다.
        '''

        print(greeting)

    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다')

    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다')




if __name__ == '__main__':
    kwj = Person('김우진', 30)  # == __init__(self, name, age):
    # kwj.name = '김우진'
    # kwj.age = 30
    kwj.gender = 'male'
    kwj.height = 176
    kwj.feetsize = 255
    kwj.bloodtype = 'RH+ A'
    

    kwj.소개한다()
    kwj.먹는다('본죽')
    kwj.일한다('핫식스')
    



str


    # p = Person()   # p라는 이름의 Person 객체 생성
    # print(type(p))
    # print(id(p)) # id 값

    # p2 = Person()  # p2 객체 생성
    # print(type(p2))
    # print(id(p2))