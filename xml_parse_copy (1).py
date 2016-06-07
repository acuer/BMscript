import urllib.request
import xml.etree.ElementTree as etree

def main():

    #서울공공데이터사용
    key = 'yourKey'
    url = "http://openAPI.seoul.go.kr:8088/%s/xml/SJWPerform/1/5" % key

    data = urllib.request.urlopen(url).read()

    filename = "sample2.xml"
    f = open(filename, "wb") #다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    #파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()

    for a in root.findall('row'):
        print(a.findtext('TITLE'))
        print(a.findtext('START_DATE'))
        print(a.findtext('PLACE_NAME'))
        print(a.findtext('TICKET_INFO'))
        print('----------------------')

if __name__ == "__main__":
    main()