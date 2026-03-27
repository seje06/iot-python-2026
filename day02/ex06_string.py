# ex06_string.py 문자열

language = 'python' # List와 동일

print(language[0]) # p
print(language[5]) # n
# print(language[6]) # 에러. C/C++ 마지막 \0이 없음

print(language[-1]) # 역순 인덱스
print(language[0:2]) # 인덱스로 문자열 슬라이싱 0에서 1까지
print(language[0:6:2]) # 인덱스로 문자열 슬라이싱 0에서 5까지 2칸씩
print(language[-3:-1]) # 음수 인덱스로 문자열 인덱싱

## 문장열 내장함수
print(language.upper()) # 문자들 모두 대문자로
print(language.lower()) # 문자들 모두 소문자로

language = 'hello'

print(language.capitalize()) # 첫글자만 대문자로
print(language.replace('llo','y')) # 문자 변환
print(language.count('l')) # 찾는 문자(열) 개수
print(language)

language = "Hello Python Wow!"

print(language.split()) # 공백으로 문자열 자르기

## 포멧팅(formatting)
name = 'Ashely'
age = 36

# 기본
print('이름은 %s, 나이는 %i세 입니다' %(name, age)) # C방식. 지금은 안씀
print("이름은 " + name + ", 나이는 " + str(age) + "세 입니다") # 기본적으로 \n 포함
print("이름은", name, ", 나이는", str(age), "세 입니다")

print('이름은 {0}, 나이는 {1}세 입니다'.format(name,age)) # 과도기 방식
print(f'이름은 {name}, 나이는 {age}세 입니다') # 기본  f-string

# f-string 포맷팅 중
pi = 3.14592
greeting = '안녕'

print(f'{greeting}하세요') # 기본
print(f'{greeting:<10}하세요') # 둘 사이에 10자리 띄울것
print(f'하세요{greeting:>10}하세요') # 둘 사이에 10자리 띄울것
print(f'{greeting:*^10}하세요') # 변수 앞뒤에 *로 채우기

print(f'{pi}')
print(f'{pi:.2f}') # 소수점 2자리까지 반올림해서 출력

print(name[::-1]) # Ashely -> ylehsA