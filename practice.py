
# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(8*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print('ㅋㅋㅋㅋ')
print('ㅋ'*9)   # 문자열로 연산도 가능


# boolean 자료형
print(5 > 10)   # False
print(5 < 10)   # True
print(True)
print(False)
print(not True)   # False
print(not False)   # True
print(not (5 > 10))   # True


# 변수
# 애완동물 소개해주세요
name = '연탄이'
animal = '강아지'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '이름은 ' + name)
hobby = '공놀이'  # 변수 재할당
# print(name+ '는 ' + str(age) + ' 살이고 ' + hobby + '을 좋아함')   # 숫자, boolean는 문자열로 변환
print(name, '는 ' , age, ' 살이고 ', hobby, '을 좋아함')   # '+' 말고 ','로도 연결 가능 -> '+'는 문자열 합치기
print(name + '는 어른일까요?' + str(is_adult))

''' 여러 줄 주석 
    여러 줄 주석
'''
##########################################################

''' 
Quiz) 변수를 이용해 다음 문장을 출력해라

변수명 : station
변수값 : "사당", "신도림", "인천공항" 순서대로 입력
출력 문장 : XX 행 열차가 들어오고 있습니다. '''
station = '사당'  
print(station + '행 열차가 들어오고 있습니다.')