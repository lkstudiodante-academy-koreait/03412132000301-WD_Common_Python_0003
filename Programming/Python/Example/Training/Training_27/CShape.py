import os
import sys


# 도형
class CShape:
	# 초기화
	def __init__(self, a_nColor):
		self.m_nColor = a_nColor
		
	# 색상을 반환한다
	def getStr_Color(self):
		oListColors = [
			"", "빨간색", "녹색", "파란색"
		]
		
		return oListColors[self.m_nColor]
	
	# 모양을 반환한다
	def getStr_Shape(self):
		pass
	
	# 도형을 그린다
	def draw(self):
		pass
	
	
# 선
class CLine(CShape):
	# 초기화
	def __init__(self, a_nColor):
		super().__init__(a_nColor)
		
	# 모양을 반환한다
	def getStr_Shape(self):
		return "선"
	
	# 도형을 그린다
	def draw(self):
		oStr_Color = self.getStr_Color()
		print(f"{oStr_Color} 선을 그렸습니다.")


# 삼각형
class CTriangle(CShape):
	# 초기화
	def __init__(self, a_nColor):
		super().__init__(a_nColor)
	
	# 모양을 반환한다
	def getStr_Shape(self):
		return "삼각형"
	
	# 도형을 그린다
	def draw(self):
		oStr_Color = self.getStr_Color()
		print(f"{oStr_Color} 삼각형을 그렸습니다.")


# 사각형
class CRectangle(CShape):
	# 초기화
	def __init__(self, a_nColor):
		super().__init__(a_nColor)
	
	# 모양을 반환한다
	def getStr_Shape(self):
		return "사각형"
	
	# 도형을 그린다
	def draw(self):
		oStr_Color = self.getStr_Color()
		print(f"{oStr_Color} 사각형을 그렸습니다.")
		