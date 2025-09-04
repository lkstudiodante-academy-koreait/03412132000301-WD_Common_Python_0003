import os
import sys

"""
Python 연습 문제 19
- 세부 학점 계산하기 (+ 함수 활용)
- 요구 사항은 연습 문제 3 번 참고
"""


# Training 19
def start(args):
	nScore = int(input("점수 입력 : "))

	oGrade = getGrade(nScore)
	oGrade_Detail = getGrade_Detail(nScore)
	
	print(f"{oGrade}{oGrade_Detail} 학점입니다.")
	

# 학점을 반환한다
def getGrade(a_nScore):
	# F 학점 일 경우
	if a_nScore < 60:
		oGrade = "F"
	
	else:
		# A 학점 일 경우
		if a_nScore >= 90:
			oGrade = "A"
		
		# B 학점 일 경우
		elif a_nScore >= 80:
			oGrade = "B"
		
		# C 학점 일 경우
		elif a_nScore >= 70:
			oGrade = "C"
		
		# D 학점 일 경우
		else:
			oGrade = "D"
		
	return oGrade
	

# 세부 학점을 반환한다
def getGrade_Detail(a_nScore):
	# F 학점 일 경우
	if a_nScore < 60:
		oGrade_Detail = ""
	
	else:
		# + 학점 일 경우
		if a_nScore >= 100 or a_nScore % 10 >= 7:
			oGrade_Detail = "+"
		
		else:
			oGrade_Detail = "-" if a_nScore % 10 <= 3 else "0"
		
	return oGrade_Detail
