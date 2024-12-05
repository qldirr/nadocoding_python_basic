# if문
# weather = input('오늘 날씨 어때요?? :')
# if weather == 'rain' or weather == 'snow':
#     print('우산을 챙기기')
# elif weather == 'dust':
#     print('마스크 챙기기')
# else:
#     print('준비물 필요 없음')


temp = int(input('기온은 어때요?'))
if 30 <= temp:
    print('너무 더움')
elif 10 <= temp and temp < 30:
    print('괜찮은 날씨')
elif 0 <= temp < 10:
    print('외투 챙기기')
else:
    print('너무 추움')
    


# for문
# for waiting_num in range(1, 6):   # 1~5
#     print('대기 번호 : {0}'.format(waiting_num))

starbucks = ['아이언맨', '토르', '그루트']
for customer in starbucks:
    print('{0}, 커피가 준비되었습니다'.format(customer))


# while문
# customer = '토르'
# index = 5
# while index >= 1:
#     print('{0}, 커피가 준비되었습니다. {1}번 남았습니다.'.format(customer, index))
#     index -= 1
#     if index == 0:
#         print('커피는 폐기 처분')

# customer = '아이언맨'
# index = 1
# while True:
#     print('{0}, 커피가 준비되었습니다. 호출 {1}회'.format(customer, index))
#     index += 1   # 무한 루프

customer = '토르'
person = 'Unknown'

while person != customer:
    print('{0}, 커피가 준비되었습니다.'.format(customer))
    person = input('이름이 어떻게 되세요? ')   # 입력된 이름이 '토르'일 경우에 while문 종료


# continue 와 break
absent = [2,5]  # 결석
no_book = [7]   # 책을 안가져옴
for student in range(1, 11):   # 1~10
    if student in absent:   # 결석한 사람이면
        continue    # 다음 반복으로 넘어감
    elif student in no_book:
        print('오늘 수업 여기까지. {0}는 교무실로'.format(student))   # 책을 안가져왔다면
        break     # 반복문 탈출
    print('{0}, 책을 읽어봐'.format(student))    # 2, 5 제외하고 반복문 실행


# 한 줄 for
## 출석 번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

## 학생 이름을 길이로 변환
students = ['iron man', 'thor', 'groot']
students = [len(i) for i in students]
print(students)    # [8, 4, 5]

## 학생 이름을 대문자로 변환
students = ['iron man', 'thor', 'groot']
students = [i.upper() for i in students]


############################################################
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사이다
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성해라

# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수
# 조건2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭 해야 함

# (출력문 예제)
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2명

from random import *
cnt = 0   # 총 탑승 승객 수
for i in range(1, 51):    # 1~50 (승객), range() : 순차적 숫자 생성
    time = randrange(5, 51)   # 5~50 분 소요 시간, randrange() : 랜덤 숫자 생성
    if 5 <= time <= 15:   # 5~15 분 이내 손님, 탑승 승객 수 증가
        print('[o] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))
        cnt += 1
    else:   # 매칭 실패
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i, time))

print('총 탑승 승객 : {0}명'.format(cnt))