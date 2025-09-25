import os
import sys

from Training.Training_26.CFactory_Unit import CFactory_Unit
from Training.Training_30.CException_Lack import CException_Lack

"""
Python 연습 문제 30
- 유닛 생산 프로그램 제작하기 (+ 예외 처리 활용)
- 요구 사항은 연습 문제 26 번 참고
"""


# Training 30
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
			
			try:
				# 비용이 부족 할 경우
				if nAmount < oCls_Unit.COST:
					raise CException_Lack()
			
				oUnit = CFactory_Unit.getInst().createUnit(nMenu - 1)
				oListUnits.append(oUnit)
				
				nAmount -= oCls_Unit.COST
				print(f"{oUnit.NAME} 을(를) 생산했습니다.")
		
			except Exception as oException:
				print(oException)
		
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
	
