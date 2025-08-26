import os
import sys

"""
Python 연습 문제 9
- 구구단 출력하기
- 사용자로부터 숫자 2 개를 입력 받아 작은 수부터 큰 수까지 구구단을 출력한다
- 단, 숫자의 입력 순서는 상관 X

Ex)
정수 (2 개) 입력 : 4 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...이하 생략

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...이하 생략

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...이하 생략
"""


# Training 9
def start(args):
	oTokens = input("정수 (2 개) 입력 : ").split()
	
	nValA = int(oTokens[0])
	nValB = int(oTokens[1])
	
	# 보정이 필요 할 경우
	if nValA > nValB:
		nValA, nValB = nValB, nValA

	for i in range(nValA, nValB + 1):
		print(f"=====> {i} 단 <=====")

		for j in range(1, 10):
			print(f"{i} * {j} = {i * j}")

		print()
	