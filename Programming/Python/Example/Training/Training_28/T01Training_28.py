import os
import sys

import time
import random

from Training.Training_28.CEquip import CWeapon, CArmor
from Training.Training_28.CCharacter import CPlayer, CMonster, CMonster_Named

"""
Python 연습 문제 28
- 게임 시뮬레이션 제작하기
- 캐릭터는 체력, 공격력, 방어력을 지니고 있다
- 플레이어 캐릭터의 스탯은 사용자로부터 입력 받는다
- 몬스터 캐릭터의 스탯은 플레이어의 캐릭터의 각 스탯의 50 % ~ 150 % 범위로 랜덤하게 지정한다
- 플레이어 캐릭터와 몬스터 캐릭터는 각각 번갈아가면서 공격을 진행하며 선공은 플레이어 캐릭터가 먼저 진행한다
- 공격 후 상대 캐릭터가 사망했을 경우 공격 단계는 중단되고 승리자를 출력한다

Ex)
플레이어 체력 입력 : 100
플레이어 공격력 입력 : 25
플레이어 방어력 입력 : 10

=====> 몬스터 정보 <=====
체력 : 125
공격력 : 15
방어력 : 20

=====> 플레이어 공격 후 <=====
플레이어 체력 : 100
몬스터 체력 : 120

...이하 생략

=====> 플레이어 공격 후 <=====
플레이어 체력 : 50
몬스터 체력 : 0

플레이어 이(가) 승리했습니다.
"""


# Training 28
def start(args):
	nHp = int(input("플레이어 체력 입력 : "))
	nAtk = int(input("플레이어 공격력 입력 : "))
	nDef = int(input("플레이어 방어력 입력 : "))
	
	oPlayer = CPlayer(nHp, nAtk, nDef)
	oMonster = createMonster(oPlayer)
	
	oEquip = createEquip(oPlayer)
	oPlayer.setEquip(oEquip)
	
	print("\n=====> 플레이어 장비 정보 <=====")
	print(f"보정치 : {oEquip.m_nVal}")
	
	print("\n=====> 몬스터 정보 <=====")
	print(f"체력 : {oMonster.m_nHp}")
	print(f"공격력 : {oMonster.m_nAtk}")
	print(f"방어력 : {oMonster.m_nDef}\n")
	
	oWinner = None
	
	while True:
		oPlayer.attack(oMonster)
		
		print("-----> 플레이어 공격 후")
		print(f"플레이어 체력 : {oPlayer.m_nHp}")
		print(f"몬스터 체력 : {oMonster.m_nHp}\n")
		
		time.sleep(0.25)
		
		# 플레이어가 승리했을 경우
		if oMonster.m_nHp <= 0:
			oWinner = oPlayer
			break
			
		oMonster.attack(oPlayer)
		
		print("-----> 몬스터 공격 후")
		print(f"플레이어 체력 : {oPlayer.m_nHp}")
		print(f"몬스터 체력 : {oMonster.m_nHp}\n")
		
		time.sleep(0.25)
		
		# 몬스터가 승리했을 경우
		if oPlayer.m_nHp <= 0:
			oWinner = oMonster
			break
			
	print(f"{oWinner.m_oName} 이(가) 승리했습니다.")
	

# 장비를 생성한다
def createEquip(a_oPlayer):
	# 무기를 생성해야 될 경우
	if random.random() < 0.5:
		return CWeapon(int(a_oPlayer.m_nAtk * 0.2))
	
	return CArmor(int(a_oPlayer.m_nDef * 0.2))


# 몬스터를 생성한다
def createMonster(a_oPlayer):
	nHp = a_oPlayer.m_nHp * (random.random() + 0.5)
	nAtk = a_oPlayer.m_nAtk * (random.random() + 0.5)
	nDef = a_oPlayer.m_nDef * (random.random() + 0.5)
	
	# 일반 몬스터 일 경우
	if random.random() < 0.5:
		return CMonster(int(nHp), int(nAtk), int(nDef))
	
	return CMonster_Named(int(nHp), int(nAtk), int(nDef))
