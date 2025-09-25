import os
import sys

import random
from Training.Training_28.CEquip import CWeapon, CArmor

# 캐릭터
class CCharacter:
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		self.m_nHp = a_nHp
		self.m_nAtk = a_nAtk
		self.m_nDef = a_nDef
		
	# 공격력을 반환한다
	def getAtk(self):
		return self.m_nAtk
	
	# 방어력을 반환한다
	def getDef(self):
		return self.m_nDef
		
	# 대상을 공격한다
	def attack(self, a_oTarget):
		nDamage = self.getAtk() - a_oTarget.getDef()
		nDamage = nDamage if nDamage > 0 else 0
		
		nHp = a_oTarget.m_nHp - nDamage
		a_oTarget.m_nHp = nHp if nHp > 0 else 0
		
		
# 플레이어 캐릭터
class CPlayer(CCharacter):
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		super().__init__(a_nHp, a_nAtk, a_nDef)
		
		self.m_oName = "플레이어"
		self.m_oEquip = None
	
	# 공격력을 반환한다
	def getAtk(self):
		# 무기를 지니고 있을 경우
		if isinstance(self.m_oEquip, CWeapon):
			return super().getAtk() + self.m_oEquip.m_nVal
		
		return super().getAtk()
	
	# 방어력을 반환한다
	def getDef(self):
		# 방어구를 지니고 있을 경우
		if isinstance(self.m_oEquip, CArmor):
			return super().getDef() + self.m_oEquip.m_nVal
		
		return super().getDef()
		
	# 장비를 변경한다
	def setEquip(self, a_oEquip):
		self.m_oEquip = a_oEquip


# 몬스터 캐릭터
class CMonster(CCharacter):
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		super().__init__(a_nHp, a_nAtk, a_nDef)
		self.m_oName = "몬스터"



# 네임드 몬스터 캐릭터
class CMonster_Named(CMonster):
	# 초기화
	def __init__(self, a_nHp, a_nAtk, a_nDef):
		super().__init__(a_nHp, a_nAtk, a_nDef)
		self.m_oName = "네임드 몬스터"
		
	# 공격력을 반환한다
	def getAtk(self):
		# 크리티컬 일 경우
		if random.random() < 5.0:
			return super().getAtk() * 2
		
		return super().getAtk()
		