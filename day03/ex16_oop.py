# ex16_oop.py 객체지향 클래스

class Dog:
    # 생성자

    def __init__(self, name):
        self.name = name

    def bark(self): # 첫번째 파라미터 self
        print(f'{self.name}이(가) 짖습니다. 멍멍!')


poppy = Dog(name = "뽀삐")
poppy.bark()
poppy = Dog(name = "초코")
poppy.bark()
