# 모듈
# import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 간 값
# theater_module.price_morning(4)  # 4명이서 조조할인 영화 보러 간 값
# theater_module.price_soldier(5)  # 5명이서 군인할인 영화 보러 간 값

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5)  못씀

# from theater_module import price_soldier as price  # 이름 재정의 가능
# price(5)


# 패키지
# import travel.thailand  # 클래스나 함수는 import문에 쓸 수 없음
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage  # from 문에서는 import뒤에 함수나 클래스 불러오기 가능
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import *
# trip_to = vietnam.VietnamPackage()  # __init__.py에다가 vietnam만 선언
# trip_to.detail()

# import inspect  # 패키지, 모듈 위치 찾아줌
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))  # c:\Users\LG\Documents\nadocoding_python\nadocoding_python_basic\travel\thailand.py


# pypi 사이트에서 'BeautifulSoup'을 찾아서 'pip install beautifulsoup4' 명령어 실행 후
## 'pip list' : 설치된 패키지 리스트 출력
## 'pip show 패키지명' : 패키지 설명
## 'pip install --upgrade 패키지명' : 업그레이드 버전 설치
## 'pip uninstall 패키지명' : 패키지 삭제
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 내장 함수
## input() : 사용자 입력을 받는 함수
lang = input('무슨 언어를 좋아하는지?')
print('{0}은 아주 좋은 언어'.format(lang))

## dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지는지 표시
# print(dir())
# import random  # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))  # random 모듈 내에서 사용 가능한 함수 등을 다 보여줌
# lst = [1, 2, 3]
# print(dir(lst))

name = 'kim'
print(dir(name))

## google에 'list of python builtins' 검색하면 내장 함수 검색 가능

# 외장 함수 : import를 해와야함
## google에 'list of python modules' 검색하면 외장 함수 검색 가능

## glob : 경로 내 폴더/파일 목록 조회(윈도우 dir)
import glob
print(glob.glob('*.py'))  # 확장자가 py인 모든 파일

## os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리

# folder = 'sample_dir'
# if os.path.exists(folder):
#     print('이미 존재하는 폴더')
#     os.rmdir(folder)
#     print(folder, '폴더 삭제')
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, '폴더 생성')
# print(os.listdir())


## time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
# print('오늘 날짜 : ', datetime.date.today())

## timedelta : 두 날짜 사이 간격
# today = datetime.date.today()   # 오늘 날짜
# td = datetime.timedelta(days=100)  # 100일 
# print('오늘부터 100일 후는 ', today + td)

###########################################################

# Quiz) 프로젝트 내 나만의 시그니처를 남기는 모듈을 만들어라
# 조건 : 모듈 파일명은 byme.py로 작성

# (모듈 사용 예제)
import byme
byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어짐
# 유튜브 : http://youtube.com
# 이메일 : djwls0803@gmail.com