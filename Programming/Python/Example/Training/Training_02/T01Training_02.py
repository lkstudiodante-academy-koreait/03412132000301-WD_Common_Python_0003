import os
import sys

"""
Python 연습 문제 2
- 학점 계산하기
- 사용자로부터 점수 3 개를 입력 받아 가장 높은 점수에 대한 학점을 계산하기

Ex)
점수 (3 개) 입력 : 65 70 85
B 학점입니다.
"""


# Training 2
def start(args):
	oTokens = input("점수 (3 개) 입력 : ").split()
	
	nScoreA = int(oTokens[0])
	nScoreB = int(oTokens[1])
	nScoreC = int(oTokens[2])
	
	nScore_High = nScoreA if nScoreA >= nScoreB else nScoreB
	nScore_High = nScore_High if nScore_High >= nScoreC else nScoreC
	
	if nScore_High < 60:
		print("F 학점입니다.")

	else:
		if nScore_High >= 90:
			print("A 학점입니다.")
		
		elif nScore_High >= 80:
			print("B 학점입니다.")
		
		elif nScore_High >= 70:
			print("C 학점입니다.")
		
		else:
			print("D 학점입니다.")
			