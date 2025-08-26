import os
import sys

import random

"""
Python 연습 문제 7
- 바위/가위/보 게임 제작하기
- 사용자로부터 바위/가위/보 중 하나를 입력 받는다
- 컴퓨터는 바위/가위/보 중 하나를 랜덤하게 선택한다
- 사용자의 입력과 컴퓨터의 선택을 비교해서 결과를 계산한다
- 사용자가 승리했거나 무승부 일 경우 게임을 다시 진행한다
- 사용자가 패배했을 경우 게임을 종료하고 전적을 출력한다

Ex)
정수 (1. 바위, 2. 가위, 3. 보) 입력 : 1
결과 : 승리 (나 - 바위, 컴퓨터 - 가위)

정수 (1. 바위, 2. 가위, 3. 보) 입력 : 3
결과 : 무승부 (나 - 보, 컴퓨터 - 보)

정수 (1. 바위, 2. 가위, 3. 보) 입력 : 1
결과 : 패배 (나 - 바위, 컴퓨터 - 보)

전적 : 1 승 1 무 1 패
프로그램을 종료합니다.
"""


# Training 7
def start(args):
	SELECT_ROCK = 1
	SELECT_SCISSORS = 2
	SELECT_PAPER = 3
	
	RESULT_WIN = 1
	RESULT_DRAW = 2
	RESULT_LOSE = 3
	
	nCount_Win = 0
	nCount_Draw = 0
	
	while True:
		nSelect_My = int(input("정수 입력 (1. 바위, 2. 가위, 3. 보) : "))
		nSelect_Computer = random.randrange(0, 3) + 1
		
		nResult = 0
		
		# 무승부 일 경우
		if nSelect_My == nSelect_Computer:
			nResult = RESULT_DRAW
			
		else:
			nSelect_Next = (nSelect_My % SELECT_PAPER) + 1
			nResult = RESULT_WIN if nSelect_Next == nSelect_Computer else RESULT_LOSE
			
		oList_SelectStrings = [
			"", "바위", "가위", "보"
		]
		
		oList_ResultStrings = [
			"", "승리", "무승부", "패배"
		]
			
		oStr_MySelect = oList_SelectStrings[nSelect_My]
		oStr_ComputerSelect = oList_SelectStrings[nSelect_Computer]
		oStr_Result = oList_ResultStrings[nResult]
		
		oMsgA = f"나 - {oStr_MySelect}"
		oMsgB = f"컴퓨터 - {oStr_ComputerSelect}"
		
		print(f"결과 : {oStr_Result} ({oMsgA}, {oMsgB})\n")
		
		nCount_Win += 1 if nResult == RESULT_WIN else 0
		nCount_Draw += 1 if nResult == RESULT_DRAW else 0
		
		# 패배했을 경우
		if nResult == RESULT_LOSE:
			break
	
	print(f"전적 : {nCount_Win} 승, {nCount_Draw} 무 1 패")
	print("프로그램을 종료합니다.")
	