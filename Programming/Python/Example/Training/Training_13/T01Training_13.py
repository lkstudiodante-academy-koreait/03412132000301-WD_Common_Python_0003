import os
import sys

"""
Python 연습 문제 13
- 문자열 중복 검사하기
- 사용자로부터 문자열을 입력 받아 해당 문자열을 구성하는 문자 중 중복되는 문자가
있는 검사하는 프로그램 제작하기 (+ 단, 대/소문자 구문 X)

Ex)
문자열 입력 : String
중복 여부 : False

문자열 입력 : Level
중복 여부 : True
"""


# Training 13
def start(args):
	oStr = input("문자열 입력 : ")
	bIsDuplicate = False
	
	for i in range(0, len(oStr)):
		for j in range(i + 1, len(oStr)):
			oLetterA = oStr[i].lower()
			oLetterB = oStr[j].lower()
			
			# 문자가 중복 될 경우
			if oLetterA == oLetterB:
				bIsDuplicate = True
				
	print(f"중복 여부 : {bIsDuplicate}")
	
	# Case 1. Set 컬렉션 활용
	# oSetLetters = set()
	#
	# for oLetter in oStr:
	# 	oSetLetters.add(oLetter.lower())
	#
	# bIsDuplicate = len(oStr) != len(oSetLetters)
	# print(f"중복 여부 : {bIsDuplicate}")
	