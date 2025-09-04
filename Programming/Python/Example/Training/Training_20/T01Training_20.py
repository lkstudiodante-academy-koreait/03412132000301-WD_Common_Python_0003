import os
import sys

"""
Python 연습 문제 20
- 합계/평균 계산하기 (+ 함수 활용)
- 요구 사항은 연습 문제 4 번 참고
"""


# Training 20
def start(args):
	nVal_Sum, nNumValues = getVal_InputSum()
	fVal_Average = getVal_Average(nVal_Sum, nNumValues)
	
	print(f"\n합계 : {nVal_Sum}")
	print(f"평균 : {fVal_Average}")
	

# 합계를 반환한다
def getVal_InputSum():
	nVal_Sum = 0
	nNumValues = 0
	
	while True:
		nVal = int(input(f"{nNumValues + 1} 번째 정수 입력 : "))
		
		# 반복을 종료했을 경우
		if nVal <= 0:
			break
		
		nVal_Sum += nVal
		nNumValues += 1
		
	return (nVal_Sum, nNumValues)


# 평균을 반환한다
def getVal_Average(a_nVal_Sum, a_nNumValues):
	return a_nVal_Sum / a_nNumValues
