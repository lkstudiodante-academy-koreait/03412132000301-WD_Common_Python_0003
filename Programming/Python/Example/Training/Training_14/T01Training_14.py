import os
import sys

import random

"""
Python 연습 문제 14
- 숫자 야구 게임 제작하기
- 1 ~ 9 사이의 수 중 램덤하게 중복 되지 않는 4 개의 수를 추출한다
- 사용자로부터 4 개의 수를 입력 받아 스트라이크 or 볼 여부를 판정한다
- 입력 받은 수가 정답에 존재하고 위치가 동일하다면 스트라이크
- 입력 받은 수가 정답에 존재하지만 위치가 다르다면 볼
- 4 스트라이크가 되면 게임을 종료한다

Ex)
정답 : 1 4 9 2

정수 (4 개) 입력 : 1 9 4 2
결과 : 2 Strike, 2 Ball

정수 (4 ㅐ) 입력 : 1 4 9 2
결과 : 4 Strike, 0 Ball

프로그램을 종료합니다.
"""


# Training 14
def start(args):
	oAnswer = []
	
	while len(oAnswer) < 4:
		nVal = random.randrange(1, 10)
		
		# 중복 되지 않을 경우
		if nVal not in oAnswer:
			oAnswer.append(nVal)
	
	# Case 1. Set 컬렉션 활용
	# oSetValues = set()
	#
	# while len(oSetValues) < 4:
	# 	nVal = random.randrange(1, 10)
	# 	oSetValues.add(nVal)
	#
	# oAnswer = list(oSetValues)
	
	print(f"정답 : {oAnswer}\n")
	
	while True:
		oTokens = input("정수 (4 개) 입력 : ").split()
		oListValues = list(map(int, oTokens))
		
		nCount_Strike = 0
		nCount_Ball = 0
		
		for i in range(0, len(oAnswer)):
			# 숫자가 없을 경우
			if oAnswer[i] not in oListValues:
				continue
				
			nIdx = oListValues.index(oAnswer[i])
		
			nCount_Strike += 1 if i == nIdx else 0
			nCount_Ball += 1 if i != nIdx else 0
			
			# for j in range(0, len(oListValues)):
			# 	# 숫자가 다를 경우
			# 	if oAnswer[i] != oListValues[j]:
			# 		continue
			#
			# 	nCount_Strike += 1 if i == j else 0
			# 	nCount_Ball += 1 if i != j else 0
				
		print(f"결과 : {nCount_Strike} Strike, {nCount_Ball} Ball\n")
		
		# 4 Strike 일 경우
		if nCount_Strike >= 4:
			break
			
	print("프로그램을 종료합니다.")
	