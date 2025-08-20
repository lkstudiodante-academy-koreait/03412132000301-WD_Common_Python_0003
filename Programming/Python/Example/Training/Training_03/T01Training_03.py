import os
import sys

"""
Python 연습 문제 3
- 세부 학점 계산하기
- 점수를 입력 받아 해당 점수에 해당하는 학점 출력한다

세부 학점 범위
- + : 7 ~ 9
- 0 : 4 ~ 6
- - : 0 ~ 3

Ex)
점수 입력 : 85
학점 : B0
"""


# Training 3
def start(args):
	nScore = int(input("점수 입력 : "))
	
	oGrade = ""
	oGrade_Detail = ""
	
	# F 학점 일 경우
	if nScore < 60:
		oGrade = "F"
		
	else:
		# A 학점 일 경우
		if nScore >= 90:
			oGrade = "A"
			
		# B 학점 일 경우
		elif nScore >= 80:
			oGrade = "B"
			
		# C 학점 일 경우
		elif nScore >= 70:
			oGrade = "C"
			
		# D 학점 일 경우
		else:
			oGrade = "D"
			
		# + 학점 일 경우
		if nScore >= 100 or nScore % 10 >= 7:
			oGrade_Detail = "+"
			
		else:
			oGrade_Detail = "-" if nScore % 10 <= 3 else "0"
			
	print(f"{oGrade}{oGrade_Detail} 학점입니다.")
	