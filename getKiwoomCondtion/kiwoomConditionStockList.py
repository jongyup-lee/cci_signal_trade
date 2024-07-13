
from pykiwoom.kiwoom import *

class GetStockList():
    def __init__(self):
        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect(block=True)

        # 조건식을 PC로 다운로드
        self.kiwoom.GetConditionLoad()

        # 전체조건식 리스트 획득
        conditions = self.kiwoom.GetConditionNameList()

        #사용할 조건식 선별
        self.condition_index = conditions[0][0]
        self.condition_name = conditions[0][1]

        #self.stocks = fdr.StockListing('KRX')
        self.stockDict = {}  # 필터 조건을 만족한 종목 딕셔너리
        self.tmpStockDict = {}  # 종목별 dataframe을 한번만 수행하도록 담아두는 딕셔너리
        self.myStockDict = {}

        self.myKiwoomConditionStockList = []
        self.myHaveStockList = []
    
    def getConditionStocks(self):
        #해당 조건식으로 선별한 종목들 리스트
        codes = self.kiwoom.SendCondition('0101', self.condition_name, self.condition_index, 0)

        for code in codes:
            self.myKiwoomConditionStockList.append(code)
        
        return self.myKiwoomConditionStockList