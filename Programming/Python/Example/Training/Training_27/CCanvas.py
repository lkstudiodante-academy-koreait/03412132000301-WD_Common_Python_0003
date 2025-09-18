import os
import sys


# 그림판
class CCanvas:
	# 초기화
	def __init__(self):
		self.m_oListShapes = []
		
	# 도형을 추가한다
	def addShape(self, a_oShape):
		self.m_oListShapes.append(a_oShape)
		
	# 모든 도형을 그린다
	def drawShapes_All(self):
		for oShape in self.m_oListShapes:
			oShape.draw()
			