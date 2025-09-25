import os
import sys

"""
Python 연습 문제 31
- 파일 복사 프로그램 제작하기
- 사용자로부터 원본 파일 경로와 사본 파일 경로를 입력 받는다
- 입력 받은 경로를 기반으로 원반 파일과 동일한 데이터를 지니고 있는 사본 파일 생성한다

Ex)
원본 파일 경로 입력 : SomeFile.txt
사본 파일 경로 입력 : SomeFile_Copy.txt

Case 1. 원본 파일이 존재 할 경우
SomeFile.txt -> SomeFile_Copy.txt 복사가 완료되었습니다.

Case 2. 원본 파일이 없을 경우
SomeFile.txt 이(가) 존재하지 않습니다.
"""


# Training 31
def start(args):
	oPath_Origin = input("원본 파일 경로 입력 : ")
	oPath_Copy = input("사본 파일 경로 입력 : ")
	
	# 원본 파일이 없을 경우
	if not os.path.exists(oPath_Origin):
		print(f"{oPath_Origin} 이(가) 존재하지 않습니다.")
		return
	
	oPath_DirName = os.path.dirname(oPath_Copy)
	
	# 사본 파일 경로에 디렉토리가 포함되어있을 경우
	if oPath_DirName:
		os.makedirs(oPath_DirName, exist_ok = True)
	
	with open(oPath_Origin, "rb") as oRStream:
		with open(oPath_Copy, "wb") as oWStream:
			while True:
				oBytes = oRStream.read(1)
				
				# 데이터가 없을 경우
				if not oBytes:
					break
					
				oWStream.write(oBytes)
				
	print(f"{oPath_Origin} -> {oPath_Copy} 파일을 복사했습니다.")
