from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

#조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

#전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()
print('조건검색 리스트 : %s \n\n' % conditions)

# 0번 조건식에 해당하는 리스트 얻기
condition_index = conditions[0][0]
condition_name = conditions[0][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print('0번째 조건식 명 : %s / 검색결과 : %s' % (condition_name,codes))