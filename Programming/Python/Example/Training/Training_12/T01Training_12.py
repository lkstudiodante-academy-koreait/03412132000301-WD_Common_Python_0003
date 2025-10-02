import os
import sys

import random

"""
Python 연습 문제 12
- 리스트 치환 시키기
- 1 ~ 15 사이의 수 중 랜덤하게 10 개의 수로 리스트를 초기화한다
- 사용자로부터 위치 (인덱스) 를 입력받아 해당 위치를 기준으로 주변에 있는 1 자리수 수를 모두 -1 로 치환 시키기

Ex)
=====> 리스트 - 치환 전 <=====
1, 10, 5, 4, 12, 8, 6, 10, 12, 15

위치 입력 : 2

=====> 리스트 - 치환 후 <=====
1, 10, -1, -1, 12, 8, 6, 10, 12, 15
"""


# Training 12
def start(args):
	oListValues = []
	
	for i in range(0, 10):
		nVal = random.randrange(1, 16)
		oListValues.append(nVal)
		
	print("=====> 리스트 - 치환 전 <=====")
	print(oListValues)
	
	nIdx = int(input("\n위치 입력 : "))
	
	nLeft = nIdx
	nRight = nIdx
	
	while True:
		bIsValid_Left = nLeft >= 0 and len(f"{oListValues[nLeft]}") < 2
		bIsValid_Right = nRight < len(oListValues) and len(f"{oListValues[nRight]}") < 2
		
		# 치환이 불가능 할 경우
		if not bIsValid_Left and not bIsValid_Right:
			break
			
		# 치환이 가능 할 경우
		if bIsValid_Left:
			oListValues[nLeft] = -1
			nLeft -= 1
			
		# 치환이 가능 할 경우
		if bIsValid_Right:
			oListValues[nRight] = -1
			nRight += 1
	
	print("\n=====> 리스트 - 치환 후 <=====")
	print(oListValues)
	