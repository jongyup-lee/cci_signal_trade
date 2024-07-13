from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
'''
삼성전자(종목코드: 005930) 종목에 대해 10주를 시장가로 매수해 봅시다.
'''
# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
print('전체주식 계좌 : %s' % accounts)
stock_account = accounts[1]

# 삼성전자
code = '005930'
kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, code, 10, 0, '03', '')