from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
GetMasterLastPrice
종목별 전일가는 GetMasterLastPrice 메소드를 통해 쉽게 얻을 수 있습니다. 
해당 메소드의 인자로 종목 코드를 입력하면 전일 종가를 리턴합니다.
'''
code = '005930'
name = kiwoom.GetMasterCodeName(code)

전일가 = kiwoom.GetMasterLastPrice(code)

print('%s의 전일가는 %s입니다.' % (name, 전일가))