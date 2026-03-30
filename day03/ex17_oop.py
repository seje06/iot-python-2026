# ex17_oop.py 상속

class Animal: # 동물 클래스
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('소리를 낸다')

class Dog(Animal): # 동물 클래스 상속한 개 클래스
    def speak(self):
        print(f'{self.name} 멍멍!',end=' ')
        super().speak()


class Cat(Animal): # 동물 클래스 상속한 고양이 클래스
    def speak(self):
        print(f'{self.name} 냐옹!', end=' ')
        super().speak()

poppy = Dog('뽀삐')
poppy.speak()

navi = Cat('나비')
navi.speak()