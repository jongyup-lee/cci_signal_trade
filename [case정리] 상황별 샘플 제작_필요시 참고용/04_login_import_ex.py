class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.dynamicCall("CommConnect()")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)

    def OnEventConnect(self, err_code):
        print(err_code)