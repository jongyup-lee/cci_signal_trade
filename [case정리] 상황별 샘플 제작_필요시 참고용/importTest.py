# from 폴더명.파일명 import 클래스명
from conditionList import GetStockList

class CatchCCISignal():
    def __init__(self) -> None:
        self.stockList = GetStockList()
    
    def getStockCodes(self):
        self.codes = self.stockList.getConditionStocks()
        print(self.codes)

if __name__ == "__main__":
    CatchCCISignal()
    