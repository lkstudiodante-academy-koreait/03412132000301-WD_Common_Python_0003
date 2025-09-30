import os
import sys

from datetime import datetime

from Training.Training_33.CUnit import CUnit
from Training.Training_33.CTable_UnitInfo import CTable_UnitInfo

"""
Python 연습 문제 33
- 유닛 생산 시뮬레이션 구현하기 (+ 파일 시스템 활용)
- 요구 사항은 연습 문제 26 번 참고
"""


# Training 33
def start(args):
	oPath_UnitInfo = "P_T01Training_33_01.txt"
	CTable_UnitInfo.getInst().loadInfos_Unit_FromFile(oPath_UnitInfo)
	
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
			nIdx = nMenu - 1
			oInfo_Unit = CTable_UnitInfo.getInst().getInfo_Unit(nIdx)
			
			# 비용이 부족 할 경우
			if nAmount < oInfo_Unit.m_nCost:
				print("비용이 부족합니다.")
			
			else:
				oUnit = CUnit(oInfo_Unit, datetime.now())
				oListUnits.append(oUnit)
				
				nAmount -= oInfo_Unit.m_nCost
				print(f"{oInfo_Unit.m_oName} 을(를) 생산했습니다.")
		
		print()
	
	print("프로그램을 종료합니다.")


# 메뉴
MENU_PRINT_UNITS_ALL = 0
MENU_EXIT = 0

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	nNumInfos_Unit = CTable_UnitInfo.getInst().getNumInfos_Unit()
	
	for i in range(0, nNumInfos_Unit):
		oInfo_Unit = CTable_UnitInfo.getInst().getInfo_Unit(i)
		nCost = oInfo_Unit.m_nCost
		oName = oInfo_Unit.m_oName
		
		print(f"{i + 1}. {oName} 생산 (비용 : {nCost})")
	
	global MENU_PRINT_UNITS_ALL
	global MENU_EXIT
	
	MENU_PRINT_UNITS_ALL = nNumInfos_Unit + 1
	MENU_EXIT = nNumInfos_Unit + 2
	
	print(f"{MENU_PRINT_UNITS_ALL}. 모든 유닛 출력")
	print(f"{MENU_EXIT}. 종료")


# 모든 유닛을 출력한다
def printUnits_All(a_oListUnits):
	print("=====> 모든 유닛 정보 <=====")
	
	for oUnit in a_oListUnits:
		oUnit.showInfo()
		