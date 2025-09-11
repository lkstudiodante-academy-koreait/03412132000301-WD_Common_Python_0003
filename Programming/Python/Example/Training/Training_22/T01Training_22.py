import os
import sys

"""
Python 연습 문제 22
- 10 진수 -> 2 진수로 변환하기 (+ 재귀 호출)
- 사용자로부터 10 진수 수를 입력 받은 후 해당 수를 2 진수 형태로 출력한다
- 단, 서식 사용 X

Ex)
정수 입력 : 10
결과 : 1010
"""


# Training 22
def start(args):
	nVal = int(input("정수 입력 : "))
	
	oBinary = convert_ToBinary(nVal)
	print(f"결과 : {oBinary}")
	
	
# 10 진수 -> 2 진수로 변환한다
def convert_ToBinary(a_nVal):
	# 재귀 호출이 불가능 할 경우
	if a_nVal <= 0:
		return ""
	
	oStr = convert_ToBinary(a_nVal // 2)
	return oStr + f"{a_nVal % 2}"
