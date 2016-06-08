import urllib.request
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ET
import os

class Data:
 
    key = 'a34c6423fa564664808bee03f48e1d27'
    url = "http://data.daegu.go.kr/hub/foodrtrt?&pIndex=1&Type=xml&pSize=50KEY=" + key


    def PrintMenu(self):
        

        print(" 대구시 맛집정보 ")
        print(" 1. 파일" )
        print(" 2. 전체 출력")

    def Choose(self, menu):
        if menu == '1':
            self.Fileset()
        elif menu == '2':
            self.PrintAll()
        else:
            print("다시 입력하세요")

    def Fileset(self):
        data = urllib.request.urlopen(self.url).read()
        f = open("foodrtrt.xml", "wb")
        f.write(data)
        f.close()

    def PrintAll(self):
        root = ET.parse("foodrtrt.xml").getroot()
        for a in root.findall('row'):
            print(a.findtext('GNG_CS'))
            print("근처 버스정류장 : ",a.findtext('BUS'))
            print(a.findtext('BZ_NM'))
            print(a.findtext('TLNO'))
            print(a.findtext('MBZ_HR'))
            print(a.findtext('SEAT_CNT'))
            print(a.findtext('PKPL'))
            print(a.findtext('MNU'))
            print(a.findtext('SMPL_DESC'))
            print('*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
            print('\n')
def main():
    data = Data()
    while(True):
        os.system('cls')
        data.PrintMenu()
        Keyvalue = str(input('메뉴 선택 : '))
        data.Choose(Keyvalue)
        input("")

if __name__ == "__main__":
    main()