'''
키움 증권 API의 ocx 객체를 생성한 후 CommConnect 함수를 호출합니다.
로그인이 완료되면 OnEventConnect 이벤트가 발생합니다.
사용자는 해당 이벤트가 발생할 때 slot_login 이라는 메서드로 처리해주면 됩니다.
OnEventConnect 이벤트가 발생할 때 로그인의 상태코드가 같이 입력되는데 이 값을 print하고 있는 예제 코드입니다.
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.slot_login)
        self.ocx.dynamicCall("CommConnect()")

    def slot_login(self, err_code):
        print('로그인 상태 : %s' % err_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()