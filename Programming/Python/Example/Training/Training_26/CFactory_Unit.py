import os
import sys

from datetime import datetime
from Training.Training_26.CUnit import CUnitA, CUnitB, CUnitC


# 유닛 팩토리
class CFactory_Unit:
	m_oInst = None
	
	# 초기화
	def __init__(self):
		self.m_oListClasses_Unit = [
			CUnitA, CUnitB, CUnitC
		]
		
	# 유닛 클래스를 반환한다
	def getCls_Unit(self, a_nIdx):
		return self.m_oListClasses_Unit[a_nIdx]
	
	# 인스턴스를 반환한다
	@classmethod
	def getInst(cls):
		# 인스턴스가 없을 경우
		if CFactory_Unit.m_oInst == None:
			CFactory_Unit.m_oInst = CFactory_Unit()
			
		return CFactory_Unit.m_oInst
		
	# 유닛을 생성한다
	def createUnit(self, a_nIdx):
		oTime = datetime.now()
		return self.m_oListClasses_Unit[a_nIdx](oTime)
	