from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
CommConnect 메소드를 통해 로그인을 수행한 후 GetConnectState 메소드를 호출하여 연결 상태를 확인할 수 있습니다. 
GetConnectState 메소드의 리턴값이 0이면 서버에 연결되지 않은 상태이고 1이면 서버에 연결 상태임을 의미합니다.
'''

state = kiwoom.GetConnectState()
if state == 0:
    print('연결안됨')
else:
    print('연결됨')