from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
GetMasterListedStockDate
어떤 종목의 상장일을 확인할 때 GetMasterListedStockDate 메소드를 사용합니다. 
위 코드는 다음과 같이 삼성전자의 상장일과 데이터 타입을 출력합니다.
'''
code = '005930'
name = kiwoom.GetMasterCodeName(code)
stock_date = kiwoom.GetMasterListedStockDate(code)

print('%s 의 상장일 : %s' % (name, stock_date))