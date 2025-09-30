import os
import sys

from pyasn1_modules.rfc6960 import ocspResponseMap

from Training.Training_29.CException_Missing import CException_Missing
from Training.Training_29.CException_Duplicate import CException_Duplicate

from Training.Training_34.CTable_Member import CTable_Member


# Training 34
def start(args):
	oPath_DB = "P_T01Training_34_01.db"
	CTable_Member.getInst().connect(oPath_DB)
	
	while True:
		printMenu()
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		try:
			# 회원 추가 일 경우
			if nMenu == MENU_ADD_MEMBER:
				addMember()
		
			# 회원 제거 일 경우
			elif nMenu == MENU_REMOVE_MEMBER:
				removeMember()
		
			# 회원 검색 일 경우
			elif nMenu == MENU_SEARCH_MEMBER:
				searchMember()
		
			# 모든 회원 출력 일 경우
			elif nMenu == MENU_PRINT_MEMBERS_ALL:
				printMembers_All()
	
		except Exception as oException:
			print(oException)
	
		print()
		
	print("프로그램을 종료합니다.")
	

# 메뉴
MENU_ADD_MEMBER = 1
MENU_REMOVE_MEMBER = 2
MENU_SEARCH_MEMBER = 3
MENU_PRINT_MEMBERS_ALL = 4
MENU_EXIT = 5

# 메뉴를 출력한다
def printMenu():
	print("=====> 메뉴 <=====")
	print("1. 회원 추가")
	print("2. 회원 제거")
	print("3. 회원 검색")
	print("4. 모든 회원 출력")
	print("5. 종료")
	
	
# 회원을 추가한다
def addMember():
	oName = input("이름 입력 : ")
	oPNumber = input("전화 번호 입력 : ")
	
	oResult = CTable_Member.getInst().findMember(oName)
	
	# 회원이 존재 할 경우
	if oResult != None:
		raise CException_Duplicate(oName)
	
	CTable_Member.getInst().addMember(oName, oPNumber)
	print(f"{oName} 을(를) 추가했습니다.")
	

# 회원을 제거한다
def removeMember():
	oName = input("이름 입력 : ")
	oResult = CTable_Member.getInst().findMember(oName)
	
	# 회원이 없을 경우
	if oResult == None:
		raise CException_Missing(oName)
	
	CTable_Member.getInst().removeMember(oName)
	print(f"{oName} 을(를) 제거했습니다.")


# 회원을 검색한다
def searchMember():
	oName = input("이름 입력 : ")
	oResult = CTable_Member.getInst().findMember(oName)
	
	# 회원이 없을 경우
	if oResult == None:
		raise CException_Missing(oName)
	
	print("=====> 회원 정보 <=====")
	print(f"이름 : {oResult[0]}")
	print(f"전화 번호 : {oResult[1]}")


# 모든 회원을 출력한다
def printMembers_All():
	print("=====> 모든 회원 정보 <=====")
	
	for oResult in CTable_Member.getInst().getMembers_All():
		print(f"이름 : {oResult[0]}")
		print(f"전화 번호 : {oResult[1]}\n")
