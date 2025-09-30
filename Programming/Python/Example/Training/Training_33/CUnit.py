import os
import sys


# 유닛
class CUnit:
	# 초기화
	def __init__(self, a_oInfo_Unit, a_oTime):
		self.m_oInfo_Unit = a_oInfo_Unit
		self.m_oTime = a_oTime
	
	# 정보를 출력한다
	def showInfo(self):
		oName = self.m_oInfo_Unit.m_oName
		print(f"{oName} 을(를) {self.m_oTime} 에 생산했습니다.")
		