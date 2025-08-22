import os
import sys

"""
Python 연습 문제 4
- 합계/평균 계산하기
- 사용자로부터 정수를 입력받는다
- 입력 받은 정수가 0 보다 클 경우 정수를 누적 후 다시 입력을 받는다
- 입력 받은 정수가 0 보다 작거나 같을 경우 입력을 종료하고 합계와 평균을 출력한다

Ex)
1 번째 정수 입력 : 1
2 번째 정수 입력 : 2
3 번째 정수 입력 : 3
4 번째 정수 입력 : 0

합계 : 6
평균 : 2.0
"""


# Training 4
def start(args):
	nVal_Sum = 0
	nNumValues = 0
	
	while True:
		nVal = int(input(f"{nNumValues + 1} 번째 정수 입력 : "))
		
		# 반복을 종료했을 경우
		if nVal <= 0:
			"""
			break 키워드란?
			- continue 와 같은 점프문 중 하나로서 반복문 내부에서만 사용 가능하며 해당 키워드를 명시하면
			프로그램의 현재 흐름을 반복문 밖으로 이동 시키는 것이 가능하다. (+ 즉, break 키워드를 활용하면
			반복문을 즉시 종료 시키는 것이 가능하다.)
			"""
			break
			
		nVal_Sum += nVal
		nNumValues += 1

	print(f"\n합계 : {nVal_Sum}")
	print(f"평균 : {nVal_Sum / nNumValues}")
	