from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

'''
GetThemeGroupList
GetThemeGroupList 메소드는 테마그룹명과 각 테마그룹에 대한 아이디 값을 얻을 수 있습니다.
{'2차전지_소재(양극화물질등)': '141',
 '2차전지_완제품': '140',
 'AMOLED_소재': '571',
 'AMOLED_장비': '570',
 'Cheap-Chic_저가실용품': '830',
 'FPCB(연성회로기판)': '501',
 'LCD_부품': '562',
 'LCD_소재': '561',
 'LCD_장비': '560',
 'LED': '572',
 'LPG(액화석유가스)': '600',
 'PCB(인쇄회로기판)': '500',.....기타 등등
'''

group = kiwoom.GetThemeGroupList(1)
pprint.pprint(group)