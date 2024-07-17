import FinanceDataReader as fdr
import pymysql
from datetime import datetime, timedelta
import FinanceDataReader as fdr

# MariaDB 연결 설정
class CCIMonitor():
    def __init__(self):
        db_config = {
            'host': 'stocktrade.c14kwm840um7.us-east-1.rds.amazonaws.com',
            'user': 'root',
            'password': 'stocktraderootpwd',
            'database': 'stocktrade'
        }

        # 데이터베이스 연결
        # self.conn = mysql.connector.connect(**db_config)
        # self.cursor = self.conn.cursor()

        self.conn = pymysql.connect(host='stocktrade.c14kwm840um7.us-east-1.rds.amazonaws.com', 
                               user='root', 
                               password='stocktraderootpwd', 
                               db='stocktrade', 
                               charset='utf8', 
                               port=3306)
        self.cur = self.conn.cursor()

        # 종목 코드 리스트
        # self.stock_codes = ['000020', '000520', '000970', '001230', '001380', '001430', '001750', '001800', '001820', '001940', '002200', '002310', '003570', '003850', '004000', '004430', '004990', '006040', '006060', '006730', '007070', '007210', '007690', '008260', '008930', '009290', '009420', '010780', '011280', '013570', '013890', '014620', '015230', '016450', '016580', '017370', '017800', '017960', '018290', '018880', '019210', '020000', '023160', '027410', '030190', '032300', '033270', '033500', '035510', '035600', '039840', '044340', '046440', '049720', '051160', '051600', '052260', '052400', '054050', '054950', '065680', '066700', '067080', '067900', '073490', '079160', '080160', '081660', '082850', '084110', '084370', '089980', '092730', '093050', '093920', '094170', '095570', '095660', '100790', '104700', '105630', '108230', '108670', '109610', '111380', '111770', '120110', '122870', '123040', '126560', '138580', '139130', '183190', '192400', '200670', '206640', '206650', '214320', '214370', '243070', '251120', '259630', '264900', '271980', '284740', '285130', '290650', '294570', '294870', '298540', '307750', '317400', '319400', '344820', '357230', '361610', '375500', '376300', '377450', '382480', '417790', '445180', '460860', '472850']

        # KRX에 상장된 모든 종목 코드 가져오기
        krx = fdr.StockListing('KRX')
        self.stock_codes = krx['Code'].tolist()
        # 종목 코드와 종목명 출력
        # for index, row in krx.iterrows():
        #     print(f"종목 코드: {row['Code']}, 종목명: {row['Name']}")

    def insertEachData(self):
        print('insertEachData')
        # 데이터 가져올 기간 설정 (예: 최근 1년)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        # 각 종목에 대해 데이터 가져오기 및 저장
        for code in self.stock_codes:
            df = fdr.DataReader(code, start_date, end_date)
            
            i = 1
            for index, row in df.iterrows():
                self.cur.execute('''
                INSERT INTO stock_price_data (stock_code, date, open, high, low, close, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', (code, index.date(), float(row['Open']), float(row['High']), float(row['Low']), float(row['Close']), float(row['Volume'])))
                print('i = %s' % i)
                i += 1

                # 변경사항 저장 및 연결 종료
                self.conn.commit()
        self.cur.close()
        self.conn.close()

        print("데이터 저장이 완료되었습니다.")

if __name__ == "__main__":
    cm = CCIMonitor()
    cm.insertEachData()
