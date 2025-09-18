import os
import sys

import random

from Training.Training_27.CShape import CLine, CTriangle, CRectangle
from Training.Training_27.CCanvas import CCanvas

"""
Python 연습 문제 27
- 콘솔 그림판 제작하기
- 도형은 선, 삼각형, 사각형 이 존재한다
- 도형은 색상 정보를 지니고 있다 (+ Ex. 빨간색, 녹색, 파란색 등등...)
- 사용자로부터 메뉴를 입력 받아 도형을 추가 후 그리는 그림판 제작하기

Ex)
=====> 메뉴 <=====
1. 선 추가
2. 삼각형 추가
3. 사각형 추가
4. 모든 도형 그리기
5. 종료

선택 : 1
녹색 선 을(를) 추가했습니다.

선택 : 2
빨간색 삼각형 을(를) 추가했습니다.

선택 : 4
녹색 선을 그렸습니다.
빨간색 선을 그렸습니다.

선택 : 5
프로그램을 종료합니다.
"""


# Training 27
def start(args):
	oCanvas = CCanvas()
	
	while True:
		printMenu()
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 모든 도형 그리기 일 경우
		if nMenu == MENU_DRAW_SHAPES_ALL:
			oCanvas.drawShapes_All()
			
		else:
			oShape = createShape(nMenu)
			oCanvas.addShape(oShape)
			
			oStr_Color = oShape.getStr_Color()
			oStr_Shape = oShape.getStr_Shape()
			
			print(f"{oStr_Color} {oStr_Shape} 을(를) 추가했습니다.")
			
		print()
		
	print("프로그램을 종료합니다.")
	
	
# 색상
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_BLUE = 3

# 메뉴
MENU_ADD_LINE = 1
MENU_ADD_TRIANGLE = 2
MENU_ADD_RECTANGLE = 3
MENU_DRAW_SHAPES_ALL = 4
MENU_EXIT = 5

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 선 추가")
	print("2. 삼각형 추가")
	print("3. 사각형 추가")
	print("4. 모든 도형 그리기")
	print("5. 종료")
	

# 도형을 생성한다
def createShape(a_nMenu):
	nColor = random.randrange(COLOR_RED, COLOR_BLUE + 1)
	
	# 선 일 경우
	if a_nMenu == MENU_ADD_LINE:
		return CLine(nColor)
	
	# 삼각형 일 경우
	elif a_nMenu == MENU_ADD_TRIANGLE:
		return CTriangle(nColor)
	
	# 사각형 일 경우
	elif a_nMenu == MENU_ADD_RECTANGLE:
		return CRectangle(nColor)
	
	return None