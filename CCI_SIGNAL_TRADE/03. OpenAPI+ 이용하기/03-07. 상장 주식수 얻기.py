from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
현재 키움증권의 API에는 버그가 있어서 상장 주식수가 21억을 넘더라도 21억까지만 표현할 수 있습니다. 
삼성전자의 경우 약 59억주가 상장되어 있는데 이 값을 제대로 얻어올 수 없습니다.

GetMasterListedStockCnt로 각 종목에 대한 상장 주식수를 얻어올수 있다
'''
code = '005930'
name = kiwoom.GetMasterCodeName(code)
stock_cnt = kiwoom.GetMasterListedStockCnt(code)
print('%s의 상장주식수 : %s' % (name, stock_cnt))