# ex15_oop. 객체지향

class Dog:
    pass

if __name__ == '__main__':
    poppy = Dog() # 클래스 인스턴스 객체 생성
    poppy.name = '뽀삐'
    poppy.age = 3

    print(f'강아지 이름 : {poppy.name}, 나이 : {poppy.age}')