import os
import sys

"""
Python 연습 문제 5
- 팩토리얼 출력하기
- 사용자로부터 1 ~ 9 사이의 수를 입력받는다
- 범위를 벗어난 수를 입력했을 경우 다시 입력을 요구한다
- 범위 내의 수를 입력했을 경우 해당 수의 팩토리얼을 출력한다

Ex)
정수 (1 ~ 9) 입력 : 10
1 ~ 9 사이의 수를 입력해주세요.

입력 (1 ~ 9) 입력 : 5
5! = 5 x 4 x 3 x 2 x 1
"""


# Training 5
def start(args):
	nVal = 0
	
	while True:
		nVal = int(input("정수 (1 ~ 9) 입력 : "))
		
		# 올바른 수를 입력했을 경우
		if nVal >= 1 and nVal <= 9:
			break
			
		print("1 ~ 9 사이의 수를 입력해주세요.\n")
		
	print(f"{nVal}! = ", end = "")
	
	for i in range(0, nVal):
		nVal_Factorial = nVal - i
		print(f"{nVal_Factorial}", end = "")
		
		# x 기호가 필요 할 경우
		if nVal_Factorial > 1:
			print(" x ", end = "")
		
	print()
	