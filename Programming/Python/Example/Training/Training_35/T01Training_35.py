import os
import sys

import re
import ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

"""
Python 연습 문제 35
- 위키피디아 사이트 크롤링하기 (+ https://en.wikipedia.org/wiki/ + 검색어)
- 사용자로부터 검색어를 입력 받는다
- 입력 받은 검색어를 기반으로 위키피디아 사이트를 크롤링한다
- 크롤링 할 대상은 위키피디아 내부 링크이다 (+ 즉, /wiki/ 로 시작하는 링크)
- 크롤링 한 위키피디아 내부 링크는 모두 파일에 기록한다
"""

# Training 35
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	oSearch = input("위키피디아 검색어 입력 : ")
	
	try:
		oHeaders = {
			"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
		}
		
		oURL = f"https://en.wikipedia.org/wiki/{oSearch}"
		oRequest = Request(oURL, headers = oHeaders)
		
		oPage = urlopen(oRequest)
		oBSoup = BeautifulSoup(oPage.read(), "html.parser")
		
		oCompile = re.compile(r"^(/wiki/)")
		oListTags = oBSoup.findAll("a", { "href" : oCompile })
		
		with open("P_T01Training_35_01.txt", "wt") as oWStream:
			oSetLinks = set()
			
			for oTag in oListTags:
				oLink = oTag.attrs["href"]
				oSetLinks.add(oLink)
				
			for oLink in oSetLinks:
				oWStream.write(f"{oLink}\n")
		
	except Exception as oException:
		print(oException)
		