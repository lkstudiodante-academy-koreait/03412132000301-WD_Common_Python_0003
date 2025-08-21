import os
import sys

import random

"""
Python 연습 문제 6
- 업/다운 게임 제작하기
- 1 ~ 99 사이의 수 중 1 개를 랜덤하게 추출한다
- 사용자로부터 정수를 입력받아 정답과 비교한다
- 입력 받은 정수가 정답을 프로그램을 종료한다
- 입력 받은 정수가 정답이 아닐 경우 정답을 맞출 수 있도록 가이드 메세지를 출력한다

Ex)
정답 : 85

정수 입력 : 90
정답은 90 보다 작습니다.

정수 입력 : 50
정답은 50 보다 큽니다.

정수 입력 : 85
프로그램을 종료합니다.
"""


# Training 6
def start(args):
	nAnswer = random.randrange(1, 100)
	print(f"정답 : {nAnswer}\n")
	
	while True:
		nVal = int(input("정수 입력 : "))
		
		# 정답 일 경우
		if nVal == nAnswer:
			break
			
		oMsg = "큽니다." if nVal < nAnswer else "작습니다."
		print(f"정답은 {nVal} 보다 {oMsg}\n")
		
	print("프로그램을 종료합니다.")
	