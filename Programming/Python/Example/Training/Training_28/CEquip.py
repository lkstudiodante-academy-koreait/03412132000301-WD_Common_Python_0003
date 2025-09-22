import os
import sys


# 장비
class CEquip:
	# 초기화
	def __init__(self, a_nVal):
		self.m_nVal = a_nVal

		
# 무기
class CWeapon(CEquip):
	# 초기화
	def __init__(self, a_nVal):
		super().__init__(a_nVal)


# 방어구
class CArmor(CEquip):
	# 초기화
	def __init__(self, a_nVal):
		super().__init__(a_nVal)
