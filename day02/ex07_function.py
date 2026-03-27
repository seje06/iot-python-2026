# ex07_function 함수

# 더하기 함수(리턴있는 함수)
def add(a, b):
    return a + b

# 파라미터 없는 함수
def test():
    x=10
    return x

# 리턴없는 함수
def sayHello(name):
    print(f'안녕하세요, {name}!')

# 함수 호출
print(add(10, 9))
print(add(10.3, 9))
print(add('문자열', '9.4'))

print('안녕하세요', end = ' ') # end의 기본값은 \n 이것을 ' ' 으로 대체
print('안녕하세요')

result = add(10,4)
print(f'결과는 {result}')

print(test())
sayHello('Hugo')