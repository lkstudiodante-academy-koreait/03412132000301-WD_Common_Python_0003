import os
import sys

import sqlite3


# 회원 테이블
class CTable_Member:
	m_oInst = None
	
	# 초기화
	def __init__(self):
		self.m_oConnection = None
	
	# 모든 회원을 반환한다
	def getMembers_All(self):
		oQuery = "SELECT * FROM MemberTable"
		return self.executeFetch(oQuery)
	
	# 인스턴스를 반환한다
	@classmethod
	def getInst(cls):
		# 인스턴스가 없을 경우
		if CTable_Member.m_oInst == None:
			CTable_Member.m_oInst = CTable_Member()
		
		return CTable_Member.m_oInst
	
	# 데이터베이스를 연결한다
	def connect(self, a_oPath_DB):
		self.m_oConnection = sqlite3.connect(a_oPath_DB)
		self.executeQuery("CREATE TABLE IF NOT EXISTS MemberTable(Name TEXT PRIMARY KEY, PNumber TEXT)")
	
	# 회원을 추가한다
	def addMember(self, a_oName, a_oPNumber):
		oQuery = f"INSERT OR IGNORE INTO MemberTable(Name, PNumber) VALUES(\"{a_oName}\", \"{a_oPNumber}\")"
		self.executeQuery(oQuery)
		
	# 회원을 제거한다
	def removeMember(self, a_oName):
		oQuery = f"DELETE FROM MemberTable WHERE Name = \"{a_oName}\""
		self.executeQuery(oQuery)
		
	# 회원을 탐색한다
	def findMember(self, a_oName):
		oQuery = f"SELECT * FROM MemberTable WHERE Name = \"{a_oName}\""
		oListResults = self.executeFetch(oQuery)
		
		return oListResults[0] if len(oListResults) > 0 else None
	
	# SQL 쿼리문을 실행한다
	def executeQuery(self, a_oQuery):
		oCursor = self.m_oConnection.cursor()
		oCursor.execute(a_oQuery)
		
		self.m_oConnection.commit()
		
	# SQL 쿼리문을 실행한다
	def executeFetch(self, a_oQuery):
		oCursor = self.m_oConnection.cursor()
		oCursor.execute(a_oQuery)
		
		return oCursor.fetchall()
	