from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 전체 주식 계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
# 매매 주식 계좌
stock_account = accounts[1]

code = '005930'
kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, code, 10, 0, "03", "")