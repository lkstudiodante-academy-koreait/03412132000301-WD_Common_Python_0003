import os
import sys

"""
Python 연습 문제 11
- 리스트 이동 시키기
- 1 ~ 5 까지의 값을 지니고 있는 리스트를 생성한다
- 사용자로부터 메뉴를 입력 받아 리스트를 왼쪽 or 오른쪽으로 이동 시킨다

Ex)
=====> 리스트 <=====
1, 2, 3, 4, 5

=====> 메뉴 <=====
1. 왼쪽으로 이동
2. 오른쪽으로 이동
3. 종료

선택 : 1
-----> 리스트 - 이동 후
2, 3, 4, 5, 1

선택 : 2
-----> 리스트 - 이동 후
1, 2, 3, 4, 5

선택 : 3
프로그램을 종료합니다.
"""


# Training 11
def start(args):
	MENU_MOVE_LEFT = 1
	MENU_MOVE_RIGHT = 2
	MENU_EXIT = 3
	
	oListValues = [1, 2, 3, 4, 5]
	
	print("=====> 리스트 <=====")
	print(f"{oListValues}\n")
	
	while True:
		print("=====> 메뉴 <=====")
		print("1. 왼쪽으로 이동")
		print("2. 오른쪽으로 이동")
		print("3. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 왼쪽으로 이동 일 경우
		if nMenu == MENU_MOVE_LEFT:
			nVal = oListValues[0]
			del oListValues[0]
			
			oListValues.append(nVal)
		
		else:
			nVal = oListValues[len(oListValues) - 1]
			del oListValues[len(oListValues) - 1]
			
			oListValues.insert(0, nVal)
		
		print("\n-----> 리스트 - 이동 후")
		print(f"{oListValues}\n")
		
	print("프로그램을 종료합니다.")
	