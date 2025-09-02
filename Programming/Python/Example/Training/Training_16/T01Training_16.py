import os
import sys

"""
Python 연습 문제 16
- 다차원 리스트 이동 시키기
- 3 x 3 크기의 리스트를 생성 및 1 부터 차례대로 초기화한다
- 사용자로부터 메뉴를 입력받아 리스트를 상/하/좌/우 로 이동시킨다

Ex)
=====> 리스트 <=====
1, 2, 3
4, 5, 6
7, 8, 9

=====> 메뉴 <=====
1. 위로 이동
2. 아래로 이동
3. 왼쪽으로 이동
4. 오른쪽으로 이동
5. 종료

선택 : 1
-----> 리스트 - 이동 후
4, 5, 6
7, 8, 9
1, 2, 3

선택 : 3
-----> 리스트 - 이동 후
5, 6, 4
8, 9, 7
2, 3, 1

선택 : 5
프로그램을 종료합니다.
"""


# Training 16
def start(args):
	MENU_MOVE_UP = 1
	MENU_MOVE_DOWN = 2
	MENU_MOVE_LEFT = 3
	MENU_MOVE_RIGHT = 4
	MENU_EXIT = 5
	
	oMatrixValues = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	
	print("=====> 리스트 <=====")
	
	for oList in oMatrixValues:
		print(oList)
		
	print()
		
	while True:
		print("=====> 메뉴 <=====")
		print("1. 위로 이동")
		print("2. 아래로 이동")
		print("3. 왼쪽으로 이동")
		print("4. 오른쪽으로 이동")
		print("5. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 위로 이동 일 경우
		if nMenu == MENU_MOVE_UP:
			oList = oMatrixValues.pop(0)
			oMatrixValues.append(oList)
	
		# 아래로 이동 일 경우
		elif nMenu == MENU_MOVE_DOWN:
			oList = oMatrixValues.pop()
			oMatrixValues.insert(0, oList)
	
		# 왼쪽으로 이동 일 경우
		elif nMenu == MENU_MOVE_LEFT:
			for oList in oMatrixValues:
				nVal = oList.pop(0)
				oList.append(nVal)
	
		# 오른쪽으로 이동 일 경우
		elif nMenu == MENU_MOVE_RIGHT:
			for oList in oMatrixValues:
				nVal = oList.pop()
				oList.insert(0, nVal)
	
		print("-----> 리스트 - 이동 후")
		
		for oList in oMatrixValues:
			print(oList)
			
		print()
			
	print("프로그램을 종료합니다.")
	