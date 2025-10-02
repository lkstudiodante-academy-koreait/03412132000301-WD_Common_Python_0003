import os
import sys

import re
import ssl
import time

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

"""
Python 연습 문제 36
- 위키피디아 사이트 크롤링하기
- 요구 사항은 연습 문제 35 번 참고
- 단, 위키피디아 내부 링크를 방문해서 다른 웹 페이지이 링크도 크롤링한다
"""


# Training 36
def start(args):
	ssl._create_default_https_context = ssl._create_unverified_context
	oSearch = input("위키피디아 검색어 입력 : ")
	
	oSetLinks = set()
	getLinks_WebPage(oSearch, 0, oSetLinks)
	
	with open("P_T01Training_36_01.txt", "wt") as oWStream:
		for oLink in oSetLinks:
			oWStream.write(f"{oLink}\n")


# 웹 페이지 링크를 반환한다
def getLinks_WebPage(a_oURL, a_nDepth, a_oOutSetLinks):
	# 링크 탐색이 불가능 할 경우
	if a_nDepth > 3:
		return
	
	time.sleep(0.25)
	oURL_Replace = a_oURL.replace("/wiki/", "")
	
	print(a_oURL)
	
	try:
		oHeaders = {
			"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
		}
		
		oURL = f"https://en.wikipedia.org/wiki/{oURL_Replace}"
		oRequest = Request(oURL, headers = oHeaders)
		
		oPage = urlopen(oRequest)
		oBSoup = BeautifulSoup(oPage.read(), "html.parser")
		
		oCompile = re.compile(r"^(/wiki/)")
		oListTags = oBSoup.findAll("a", { "href" : oCompile })
		
		for oTag in oListTags:
			oLink = oTag.attrs["href"]
			
			# 링크 탐색이 불가능 할 경우
			if oLink in a_oOutSetLinks:
				continue
				
			a_oOutSetLinks.add(oLink)
			getLinks_WebPage(oLink, a_nDepth + 1, a_oOutSetLinks)

	except Exception as oException:
		print(oException)
		