import os
import sys

from Example.Example_20.CBase import CBase


# 자식 클래스
class CDerived(CBase):
	# 초기화
	def __init__(self, a_nVal, a_fVal, a_oStr):
		super().__init__(a_nVal, a_fVal)
		self.m_oStr = a_oStr
	
	# 비교 결과를 반환한다
	def __eq__(self, a_oOther):
		bIsEquals = super().__eq__(a_oOther)
		return bIsEquals and self.m_oStr == a_oOther.m_oStr
	
	# 정보를 반환한다
	def __str__(self):
		oStr = super().__str__()
		return f"{oStr}\n문자열 : {self.m_oStr}"
	