import os
import sys


# 유닛 A
class CUnitA:
	COST = 250
	NAME = "유닛 A"
	
	# 초기화
	def __init__(self, a_oTime):
		self.m_oTime = a_oTime
		
	# 정보를 출력한다
	def showInfo(self):
		print(f"{CUnitA.NAME} 을(를) {self.m_oTime} 에 생산했습니다.")


# 유닛 B
class CUnitB:
	COST = 500
	NAME = "유닛 B"
	
	# 초기화
	def __init__(self, a_oTime):
		self.m_oTime = a_oTime
	
	# 정보를 출력한다
	def showInfo(self):
		print(f"{CUnitB.NAME} 을(를) {self.m_oTime} 에 생산했습니다.")
		

# 유닛 C
class CUnitC:
	COST = 750
	NAME = "유닛 C"
	
	# 초기화
	def __init__(self, a_oTime):
		self.m_oTime = a_oTime
	
	# 정보를 출력한다
	def showInfo(self):
		print(f"{CUnitC.NAME} 을(를) {self.m_oTime} 에 생산했습니다.")
		