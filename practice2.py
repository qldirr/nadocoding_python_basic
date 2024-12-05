# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)   # 제곱
print(5%3)   # 나머지
print(10%3)
print(5//3)   # 몫

print(10 > 3)  # True
print(4 >= 7)   # False
print(10 < 3)  # False
print(5 <= 5)   # True

print(3 == 3)   # True
print(4 == 2)   # False
print(3+4 == 7)   # True
print(1 != 3)   # True
print(not (1 != 3))   # False

print((3 > 0) and (3<5))  # True
print((3 > 0) & (3<5))  # True

print((3 > 0) or (3 > 5))  # True
print((3 > 0) | (3 > 5))   # True

print(5 > 4 > 3)   # True
print(5 > 4 > 7)   # False


# 간단한 수식
print(2 + 3 * 4)   # 14
print((2 + 3) * 4)   # 20
number = 2 + 3 * 4   # 14
print(number)
number = number + 2   # 16
print(number)
number += 2   # 18
print(number)
number *= 2   # 36
print(number)
number /= 2   # 18
print(number)
number -= 2   # 16
print(number)

number %= 5   # 1
print(number)


# 숫자 처리 함수
print(abs(-5))   # 절댓값
print(pow(4, 2))   # 제곱, 4*4=16
print(max(5, 12))   # 촤댓값
print(min(5, 12))   # 최솟값
print(round(3.14))   # 반올림, 3
print(round(4.99))   # 반올림, 5

from math import *
print(floor(4.99))  # 내림, 4
print(ceil(3.14))   # 올림, 4
print(sqrt(16))   # 제곱근, 4


# 랜덤 함수
from random import *
print(random())    # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10)   # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10))   # 0 이상 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)   # 1 이상 10 이하의 임의의 값 생성

print(int(random() * 45) + 1)   # 1 이상 45 이하의 임의의 값 생성

print(randrange(1, 46))   # 1 이상 46 미만의 임의의 값 생성

print(randint(1, 45))   # 1 이상 45 이하의 임의의 값 생성

#############################################################

# Quiz) 새로운 스터디 모임을 만들었다
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했다
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성해라

# 1. 랜덤으로 날짜 뽑아야함
# 2. 월별 날짜는 다름을 감안해 최소 일수인 28 이내로 정함
# 3. 매월 1~3일은 스터디 준비때문에 제외

# ex) 오프라인 스터디 모임 날짜는 매월 X일로 선정되었습니다.

meeting = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월'+ str(meeting) + '일로 선정되었습니다.')