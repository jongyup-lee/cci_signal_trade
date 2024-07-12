from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
API 사용에 있어 가장 먼저 할 일은 종목코드를 얻는것입니다. 
로그인이 완료되면 GetCodeListByMarket 메서드를 호출하여 각 시장에 상장된 종목코드 리스트를 얻을 수 있습니다.

파라미터    	시장
"0"     	코스피
"3"     	ELW
"4"     	뮤추얼펀드
"5"     	신주인수권
"6"     	리츠
"8"     	ETF
"9"     	하이얼펀드
"10"        코스닥
"30"    	K-OTC
"50"    	코넥스
'''

kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)