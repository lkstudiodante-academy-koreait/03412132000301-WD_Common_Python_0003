import os
import sys

import random

from Example.Example_28.CList_Array import CList_Array
from Example.Example_28.CList_SLinked import CList_SLinked
from Example.Example_28.CList_DLinked import CList_DLinked

"""
자료구조 (Data Structure) 란?
- 데이터를 저장하고 표현하는 방법을 의미한다. (+ 즉, 자료구조는 데이터를 저장하고 저장 된 데이터에 대한
연산을 통칭하는 용어라는 것을 알 수 있다.)

자료구조는 크게 기본 자료구조와 복합 자료구조로 구분 된다.

기본 자료구조 종류
- 정수
- 실수
- 문자열
- 등등...

위와 같이 기본 자료구조는 프로그래밍 언어가 지원하는 기본 자료형이라는 것을 알 수 있다. (+ 즉,
대부분의 프로그래밍 언어는 기본 자료구조를 지원한다는 것을 의미한다.)

따라서 자료구조라 불리는 것은 일반적으로 복합 자료구조를 의미한다 (+ 즉, 일반적으로 자료구조는
여러 데이터를 효율적으로 관리하고 연산하는 방법이라는 것을 알 수 있다.)

기본 자료구조는 대부분 1 개의 데이터를 저장하고 연산하는 것이 가능하지만 복합 자료구조는 여러 데이터를
저장하고 연산하는 것이 가능하다. (+ 즉, 리스트와 같은 컬렉션은 복합 자료구조라는 것을 알 수 있다.)

복합 자료구조는 내부적으로 데이터를 관리하는 형태에 따라 선형 자료구조와 비선형 자료구조로 구분되며
자료구조마다 사용하는 상황이 다르기 때문에 적절한 자료구조를 선택 할 수 있는 선구안이 필요하다. (+ 즉,
잘못 된 자료구조의 선택은 명령문의 구성을 복잡하게 만든다는 것을 알 수 있다.)

선형 자료구조 종류
- 리스트 (+ 배열, 연결)
- 스택
- 큐

리스트 (List) 란?
- 목록의 형태로 데이터를 관리하는 자료구조를 의미한다. (+ 즉, 리스트에 의해 관리되는 데이터는 순서가
존재한다는 것을 알 수 있다.)

리스트는 구현하는 방식에 따라 배열 기반 리스트 (Array List) 와 연결 기반 리스트 (Linked List) 로 구분 된다.

배열 기반 리스트 (Array List) 란?
- 배열을 이용해서 데이터를 관리하는 자료구조를 의미한다. (+ 즉, 데이터의 순서와 메모리의 순서가 일치한다는 것을
알 수 있다.)

연결 기반 리스트 (Linked List) 란?
- 참조를 이용해서 데이터를 관리하는 자료구조를 의미한다. (+ 즉, 데이터의 순서와 메모리의 순서가
일치하지 않을 수 있다는 것을 알 수 있다.)

배열 기반 리스트 (Array List) vs 연결 기반 리스트 (Linked List)
- 배열 기반 리스트는 배열을 통해 구현 되었기 때문에 데이터의 위치를 알고 있다면 [] (인덱스 연산자) 를 통해
빠른 속도로 접근하는 것이 가능하다.

단, 배열 기반 리스트는 내부적으로 관리하는 데이터의 순서와 메모리의 순서가 일치하기 때문에 특정 위치에
데이터를 추가하거나 제거 할 경우 데이터의 이동이 발생한다는 단점이 존재한다. (+ 즉, 데이터의 추가/제거 가
빈번 할 경우 성능이 떨어진다는 것을 알 수 있다.)

반면 연결 기반 리스트는 참조를 통해 구현 되었기 때문에 데이터의 위치를 알고 있다고 하더라도 항상 첫 데이터부터
순차적으로 접근해야되는 단점이 존재한다. (+ 즉, 임의 접근이 불가능하다는 것을 알 수 있다.)

단, 연결 기반 리스트는 특정 위치에 데이터를 추가하거나 제거 할 경우 배열 기반 리스트처럼 데이터의 이동이
발생하지 않는다는 장점이 존재한다. (+ 즉, 데이터의 추가/제거 가 배열 기반 리스트에 비해 용이하다는 것을
알 수 있다.)
"""


# Example 28 (자료구조 - 1)
def start(args):
	oListValuesA = CList_Array()
	oListValuesB = CList_SLinked()
	oListValuesC = CList_DLinked()
	
	for i in range(0, 10):
		nVal = random.randrange(1, 100)
		
		oListValuesA.addVal(nVal)
		oListValuesB.addVal(nVal)
		oListValuesC.addVal(nVal)
	
	print("=====> 리스트 <=====")
	printValues(oListValuesA)
	printValues(oListValuesB)
	printValues(oListValuesC)
	
	nVal_Insert = int(input("\n정수 입력 (추가) : "))
	oListValuesA.insertVal(0, nVal_Insert)
	oListValuesB.insertVal(0, nVal_Insert)
	oListValuesC.insertVal(0, nVal_Insert)
	
	print("\n=====> 리스트 - 추가 후 <=====")
	printValues(oListValuesA)
	printValues(oListValuesB)
	printValues(oListValuesC)
	
	nVal_Remove = int(input("\n정수 입력 (제거) : "))
	oListValuesA.removeVal(nVal_Remove)
	oListValuesB.removeVal(nVal_Remove)
	oListValuesC.removeVal(nVal_Remove)
	
	print("\n=====> 리스트 - 제거 후 <=====")
	printValues(oListValuesA)
	printValues(oListValuesB)
	printValues(oListValuesC)


# 값을 출력한다
def printValues(a_oListValues):
	for i in range(0, a_oListValues.m_nNumValues):
		nVal = a_oListValues.getVal(i)
		print(f"{nVal}, ", end = "")
	
	print()
	