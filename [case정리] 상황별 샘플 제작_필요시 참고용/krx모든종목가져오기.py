import FinanceDataReader as fdr

# KRX 상장 종목 전체 목록 가져오기
krx = fdr.StockListing('KRX')

# 종목 코드만 추출
stock_codes = krx['Symbol'].tolist()

# 결과 출력
print(f"총 {len(stock_codes)}개의 종목 코드를 가져왔습니다.")
print("처음 10개 종목 코드:", stock_codes[:10])