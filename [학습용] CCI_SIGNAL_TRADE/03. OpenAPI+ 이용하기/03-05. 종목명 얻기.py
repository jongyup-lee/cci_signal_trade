from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
증권사 API를 사용할 때 주로 종목코드를 사용합니다. 
그러나 종목코드만 보고는 어떤 종목인지 알기 어렵지요? 
키움 OpenAPI+의 GetMasterCodeName 메서드에 종목코드를 전달하면 종목명을 얻을 수 있습니다.
'''

name = kiwoom.GetMasterCodeName('005930')
print('name : %s' % name)