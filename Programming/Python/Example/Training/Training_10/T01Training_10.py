import os
import sys

"""
Python 연습 문제 10
- 구구단 출력하기
- 사용자로부터 숫자 2 개를 입력 받아 첫번째 수부터 두번째 수까지 구구단을 출력한다

Ex)
정수 (2 개) 입력 : 4 2
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...이하 생략

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...이하 생략

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...이하 생략
"""


# Training 10
def start(args):
	oTokens = input("정수 (2 개) 입력 : ").split()
	
	nValA = int(oTokens[0])
	nValB = int(oTokens[1])
	
	nOffset = 1 if nValA <= nValB else -1
	
	while nValA != nValB + nOffset:
		print(f"=====> {nValA} 단 <=====")
		
		for j in range(10):
			print(f"{nValA} * {j} = {nValA * j}")
		
		print()
		nValA += nOffset
		