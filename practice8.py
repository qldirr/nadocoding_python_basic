# # 클래스

# 클래스 생성
class Unit:
    def __init__(self, name, hp, speed):  # 생성자
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('지상 유닛 이동')
        print('{0} : {1} 방향으로 이동. 속도 : {2}'.format(\
            self.name, location, self.speed))

# marine1 = Unit('마린', 40, 5)
# marine2 = Unit('마린', 40, 5)
# tank = Unit('탱크', 150, 35)
# # marine3 = Unit('마린')   # 생성자에 정의된 변수만큼 정의해줘야함

# ## 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit('레이스', 80, 5)
# print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

# wraith2 = Unit('빼앗은 레이스', 80, 5)
# wraith2.cloking = True  # 외부에서 객체에 추가로 변수를 만들수 있음

# if wraith2.cloking == True:
#     print('{0}는 현재 클로킹 상태'.format(wraith2.name))


# 메서드
class AttackUnit(Unit):  # Unit 클래스를 상속 받음
    def __init__(self, name, hp, damage, speed):  # 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군 공격. 공격력 : {2}'\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print('{0} : {1} 데미지 입음'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴'.format(self.name))

# firebat1 = AttackUnit('파이어뱃', 50, 16)
# firebat1.attack('5시')
# # 공격 2번 받음
# firebat1.damaged(25)
# firebat1.damaged(25)  # 두번 공격 받아서 파괴

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아감. 속도 {2}'.format(\
            name, location, self.flying_speed))
        
class FlyableAttackUnit(AttackUnit, Flyable):  # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    # 메서드 오버라이딩
    def move(self, location):   # Unit클래스의 move()를 재정의
        print('공중 유닛 이동')
        self.fly(self.name, location)

# valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
# valkyrie.fly(valkyrie.name, '3시')



# valture = AttackUnit('벌처', 80, 10, 20)
# battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)
# valture.move('11시')
# # battlecruiser.fly(battlecruiser.name, '9시')
# battlecruiser.move('9시')

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

# def game_start():
#     print('게임 시작----')

# def game_over():
#     pass    # 이 함수는 실행도 되지 않음


###############################################
# Quiz) 주어진 코드를 활용해 부동산 프로그램을 작성해라
# (출력 예제)
# 총 3대의 매물
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    # 매물 초기화 
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
              , self.price, self.completion_year)

houses = []
house1 = House('강남', '아파트', '매매', '10억', '2010년')
house2 = House('마포', '오피스텔', '전세', '5억', '2007년')
house3 = House('송파', '빌라', '월세', '500/50', '2000년')

houses.append(house1)
houses.append(house2)
houses.append(house3)

print('총 {0}대의 매물'.format(len(houses)))
for house in houses:
    house.show_detail()