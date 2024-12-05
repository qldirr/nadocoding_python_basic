# 문자열
sentence = '나는 소년이다'
print(sentence)
sentence2 = "파이썬은 쉽다"
print(sentence2)
sentence3 = """
나는 소년이고
파이썬은 쉽다
"""
print(sentence3)


# 슬라이싱
jumin = '991130-1234567'
print('셩별: ' + jumin[7])   # 7번 인덱스의 문자열 출력
print("년도: " + jumin[0:2])   # 0~1 인덱스 문자열 출력
print("월: " + jumin[2:4])    # 2~3 인덱스 문자열 출력
print("일: " + jumin[4:6])    # 4~5 인덱스 문자열 출력
print("생년월일: " + jumin[:6])    # 처음~5 인덱스 문자열 출력
print('뒤 7자리: ' + jumin[7:])    # 7~끝 인덱스 문자열 출력
print('뒤 7자리(뒤부터): ' + jumin[-7:])    # 맨뒤 7~끝 인덱스 문자열 출력


# 문자열 처리 함수
python = 'Python is Amazing'
print(python.lower())   # 소문자
print(python.upper())   # 대문자
print(python[0].isupper())   # True, 첫번째 문자가 대문자냐
print(len(python))   # 문자열 길이
print(python.replace('Python', 'Java'))   # 특정 문자열 찾고 다른 문자열로 대체

index = python.index('n')
print(index)   # 'n'이라는 글자가 몇번째 인덱스에 있는지, 5
index = python.index('n', index + 1)    # 5번 인덱스 이후에 'n'이 몇번째에 있는지
print(index)   # 15(두번째 'n')

print(python.find('n'))   # 찾는 문자열이 몇번째 인덱스에 있는지, 5 / 찾는 문자열이 없으면 -1 반환
# print(python.index("Java"))   # Error, index()에서는 찾는 문자열이 없으면 Error를 반환

print(python.count('n'))   # 해당 문자열이 몇번 나오는지, 2


# 문자열 포맷
print('a' + 'b')
print('a', 'b')

## 1)
print('나는 %d살입니다' % 20)   # 정수
print('나는 %s를 좋아한다' % '파이썬')  # 문자열
print('Apple %c로 시작한다' % 'A')  # character
## %s
print('나는 %s살입니다' % 20)
print('나는 %s색과 %s색을 좋아한다' % ("빨간", "파란"))

## 2)
print('나는 {}살입니다' .format(20))
print('나는 {}색과 {}색을 좋아한다' .format("빨간", "파란"))
print('나는 {0}색과 {1}색을 좋아한다' .format("빨간", "파란"))
print('나는 {1}색과 {0}색을 좋아한다' .format("빨간", "파란"))   # 인덱스를 지정 가능

## 3) 
print('나는 {age}살이며 {color}색을 좋아한다' .format(age = 20, color = '빨간'))
print('나는 {age}살이며 {color}색을 좋아한다' .format(color = '빨간', age = 20))    # 변수 지정 가능

## 4) v3.6 이상
age = 20
color = '빨간'
print(f'나는 {age}살이며 {color}색을 좋아한다')


# 탈출 문자
## /n : 줄바꿈
print('백문이 불여일견\n백견이 불여일타')   

## \', \" : 문자열 내 따옴표
print("저는 '김어진'입니다")   # 문자열 내 ' 사용
print('저는 "김어진"입니다')   # 문자열 내 " 사용
print("저는 \"김어진\"입니다")   # 문자열 내 " 사용
print("저는 \'김어진\'입니다")   # 문자열 내 " 사용

## \\ : 문자열 내 \
print('C:\\Users\\LG\\Desktop\\PythonWorkspace')

## \r : 커서를 맨앞으로 이동
print('Red Apple\rPine')   # PineApple

## \b :  백스페이스(한 글자 삭제)
print('Redd\bApple')  # RedApple

## \t : 탭
print('Red\tApple')   # Red   Apple

#######################################################

# Quiz) 사이트별로 비번을 만들어주는 프로그램 작성
# ex. http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + '!'로 구성(!)
# ex. 생성된 비번 : nav51!
site = 'http://naver.com'
my_str = site.replace("http://", '')  # 규칙1
my_str = my_str[:my_str.index('.')]  # 규칙2, 처음부터 '.'인덱스 전까지(0~4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'   # 규칙3
print('{0}의 비번은 {1}입니다'.format(site, password))

