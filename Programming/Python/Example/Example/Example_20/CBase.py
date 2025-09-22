import os
import sys


# 부모 클래스
class CBase:
	# 초기화
	def __init__(self, a_nVal, a_fVal):
		self.m_nVal = a_nVal
		self.m_fVal = a_fVal
		
	# 비교 결과를 반환한다
	def __eq__(self, a_oOther):
		return self.m_nVal == a_oOther.m_nVal and self.m_fVal == a_oOther.m_fVal
		
	# 정보를 반환한다
	def __str__(self):
		return f"정수 : {self.m_nVal}\n실수 : {self.m_fVal}"
	