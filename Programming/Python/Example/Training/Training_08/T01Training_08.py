import os
import sys

"""
Python 연습 문제 8
- 피보나치 수열 출력하기
- 사용자로부터 숫자를 입력받아 해당 숫자에 해당하는 피보나치 수열 출력하기

Ex)
정수 입력 : 7
0, 1, 1, 2, 3, 5, 8, 13, 21
"""


# Training 8
def start(args):
	nVal = int(input("정수 입력 : "))
	
	nVal_Cur = 1
	nVal_Prev = 0
	
	print(f"{nVal_Prev}, {nVal_Cur}, ", end = "")
	
	for i in range(0, nVal):
		nVal_Next = nVal_Prev + nVal_Cur
		print(f"{nVal_Next}, ", end = "")
		
		nVal_Prev = nVal_Cur
		nVal_Cur = nVal_Next
		
	print()
	