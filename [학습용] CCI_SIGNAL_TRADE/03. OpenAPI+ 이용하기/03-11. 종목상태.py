from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
GetMasterStockState
GetMasterStockState는 종목 상태를 리턴하는 메소드입니다. 
메소드의 인자로 종목 코드를 입력하면 됩니다.
'''

code = '005930'
name = kiwoom.GetMasterCodeName(code)

종목상태 = kiwoom.GetMasterStockState(code)

print('%s이 종목상태 : %s' % (name, 종목상태))