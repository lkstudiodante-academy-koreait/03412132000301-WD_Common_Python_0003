import os
import sys

"""
Python 연습 문제 18
- 회원 관리 프로그램 제작하기
- 회원 정보는 이름, 전화 번호가 존재한다
- 사용자로부터 메뉴를 입력 받아 회원 추가, 제거, 검색 등의 결과를 처리한다
- 단, 회원 이름의 중복은 허용하지 않는다

Ex)
=====> 메뉴 <=====
1. 회원 추가
2. 회원 제거
3. 회원 검색
4. 모든 회원 출력
5. 종료

선택 : 1
이름 입력 : 회원 A
전화 번호 입력 : 1234

Case 1. 신규 회원 일 경우
회원 A 을(를) 추가했습니다.

Case 2. 동일한 이름의 회원이 존재 할 경우
회원 A 은(는) 이미 존재하는 회원입니다.

선택 : 2
이름 입력 : 회원 A

Case 1. 회원이 없을 경우
회원 A 은(는) 존재하지 않습니다.

Case 2. 회원이 존재 할 경우
회원 A 을(를) 제거했습니다.

선택 : 5
프로그램을 종료합니다.
"""


# Training 18
def start(args):
	MENU_ADD_MEMBER = 1
	MENU_REMOVE_MEMBER = 2
	MENU_SEARCH_MEMBER = 3
	MENU_PRINT_MEMBERS_ALL = 4
	MENU_EXIT = 5
	
	oDictMembers = {}
	
	while True:
		print("=====> 메뉴 <=====")
		print("1. 회원 추가")
		print("2. 회원 제거")
		print("3. 회원 검색")
		print("4. 모든 회원 출력")
		print("5. 종료")
		
		nMenu = int(input("\n선택 : "))
		
		# 종료 일 경우
		if nMenu == MENU_EXIT:
			break
			
		# 회원 추가 일 경우
		if nMenu == MENU_ADD_MEMBER:
			oName = input("이름 입력 : ")
			oPNumber = input("전화 번호 입력 : ")
			
			# 회원이 존재 할 경우
			if oName in oDictMembers:
				print(f"{oName} 은(는) 이미 존재하는 회원입니다.")
				
			else:
				oMember = (oName, oPNumber)
				oDictMembers[oName] = oMember
				
				print(f"{oName} 을(를) 추가했습니다.")
	
		# 회원 제거 일 경우
		elif nMenu == MENU_REMOVE_MEMBER:
			oName = input("이름 입력 : ")
			
			# 회원이 없을 경우
			if oName not in oDictMembers:
				print(f"{oName} 은(는) 존재하지 않습니다.")
				
			else:
				del oDictMembers[oName]
				print(f"{oName} 을(를) 제거했습니다.")
		
		# 회원 검색 일 경우
		elif nMenu == MENU_SEARCH_MEMBER:
			oName = input("이름 입력 : ")
			
			# 회원이 없을 경우
			if oName not in oDictMembers:
				print(f"{oName} 은(는) 존재하지 않습니다.")
				
			else:
				oMember = oDictMembers[oName]
				
				print("=====> 회원 정보 <=====")
				print(f"이름 : {oMember[0]}")
				print(f"전화 번호 : {oMember[1]}")
	
		# 모든 회원 출력 일 경우
		elif nMenu == MENU_PRINT_MEMBERS_ALL:
			print("=====> 모든 회원 정보 <=====")
			
			for oKey, oMember in oDictMembers.items():
				print(f"이름 : {oMember[0]}")
				print(f"전화 번호 : {oMember[1]}\n")
		
		print()
			
	print("프로그램을 종료합니다.")
