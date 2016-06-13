import urllib.request
import xml.etree.ElementTree as etree

def main():

    #서울공공데이터사용
    key = 'a34c6423fa564664808bee03f48e1d27&pIndex=1&Type=xml&pSize=50'
    url = "http://data.daegu.go.kr/hub/foodrtrt?KEY=" + key

    data = urllib.request.urlopen(url).read()

    filename = "daegu.xml"
    f = open(filename, "wb") #다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    #파싱하기
    tree = etree.parse(filename)
    root = tree.getroot()

    for a in root.findall('row'):
        print(a.findtext('BUS'))
        print('----------------------')

if __name__ == "__main__":
    main()
