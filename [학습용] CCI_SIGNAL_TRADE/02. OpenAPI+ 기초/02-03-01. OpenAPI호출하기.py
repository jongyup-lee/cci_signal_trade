import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import pythoncom

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)
        self.CommConnect()

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")

    def GetMasterCodeName(self, code):
        name =  self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return name

    def OnEventConnect(self, err_code):
        print("로그인 결과")
        code = "005930"
        name = self.GetMasterCodeName(code)
        print(code, name)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()