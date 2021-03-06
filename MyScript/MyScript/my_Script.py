# -*- coding:utf-8 -*-
import urllib.request
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ET
import os
import webbrowser
import mimetypes
import mysmtplib

from email.mime.base import MIMEBase
from email.mime.text import MIMEText

class Data:
    fileName = "foodrtrt.xml"
 
    key = 'a34c6423fa564664808bee03f48e1d27'
    url = "http://data.daegu.go.kr/hub/foodrtrt?&pIndex=1&Type=xml&pSize=50KEY=" + key


    def PrintMenu(self):
        print("\n")
        print(" 대구시 맛집정보 ")
        print("\n")
        print(" 1. 음식 분류별 검색" )
        print(" 2. 구군별 검색")
        print(" 3. 이메일 보내기")
        print(" 4. 다음으로 검색")
        print(" 5. 위치 검색")
        print(" 0. 종료")
        print("\n")

    def Choose(self, menu):
        os.system('cls')
        if menu == '1':
            self.PrintWhat()
        elif menu == '2':
            self.PrintWhere()
        elif menu == '3':
            self.SendEmail()
        elif menu == '4':
            self.SearchDaum()
        elif menu == '5':
            self.SearchMap()
        elif menu == '0':
            self.Exit()
        else:
            print("다시 입력하세요")

    def Exit(self):
        exit()

    def PrintWhat(self):
        os.system('cls')
        What = str(input('\n'+'음식 분류(한식, 중식, 양식, 일식, 세계요리) : '))
        root = ET.parse("foodrtrt.xml").getroot()
        for a in root.findall('row'):
            if(str(a.findtext('FD_CS')) == What):
                print('*=' * 55)
                print("구군 분류       : ",a.findtext('GNG_CS'))
                print("근처 버스정류장 : ",a.findtext('BUS'))
                print("업소명          : ",a.findtext('BZ_NM'))
                print("전화번호        : ",a.findtext('TLNO'))
                print("영업시간        : ",a.findtext('MBZ_HR'))
                #print("메뉴            : ",a.findtext('MNU'))
                #print("간단 설명       : ",a.findtext('SMPL_DESC'))
                print("지하철          : ", a.findtext('SBW'))
                print("음식분류        : ", a.findtext('FD_CS'))
                print('*=' * 55)
                print('\n')

    def PrintWhere(self):
        os.system('cls')
        Where = str(input(' 구군 입력(서구, 북구, 수성구, 중구) : ' ))
        root = ET.parse("foodrtrt.xml").getroot()
        for a in root.findall('row'):
            if(str(a.findtext('GNG_CS')) == Where):
                print('*=' * 55)
                print("구군 분류       : ",a.findtext('GNG_CS'))
                print("근처 버스정류장 : ",a.findtext('BUS'))
                print("업소명          : ",a.findtext('BZ_NM'))
                print("전화번호        : ",a.findtext('TLNO'))
                print("영업시간        : ",a.findtext('MBZ_HR'))
                #print("메뉴            : ",a.findtext('MNU'))
                #print("간단 설명       : ",a.findtext('SMPL_DESC'))
                print("지하철          : ", a.findtext('SBW'))
                print("음식분류        : ", a.findtext('FD_CS'))
                print('*=' * 55)
                print('\n')


    def SearchMap(self):
        os.system('cls')
        MAP = str(input("검색어를 입력하세요 : "))
        url ="https://www.google.co.kr/maps/place/"+MAP
        webbrowser.open_new(url)

    def SearchDaum(self):
        os.system('cls')
        SFW = str(input("검색어를 입력하세요 : "))
        url ="http://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q="+SFW
        webbrowser.open_new(url)
            
    def SendEmail(self):
        os.system('cls')
        #global value
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "foodrtrt.xml"

        senderAddr = "acuer93@gmail.com"     # 보내는 사람 email 주소.
        recipientAddr = " "
        recipientAddr = str(input("메일 주소를 입력하세요 : "))

        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "스크립트 텀프로젝트 테스트 메일"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        # MIME 문서를 생성합니다.
        htmlFD = open(htmlFileName, 'rb')
        HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
        htmlFD.close()

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(HtmlPart)
        print("\n")
        print("******메일을 보내는 중입니다******")
        print("\n")
        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("acuer93@gmail.com","roslal12")
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        print("******메일 전송 완료******")
        s.close()




    #파싱하기
    #tree = etree.parse(filename)
    #root = tree.getroot()

def main():
    data = Data()
    while(True):
        data.PrintMenu()
        Keyvalue = str(input('메뉴 선택 : '))
        data.Choose(Keyvalue)

        

if __name__ == "__main__":
    main()