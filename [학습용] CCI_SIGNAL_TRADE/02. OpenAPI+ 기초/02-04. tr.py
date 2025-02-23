import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import pythoncom

class Kiwoom:
    def __init__(self):
        self.login = False
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)
        self.ocx.OnReceiveTrData.connect(self.OnReceiveTrData)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while not self.login:
            pythoncom.PumpWaitingMessages()

    def OnReceiveTrData(self, screen, rqname, trcode, record, next):
        print(screen, rqname, trcode, record, next)
        per = self.GetCommData(trcode, rqname, 0, "PER")
        pbr = self.GetCommData(trcode, rqname, 0, "PBR")
        print("per : %s / pbr : %s " % (per, pbr))

    def GetMasterCodeName(self, code):
        name = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return name

    def OnEventConnect(self, err_code):
        self.login = True

    def SetInputValue(self, id, value):
        self.ocx.dynamicCall("SetInputValue(QString, QString)", id, value)

    def CommRqData(self, rqname, qrcode, next, screen):
        self.ocx.dynamicCall("CommRqData(QString, QString, int, QString)", rqname, qrcode, next, screen)

    def GetCommData(self, rqname, qrcode, index, item):
        print("GetCommData() - rqname : %s, qrcode : %s, index : %s, item : %s" % (rqname, qrcode, index, item))
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, QString)", rqname, qrcode, index, item)
        return data.strip()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()

        # tr request
        self.kiwoom.SetInputValue("종목코드", "005935")
        self.kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()




