# 1. 리스트 []

## 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ['존', '마크', '톰']
print(subway)

## '존'이 몇번째 칸에 타고있는지??
print(subway.index('존'))   # 인덱스 출력

## '앤디'가 다음 칸에 타면?
subway.append('앤디')   # 맨 뒤에 추가
print(subway)

## '에릭'을 '존'과 '마크'사이에 태움
subway.insert(1, '에릭')   # 해당 인덱스에 추가
print(subway)

## 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())   # 맨뒤에 한명 꺼내서 제외시킴
print(subway)   # 맨 뒤 사람이 없는 상태의 리스트 반환

## 같은 이름의 사람이 몇명 있는지
subway.append('마크')
print(subway.count('마크'))

## 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

## 순서 뒤집기
num_list.reverse()
print(num_list)

## 모두 지우기
num_list.clear()
print(num_list)   # [](빈 리스트)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ['마크', 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)   # 하나의 리스트로 합쳐짐


# 2. 사전 {key:value}
cabinet = {3:'에릭', 100:'존'}
print(cabinet[3])   # vaule 출력 : [key]
print(cabinet[100])

print(cabinet.get(3))   # vaule 출력 : .get(key)
# print(cabinet[5])   # keyError : 없는 키를 호출
# print(cabinet.get(5))   # None : 없는 키를 호출
print(cabinet.get(5, '사용 가능'))   # 5번 key가 없으면 '사용 가능' 출력

print(3 in cabinet)   # 해당 key가 사전 안에 있냐, True

cabinet = {'A-3':'에릭', 'B-100' :'존'}
print(cabinet['A-3'])   # [key]
print(cabinet['B-100'])

## 새 손님
print(cabinet)
cabinet['A-3'] = '텐'   # 기존 key의 값이 변경
cabinet['C-20'] = '톰'   # 새 key가 추가
print(cabinet)

## 간 손님
del cabinet["A-3"]   # 해당 key 삭제
print(cabinet)  

## key 들만 출력
print(cabinet.keys())

## value들만 출력
print(cabinet.values())

## key/value 쌍으로 출력
print(cabinet.items())

## 목욕탕 폐점
cabinet.clear()
print(cabinet)    # {} : 사전 비우기


# 3. 튜플 (value, value) : 변경되지 않는 목록
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])

# menu.add('생선까스')   값을 추가하거나 삭제 불가

(name, age, hobby) = ('쟈니', 20, '코딩')
print(name, age, hobby)


# 4. set(세트) {value, value} : 중복 불가, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)   # {1,2,3} -> 3이 중복되므로 한번만 출력

java = {'kim', 'lee', 'jung'}
python = set(['kim', 'park'])

## 교집합(java/python을 모두 할 수 있음)
print(java & python)   # 'kim'
print(java.intersection(python))  # 'kim'

## 합집합(java/python 둘중 하나라도 할 수 있음)
print(java | python)   # {'kim', 'lee', 'jung', 'park'}
print(java.union(python))   # {'kim', 'lee', 'jung', 'park'}

## 차집합(java는 가능, python 불가능)
print(java - python)   # {'lee', 'jung'}
print(java.difference(python))  # {'lee', 'jung'}

## python 할줄 아는 사람이 늘어남
python.add('jung')
print(python)   # set에 값 추가

## java를 까먹음
java.remove('lee')   # set에 값 삭제
print(java)


# 5. 자료 구조 변경
menu2 = {'coffee', 'juice', 'milk'}
print(menu2, type(menu2))   # set

menu2 = list(menu2)
print(menu2, type(menu2))   # list

menu2 = tuple(menu2)
print(menu2, type(menu2))   # tuple

menu2 = set(menu2)
print(menu2, type(menu2))   # set

###########################################################

# Quiz) 학교에서 파이썬 코딩 대회를 주최한다
# 참석률을 높이기 위해 댓글 이벤트를 진행한다
# 댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는다
# 추첨 프로그램을 작성해라

# 조건1 : 편의상 댓글은 20명이 작성, 아이디는 1~20이라 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 : 1
# 커피 : [2,3,4]
# -- 축하합니다 --

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)   # 순서 섞기
# print(lst)   
# print(sample(lst, 1))   # 리스트 중 1개 무작위로 뽑기

from random import *
users = range(1, 21)   # 1~20 숫자 생성
# print(type(users))   # range
users = list(users)
# print(type(users))   # list

shuffle(users)
print(users)    # 리스트 내 순서 섞기

winners = sample(users, 4)  # 4명중 1명은 치킨, 3명은 커피

print('-- 당첨자 발표 --')
print('치킨 : {0}'.format(winners[0]))
print('커피 : {0}'.format(winners[1:]))
print('-- 축하합니다 --')