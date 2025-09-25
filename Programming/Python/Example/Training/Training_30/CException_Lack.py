import os
import sys


# 비용 부족 예외
class CException_Lack(Exception):
	# 초기화
	def __init__(self):
		super().__init__("비용이 부족합니다.")
		