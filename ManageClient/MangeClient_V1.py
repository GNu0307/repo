import csv


def start_information_idx():
    while True:
        print('뒤에 표시된 번호를 입력해주세요!')
        print('새로운 거래가 있나요?      [1]')
        print('기존 거래를 다시 볼래요?   [2]')
        print('거래 내용을 수정해 볼래요? [3]')

        idx = int(input('Number : '))
#        if idx > 0 and idx < 4: # 다음과 같은 수식을 변경가능
        if 0 < idx < 4:
            break
        else:
            print('아직 개발중이에요... 위에 표시된것만 입력해 줄래요?')
            pass
    return idx


def insert_data(old_num):

    # new_data = ['num', 'date', 'company_name', 'income', 'product', 'memo', 'tax']
    while True:
        date = input('거래 날짜 (년도포함 숫자 8개) :')
        company_name = input('상호명 :')
        income = input('거래 단가 : ')
        product = input('거래 내용 : ')
        memo = input('비고 : ')
        tax = input('거래 방식(세금) : ')

        confirm = input('위 내용이 맞아요? [y,n] : ')
        if str(confirm) == 'y':
            # new_date value update
            num = int(old_num) + 1
            break
        elif str(confirm) == 'n':
            print('에고, 다시 작성해줄래요?\n')
            pass
        else:
            print('미안해요, 맞으면 y, 틀리면 n 만 입력할 수 있어요.\n')
            pass

    new_data = [num, date, company_name, income, product, memo, tax]
    print("이번 거래는 번호는 {}로 저장했어요!".format(num))
    return new_data


def store_data_csv(new_data):
    with open('ContactBook.csv', 'a', encoding='utf-8', newline='') as file:
    # with open('ContactBook.csv', 'a', encoding='utf-8') as file:
    # newline을 추가하지 않으면, 기존 행에 데이터가 추가됨. 새 row에 데이터를 넣으러면 newline을 넣어야 함.

        a = csv.writer(file, lineterminator="\n")
       #a = csv.writer(file)
       # 그냥 추가하면 빈칸이 생겨서 ㅠ 문제가 생김.
        a.writerow(new_data)
        print("저장했어요!!! 대단해 우리마누라♥")


def read_data_csv():
    with open('ContactBook.csv', 'r', encoding='utf-8') as file:
        r = csv.reader(file)
        for line in r:
            print(line)


def get_contract_num():
    # 저장된 마지막 거래번호 조회
    with open('ContactBook.csv', 'r', encoding='utf-8') as file:
        r = csv.reader(file)
        for line in r:
            pass
        return line[0] # 거래번호 Idx

def correct_data_csv_confirm(num):
    # 수정할 데이터 확인
    with open('ContactBook.csv', 'r', encoding='utf-8') as file:
        r = csv.reader(file)
        for line in num:
            pass
        print(line)
        return line # 전체 내용 확인


def correct_data_csv(num):
    # 저장된 데이터 확인
    with open('ContactBook.csv', 'w', encoding='utf-8',) as file:
        w = csv.writer(file, lineterminator="\n")



def main():

    print('eho!')
    # What To DO
    idx = start_information_idx()
    # insert New Valid Data
    if idx == 1:
        num = get_contract_num()
        new_data = insert_data(num)
        store_data_csv(new_data)
    elif idx == 2:
        read_data_csv()
    elif idx == 3:
        num = input('수정할 거래 번호 입력 : ')
        correct_data_csv(num)




try:
    while True:
        main()
except KeyboardInterrupt:
        print("Bye-Bye!")
        exit()
# 프로그램 실행시 Ctrl + C 입력하면 중간에 빠져나올 수 있는 코드

# 빈 파일에 추가될 때는 기존 거래 번호를 읽을 수 없어서 문제가 될수 있음, 예외처리가 필요