'''
키움 OpenAPI+는 로그인을 수행한 후 GetLoginInfo 메서드를 호출하여 사용자 정보를 얻을 수 있습니다.
GetLoginInfo 메서드의 인자값에 따라 얻어올 수 있는 정보는 다음 표와 같습니다.

태그	           | 정보
--------------------------------------------------------------------
ACCOUNT_CNT	    전체 계좌 개수를 반환합니다.
ACCNO	        전체 계좌를 반환합니다.
USER_ID	        사용자 ID를 반환합니다.
USER_NAME	    사용자명을 반환합니다.
KEY_BSECGB	    키보드보안 해지여부를 반환합니다. 0: 정상, 1: 해지
FIREW_SECGB	    방화벽 설정 여부를 반환합니다. 0: 미설정, 1: 설정, 2: 해지
'''

from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT") #전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")
user_id = kiwoom.GetLoginInfo("USER_ID")
user_name = kiwoom.GetLoginInfo("USER_NAME")
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")

print(account_num)
print(accounts)
print(user_id)
print(user_name)
print(keyboard)
print(firewall)