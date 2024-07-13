from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
GetMasterConstruction
감리구분은 '정상', '투자주의', '투자경고', '투자위험', '투자주의환기종목'의 값을 갖습니다. 
삼성전자(005930)의 경우 '정상' 값이 출력됩니다.
'''
code = '003580'
감리구분 = kiwoom.GetMasterConstruction(code)
print('감리구분 : %s' % 감리구분)
