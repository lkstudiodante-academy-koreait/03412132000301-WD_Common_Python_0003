import os
import sys


# 유닛 정보
class CInfo_Unit:
	# 초기화
	def __init__(self, a_oName, a_nCost):
		self.m_oName = a_oName
		self.m_nCost = a_nCost


# 유닛 정보 테이블
class CTable_UnitInfo:
	m_oInst = None
	
	# 초기화
	def __init__(self):
		self.m_oListInfos_Unit = []
		
	# 유닛 정보 개수를 반환한다
	def getNumInfos_Unit(self):
		return len(self.m_oListInfos_Unit)
		
	# 유닛 정보를 반환한다
	def getInfo_Unit(self, a_nIdx):
		return self.m_oListInfos_Unit[a_nIdx]
	
	# 인스턴스를 반환한다
	@classmethod
	def getInst(cls):
		# 인스턴스가 없을 경우
		if CTable_UnitInfo.m_oInst == None:
			CTable_UnitInfo.m_oInst = CTable_UnitInfo()
			
		return CTable_UnitInfo.m_oInst
		
	# 유닛 정보를 로드한다
	def loadInfos_Unit_FromFile(self, a_oPath_File):
		with open(a_oPath_File, "rt") as oRStream:
			for oInfo_Unit in oRStream.readlines():
				oTokens = oInfo_Unit.split(",")
				oCost = oTokens[1].replace("\n", "")
				
				oInfo_Unit = CInfo_Unit(oTokens[0], int(oCost))
				self.m_oListInfos_Unit.append(oInfo_Unit)
				