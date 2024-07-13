# from 폴더명.파일명 import 클래스명
from getKiwoomCondtion.kiwoomConditionStockList import GetStockList
from catchSignal.CCISignal.catchCCISignal import CCIMonitor

class MainControl():
    def __init__(self) -> None:
        self.stockList = GetStockList()
        self.cciMonitor = CCIMonitor()
    
    # 키움 증권의 조건식을 선별하여 해당 조건식에 포함된 종목들의 종목 코드를 가져온다.
    def getStockCodes(self):
        self.codes = self.stockList.getConditionStocks()
        #print('[__init__] - %s' % self.codes)

    # getStockCodes를 통해 획득한 종목들에 대한 CCI 시그널을 감시한다.
    # CCI Signal 조건에 맞는 종목 코드를 획득한다.
    ###############################################################################################
    # ToDo : 
    # 개발시에는 코드 리스트를 넘기지만
    # 운영시에는 실시간 데이터를 받을 때마다 해당 sCode를 넘기도록 수정해야 한다.
    ###############################################################################################
    def catchCCISignal(self):
        self.catchSignalStock = self.cciMonitor.monitor_cciSignal_stocks(self.codes)
        print('[__init__] - %s' % self.catchSignalStock)


if __name__ == "__main__":
    mc = MainControl()
    mc.getStockCodes()
    mc.catchCCISignal()
    