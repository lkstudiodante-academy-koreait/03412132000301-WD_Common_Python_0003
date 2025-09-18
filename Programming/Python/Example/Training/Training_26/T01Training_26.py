import os
import sys

from Training.Training_26.CFactory_Unit import CFactory_Unit

"""
Python 연습 문제 26
- 유닛 생산 프로그램 제작하기
- 사용자로부터 초기 소지 금액을 입력 받는다
- 사용자가 입력 한 메뉴에 따라 서로 다른 금액의 유닛을 생산한다
- 단, 소지 금액이 부족하면 생산 불가

Ex)
초기 금액 입력 : 1000

=====> 메뉴 <=====
1. 유닛 A 생산 (비용 : 250)
2. 유닛 B 생산 (비용 : 500)
3. 유닛 C 생산 (비용 : 750)
4. 생산 된 모든 유닛 출력
5. 종료

선택 (소지 금액 : 1000) : 1
유닛 A 을(를) 생산했습니다.

선택 (소지 금액 : 750) : 4
유닛 A 을(를) {날짜} 에 생산했습니다.

선택 (소지 금액 : 750) : 5
프로그램을 종료합니다.
"""


# Training 26
def start(args):
	nAmount = int(input("초기 금액 입력 : "))
	oListUnits = []
	
	print()
	
	while True:
		printMenu()
		nMenu = int(input(f"\n선택 (소지 금액 : {nAmount}) : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 모든 유닛 출력 일 경우
		if nMenu == MENU_PRINT_UNITS_ALL:
			printUnits_All(oListUnits)
		
		else:
			oCls_Unit = CFactory_Unit.getInst().getCls_Unit(nMenu - 1)
			
			# 비용이 부족 할 경우
			if nAmount < oCls_Unit.COST:
				print("비용이 부족합니다.")
				
			else:
				oUnit = CFactory_Unit.getInst().createUnit(nMenu - 1)
				oListUnits.append(oUnit)
				
				nAmount -= oCls_Unit.COST
				print(f"{oUnit.NAME} 을(를) 생산했습니다.")
		
		print()
		
	print("프로그램을 종료합니다.")


# 메뉴
MENU_PRINT_UNITS_ALL = 0
MENU_EXIT = 0

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	oListClasses_Unit = CFactory_Unit.getInst().m_oListClasses_Unit
	
	for i in range(0, len(oListClasses_Unit)):
		nCost = oListClasses_Unit[i].COST
		oName = oListClasses_Unit[i].NAME
		
		print(f"{i + 1}. {oName} 생산 (비용 : {nCost})")
		
	global MENU_PRINT_UNITS_ALL
	global MENU_EXIT
	
	MENU_PRINT_UNITS_ALL = len(oListClasses_Unit) + 1
	MENU_EXIT = len(oListClasses_Unit) + 2
	
	print(f"{MENU_PRINT_UNITS_ALL}. 모든 유닛 출력")
	print(f"{MENU_EXIT}. 종료")
	
	
# 모든 유닛을 출력한다
def printUnits_All(a_oListUnits):
	print("=====> 모든 유닛 정보 <=====")
	
	for oUnit in a_oListUnits:
		oUnit.showInfo()
		