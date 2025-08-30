import os
import sys

"""
Python 연습 문제 15
- 모든 조합 출력하기
- 가격이 다른 물건 3 개가 존재한다 (+ Ex. 50, 250, 500)
- 사용자로부터 소지 금액을 입력 받아 해당 소지 금액을 모두 소비해서 구입 할 수 있는 물건의 조합을 모두 출력한다
(+ 단, 각 물건은 최소 1 개 이상 구입)

Ex)
소지 금액 입력 : 1000

=====> 구입 가능 조합 <=====
물건 A x 5, 물건 B x 1 개, 물건 C x 1 개
"""


# Training 15
def start(args):
	PRICE_STUFF_A = 50
	PRICE_STUFF_B = 250
	PRICE_STUFF_C = 500
	
	nAmount = int(input("소지 금액 입력 : "))
	print("=====> 구입 가능 조합 <=====")
	
	for i in range(PRICE_STUFF_A, nAmount + 1, PRICE_STUFF_A):
		for j in range(PRICE_STUFF_B, nAmount + 1, PRICE_STUFF_B):
			for k in range(PRICE_STUFF_C, nAmount + 1, PRICE_STUFF_C):
				# 구입 가능 조합이 아닐 경우
				if i + j + k != nAmount:
					continue
					
				nNumStuffsA = i // PRICE_STUFF_A
				nNumStuffsB = j // PRICE_STUFF_B
				nNumStuffsC = k // PRICE_STUFF_C
				
				oMsgA = f"물건 A x {nNumStuffsA} 개"
				oMsgB = f"물건 B x {nNumStuffsB} 개"
				oMsgC = f"물건 C x {nNumStuffsC} 개"
				
				print(f"{oMsgA}, {oMsgB}, {oMsgC}")
