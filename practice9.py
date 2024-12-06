# 예외 처리
# try:
#     print('나누기 전용 계산기')
#     nums = []
#     nums.append(int(input('첫번째 숫자 : ')))
#     nums.append(int(input('두번째 숫자 : ')))
#     nums.append(int(nums[0] / nums[1]))
#     print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print('에러 : 잘못된 값 입력')  # 숫자가 아닌 문자 입력 시
# except ZeroDivisionError as err:
#     print(err)   # 0으로 나눌때 발생
# except Exception as err:
#     print('알수없는 에러 발생')
#     print(err)

# 에러 발생시키기
try:
    print('한자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫번째 숫자 : '))
    num2 = int(input('두번째 숫자 : '))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError
        raise BigNumberError('입력값:{0}, {1}'.format(num1, num2))
    print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
except ValueError:
    print('잘못된 값 입력. 한자리 숫자만 입력하세요')
except BigNumberError as err:
    print('에러 발생. 한자리 숫자만 입력하세요')
    print(err)
finally:   # 에러가 발생하던 말던 무조건 실행되는 부분
    print('계산기를 이용해 주셔서 감사합니다')


# 사용자 정의 예외 처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    

######################################################
# Quiz) 대기 손님이 있는 치킨집이 있다
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였다
# 시스템 코드를 확인하고 적절한 예외 처리 구문을 넣어라

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 처리
#         출력 메세지 - '잘못된 값을 입력'
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldoutError]발생시키고 프로그램 종료
#         출력 메세지 - '재고가 소진되어 더 이상 주문을 받지 않음'

# [코드]
class SoldoutError(Exception):
    pass

chicken = 10
waiting = 1 # 홀 안에는 만석, 대기번호 1부터 시작
while(True):
     try:
        print('[남은 치킨: {0}]'.format(chicken))
        order = int(input('치킨 몇마리 주문??'))
        if order > chicken:   # 남은 치킨보다 주문량이 많을때
            print('재고 부족')
        elif order <= 0:
            raise ValueError
        else:
            print('[대기 번호 {0}] {1}마리 주문 완료'.format(\
                waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldoutError
     except ValueError:
        print('잘못된 값을 입력')
     except SoldoutError:
        print('재고가 소진되어 더 이상 주문을 받지 않음')
        break
     

