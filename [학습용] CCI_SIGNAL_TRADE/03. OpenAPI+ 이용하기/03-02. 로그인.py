'''
If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

상기 메시지를 뿌리면서 오류가 발생하는 케이스는

numpy 버전이 호환되지 않기 때문
다음과 같이 다운그레이드 후 정상 동작 확인하였음

01. pip uninstall numpy
02. pip install numpy==1.21.4
'''

from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블로킹 로그인 완료")