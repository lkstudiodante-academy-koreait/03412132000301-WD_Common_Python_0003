import os
import sys

import random

"""
Python 연습 문제 21
- 바위/가위/보 게임 제작하기
- 요구 사항은 연습 문제 7 번 참고
"""


# Training 21
def start(args):
	nCount_Win = 0
	nCount_Draw = 0
	
	while True:
		nSelect_My = int(input("정수 입력 (1. 바위, 2. 가위, 3. 보) : "))
		nSelect_Computer = random.randrange(0, 3) + 1
		
		nResult = getResult(nSelect_My, nSelect_Computer)
		oStr_Result = getStr_Result(nResult)
		
		oStr_MySelect = getStr_Select(nSelect_My)
		oStr_ComputerSelect = getStr_Select(nSelect_Computer)
		
		oMsgA = f"나 - {oStr_MySelect}"
		oMsgB = f"컴퓨터 - {oStr_ComputerSelect}"
		
		print(f"결과 : {oStr_Result} ({oMsgA}, {oMsgB})\n")
		
		nCount_Win += 1 if nResult == RESULT_WIN else 0
		nCount_Draw += 1 if nResult == RESULT_DRAW else 0
		
		# 패배 일 경우
		if nResult == RESULT_LOSE:
			break
			
	print(f"전적 : {nCount_Win} 승 {nCount_Draw} 무 1 패")
	print("프로그램을 종료합니다.")
		

# 선택
SELECT_ROCK = 1
SELECT_SCISSORS = 2
SELECT_PAPER = 3

# 결과
RESULT_WIN = 1
RESULT_DRAW = 2
RESULT_LOSE = 3

# 결과를 반환한다
def getResult(a_nSelect_My, a_nSelect_Computer):
	# 무승부 일 경우
	if a_nSelect_My == a_nSelect_Computer:
		return RESULT_DRAW
	
	nSelect_Next = (a_nSelect_My % SELECT_PAPER) + 1
	return RESULT_WIN if nSelect_Next == a_nSelect_Computer else RESULT_LOSE


# 선택 문자열을 반환한다
def getStr_Select(a_nSelect):
	oListStrings = [
		"", "바위", "가위", "보"
	]
	
	return oListStrings[a_nSelect]


# 결과 문자열을 반환한다
def getStr_Result(a_nResult):
	oListStrings = [
		"", "승리", "무승부", "패배"
	]
	
	return oListStrings[a_nResult]
