import csv

dict = {'key': 'A', 'value': '1'}
print(dict.items())

with open('csv_tesx.csv', 'w', encoding='utf-8', newline='') as file:
    w = csv.writer(file)
    for key, val in dict.items():
        w.writerow([key, val])

# csv.writer(file) : CSV file에 쓰는 CSV Class Type으로 받은 후 writerow 함수를 이용해 데이터를 씀.
# 참고 URL : http://pythonstudy.xyz/python/article/207-CSV-%ED%8C%8C%EC%9D%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0,  https://pythonspot.com/save-a-dictionary-to-a-file/
header = ['num', 'date', 'name', 'income']
newdata = ['1', ' 181212', 'A', '200']
newdata2 = ['2', ' 181214', 'A', '500']

with open('book.csv', 'w', encoding='utf-8', newline='') as file:
    w = csv.writer(file)
    w.writerow(header)
    w.writerow(newdata)

# writerow를 순차적으로 사용할 경우 기존 데이터에 Append 한다.

with open('book.csv', encoding='utf-8', newline='') as file:

    r = csv.reader(file)
#    print(r.line_num)
    for line in r:
        pass
        #print(line)
    print(r.line_num)
#전체 내용을 읽을수도 있지만!
#난 마지막을 읽어서 해당 값이 얼만지 알고싶어!
#꼭 다읽어야하니? ㅠㅠ 방법은 나중에 찾고.... 다 읽어보고 판단해야겠네?
# 문자 스트립 및 여백 제거 이유 : http://statkclee.github.io/web-data-python/02-csv.html
# CSV 관련 Doc : https://docs.python.org/3/library/csv.html
    print(r)
    print(line)
# for문써서 한번 읽으면 (어차피 읽어야 한다면 마지막 라인 데이터가 line에 들어가 있음

    num = line[0]
    newdata2[0] = str(int(num)+1)
    print(newdata2)

    for line in r:
        print(line)

# read write를 한파일에서 할순 없고 file open을 나눠서 해줘야하는걸까?

with open('book.csv', 'a', encoding='utf-8', newline='') as file: # 'a' option append
    w = csv.writer(file)
    w.writerow(newdata2)

# 하지만 이렇게 쓰면 기존에 있던 데이터에 append 되는 것이 아니라 새로운 라인에 새로 써버림.... ㅠ  기존라인을 살리고 더할순 없을까? file open 옵션에서 'a' append를 사용하자!
# 이런 기본 펑션들 댜큐는 어디서 찾을 수 있는 것일까?





