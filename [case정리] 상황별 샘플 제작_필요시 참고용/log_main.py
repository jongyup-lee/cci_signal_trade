from log_import import Logging

class LogMain():
    def __init__(self) -> None:
        self.logger = Logging()

    def writeLog(self):
        self.wlog = self.logger.setLogging('info', '장시작/종료 실시간 요청')

if __name__ == "__main__":
    lgm = LogMain()
    lgm.writeLog()