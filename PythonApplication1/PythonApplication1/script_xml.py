# -*- coding:utf-8 -*-
import urllib.request
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as ET
import os
import mimetypes
import mysmtplib

from email.mime.base import MIMEBase
from email.mime.text import MIMEText

class Data:
    fileName = "foodrtrt.xml"
 
    key = 'a34c6423fa564664808bee03f48e1d27'
    url = "http://data.daegu.go.kr/hub/foodrtrt?&pIndex=1&Type=xml&pSize=50KEY=" + key


    def PrintMenu(self):
        print(" 대구시 맛집정보 ")
        print(" 1. 파일" )
        print(" 2. 전체 출력")
        print(" 3. 이메일 보내기")

    def Choose(self, menu):
        if menu == '1':
            self.Fileset()
        elif menu == '2':
            self.PrintAll()
        elif menu == '3':
            self.SendEmail()
        else:
            print("다시 입력하세요")

    def Fileset(self):
        data = urllib.request.urlopen(self.url).read()
        f = open("foodrtrt.xml", "wb")
        f.write(data)
        f.close()

    def PrintAll(self):
        root = ET.parse("foodrtrt.xml").getroot()
        for a in root.findall('\trow'):
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

    def SendEmail(self):
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"

        senderAddr = "acuer93@gmail.com"     # 보내는 사람 email 주소.
        recipientAddr = " "   # 받는 사람 email 주소.

        recipientAddr = str(input ('받을 사람 Mail주소를 입력해주세요 : '))

        msg = MIMEText(_text, _charset= 'utf8')
        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "\n"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        # MIME 문서를 생성합니다.
        htmlFD = open(self.fileName, 'rb')
        HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
        htmlFD.close()

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(HtmlPart)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("acuer93@gmail.com","roslal12")
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        s.close()


    #파싱하기
    #tree = etree.parse(filename)
    #root = tree.getroot()

def main():
    data = Data()
    while(True):
        os.system('cls')
        data.PrintMenu()
        Keyvalue = str(input('메뉴 선택 : '))
        data.Choose(Keyvalue)
        

if __name__ == "__main__":
    main()