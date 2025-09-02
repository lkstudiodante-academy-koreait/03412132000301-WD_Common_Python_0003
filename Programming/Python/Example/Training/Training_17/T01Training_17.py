import os
import sys

import random

"""
Python 연습 문제 17
- 다차원 리스트 치환 시키기
- 5 x 5 크기의 리스트를 생성 후 1 ~ 15 사이의 수 중 랜덤하게 초기화한다
- 사용자로부터 위치를 입력 받아 해당 위치를 기준으로 수직/수평에 존재하는 1 자리수
수를 모두 -1 로 치환 시킨다

Ex)
=====> 리스트 <=====
 1,  4, 10,  5
 9, 15, 12,  2
11,  8,  4, 13
15, 12, 11, 10

위치 입력 (행, 열) : 2 1

=====> 리스트 - 치환 후 <=====
 1, -1, 10,  5
 9, 15, 12,  2
11, -1, -1, 13
15, 12, 11, 10
"""


# Training 17
def start(args):
	nSize = 5
	oMatrixValues = []
	
	for i in range(0, nSize):
		oListValues = [random.randrange(1, 16) for j in range(0, nSize)]
		oMatrixValues.append(oListValues)
		
	print("=====> 리스트 <=====")
	
	for oListValues in oMatrixValues:
		for nVal in oListValues:
			print(f"{nVal:2}, ", end = "")
			
		print()
		
	oTokens = input("\n위치 입력 (행, 열) : ").split()
	
	nRow = int(oTokens[0])
	nCol = int(oTokens[1])
	
	# 수직 방향으로 치환한다
	for i in range(0, nSize):
		# 치환이 불가능 할 경우
		if oMatrixValues[i][nCol] >= 10:
			continue
			
		oMatrixValues[i][nCol] = -1
		
	# 수평 방향으로 치환한다
	for i in range(0, nSize):
		# 치환이 불가능 할 경우
		if oMatrixValues[nRow][i] >= 10:
			continue
			
		oMatrixValues[nRow][i] = -1
	
	print("\n=====> 리스트 - 치환 후 <=====")
	
	for oListValues in oMatrixValues:
		for nVal in oListValues:
			print(f"{nVal:2}, ", end = "")
		
		print()