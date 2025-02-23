'''
개발가이드를 참조하면 주문은 SendOrder 메소드를 사용함을 확인할 수 있습니다. 
SendOrder 역시 하나의 Transaction (TR)으로 간주하는데 주문은 1초에 최대 5번까지만 가능합니다.

SendOrder 메소드의 입력값은 다음과 같습니다.

입력값	        의미
-------------------------------------------------------------------------------
sRQName	        사용자가 임의로 지정할 수 있는 이름입니다. (예: "삼성전자주문")
sScreenNO	    화면번호로 "0"을 제외한 4자리의 문자열을 사용합니다. (예: "1000")
sAccNo	        계좌번호입니다. (예: "8140977311")
nOrderType	    주문유형입니다. (1: 매수, 2: 매도, 3: 매수취소, 4: 매도취소, 5: 매수정정, 6: 매도 정정)
sCode	        매매할 주식의 종목코드입니다.
nQty	        주문수량입니다.
nPrice	        주문단가입니다.
sHogaGb	        '00': 지정가, '03': 시장가
sOrgOrderNo	    원주문번호로 주문 정정시 사용합니다.
'''

