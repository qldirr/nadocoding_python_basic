# 표준 입출력
print('Python', 'Java', sep=",")  # 중간에 뭘 넣을지 설정 가능
print('Python', 'Java', 'Javascript', sep=" VS ")  # 중간에 뭘 넣을지 설정 가능

print('Python', 'Java', sep=",", end="?")  # 끝에 뭘 넣을지도 설정 가능
print('무엇이 더 재미있을까')   # 이 문장 뒤에도 '?'가 붙음

# import sys
# print('Python', 'Java', file=sys.stdout)   # 표준 출력
# print('Python', 'Java', file=sys.stderr)   # 표준 에러

## 시험 성적
scores = {'math':0, 'english':50, 'coding':100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=':')   # 8칸 공간 만들고 왼쪽 정렬, 4칸 공간 만들고 오른쪽 정렬


## 은행 대기 순번표
## 001, 002, 003..... 020
for number in range(1, 21):
    print('대기번호 : ' + str(number).zfill(3))  # 세글자로 만들어주는데 값이 없으면 0으로 채워라


## 표준 입력
answer = input('아무값이나 입력 : ')  # 입력한 값은 항상 문자열
print('입력한 값은 : ' + answer + '입니다')


# 다양한 출력 포맷
## 빈자리는 빈공간으로 두고 오른쪽 정렬을 하고 총 10자리 공간 확보
print('{0: >10}'.format(500))   # 500이 출력되는데 10자리 차지하면서 오른쪽 정렬
## 양수일때 '+', 음수일때 '-'
print('{0: >+10}'.format(500))   # +500이 출력되는데 10자리 차지하면서 오른쪽 정렬
print('{0: >-10}'.format(500))   # -500이 출력되는데 10자리 차지하면서 오른쪽 정렬
## 왼쪽 정렬, 빈칸을 _로 채우기
print('{0:_<+10}'.format(500))   # +500이 출력되는데 10자리 차지하면서 왼쪽 정렬이고 빈칸에는 _표시, +500______
## 세자리마다 ',' 찍기
print('{0:,}'.format(1000000000))
## 세자리마다 ',' 찍기, +- 부호 붙이기
print('{0:+,}'.format(1000000000))
print('{0:+,}'.format(-1000000000))
## 세자리마다 ',' 찍기, +- 부호 붙이기, 자리수도 확보, 빈자리는 ^ 로 채우기
print('{0:^<+30,}'.format(10000000000000))   # +10,000,000,000,000^^^^^^^^^^^
# 소수점 출력
print('{0:f}'.format(5/3))   # 1.66667
# 소수점 특정 자리까지 표시
print('{0:.2f}'.format(5/3))   # 1.67


# 파일 입출력
# score_file = open('score.txt', 'w', encoding='utf8')   내용 쓰기
# print('math : 0', file=score_file)
# print('english : 50', file=score_file) 
# score_file.close()  # 이 코드를 실행하면 'score.txt'파일이 생성되면서 위에서 적은 내용이 들어감

# score_file = open('score.txt', 'a', encoding='utf8')  # 내용을 더 추가
# score_file.write('science : 80')
# score_file.write('\ncoding : 100')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')  # 내용을 읽어오기
# print(score_file.read())
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline(), end='')  # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end='')  # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end='')  # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end='')  # 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line: break
#     print(line)
# score_file.close()   # 위랑 결과는 똑같은데 파일 내 몇줄이 있는지 모를때는 for문 사용해서 출력 가능

# score_file = open('score.txt', 'r', encoding='utf8')
# lines = score_file.readlines()   # 모든 line을 가져와서 list형태로 저장
# for line in lines:
#     print(line, end='')
# score_file.close()


# pickle
import pickle
# profile_file = open('prfile.pickle', 'wb')
# profile = {'name':'park', 'age':30, 'hobby':['golf', 'coding', 'soccer']}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open('prfile.pickle', 'rb')
# profile = pickle.load(profile_file)   # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# with
with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))   

with open('study.txt', 'w', encoding='utf8') as study_file:
    study_file.write('파이썬 공부 중')   # 파일에 내용 쓰기

with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())   # 파일 내용 읽기

#############################################################
# Quiz) 회사에서 매주 1회 작성해야하는 보고서가 있다
# 보고서는 아래의 양식에 맞춰야 한다

# - X 주차 주간보고-
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차~50주차까지 보고서 파일을 만드는 프로그램을 작성해라

# 조건 : 파일명은 '1주차.txt'와 같은 형태
# for i in range(1, 51):
#     with open(str(i) + '주차.txt', 'w', encoding='utf8') as report_file:
#         report_file.write('- {0} 주차 주간보고-'.format(i))
#         report_file.write('\n부서 :')
#         report_file.write('\n이름 :')
#         report_file.write('\n업무 요약 :')