# 함수
# def open_account():
#     print('새 계좌 생성')

# open_account()

# 전달값, 반환값
def deposit(balance, money):
    print('입금 완료, 잔액은 {0}원'.format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:   # 잔액이 출금보다 많으면
        print('출금 완료, 잔액 {0}원'.format(balance - money))
        return balance - money
    else:
        print('출금 불가, 잔액 {0}원'.format(balance))
        return balance
    
def withdraw_night(balance, money):   # 저녁에 출금
    commission = 100   # 수수료
    return commission, balance - money - commission   # 튜플 형식으로 반환

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)   # 입금을 1000원을 하고 2000원을 출금하려고 하니 출금 불가
commission, balance = withdraw_night(balance, 500)
print('수수료 {0}원, 잔액 {1}원'.format(commission, balance))   # 100, 400


# 기본값
# def profile(name, age, main_lang):
#     print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}' \
#           .format(name, age, main_lang))

# profile('tom', 20, 'python')
# profile('mike', 25, 'java')

## 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang='python'):
    print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}' \
          .format(name, age, main_lang))

profile('tom')
profile('mike')


# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name='mike', main_lang='python', age=23)   # 키워드를 지정해주면 순서가 뒤바뀌어있어도 함수를 선언한 순서대로 출력
profile(main_lang='java', name='tom', age=20)


# 가변 인자
# def profile(name, age, leng1, leng2, leng3, leng4, leng5):   # 언어를 5개까지만 쓸 수 있음 
#     print('이름 : {0}\t나이 : {1}'.format(name, age), end=" ")   # 문장이 끝나도 줄바꿈이 되지 않음
#     print(leng1, leng2, leng3, leng4, leng5)

def profile(name, age, *language):    # 언어를 몇 개를 써도 상관없음, 서로 다른 개수의 값을 넣을 수 있음
    print('이름 : {0}\t나이 : {1}'.format(name, age), end=" ")   # 문장이 끝나도 줄바꿈이 되지 않음
    for lang in language:
        print(lang, end=' ')
    print()

profile('tom', 20, 'java', 'python', 'C', 'C++', 'C#', 'javascript')
profile('andy', 25, 'kotlin', 'swift')


# 지역 변수, 전역 변수
gun = 10

def checkpoint(soldiers):   # 경계근무
    # gun = 20   # 지역 변수
    global gun  # 전역 공간에 있는 gun 사용, 10
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))   

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))  
    return gun 

print('전체 총 : {0}'.format(gun))
# checkpoint(2)   # 2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)   # gun = 8
print('남은 총 : {0}'.format(gun))   

##############################################
# Quiz) 표준 체중을 구하는 프로그램을 작성해라
# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남 : 키(m) X 키(m) X 22
# 여 : 키(m) X 키(m) X 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다

def std_weight(height, gender):   # 키는 m 단위(실수), 성별은 '남자' or '여자'
    if gender == '남자':
        return height * height * 22
    else:
        return height * height *21

height = 175
gender = '남자'    
weight = round(std_weight(height / 100, gender), 2)   # 소수점 둘째자리까지
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다'.format(height, gender, weight))