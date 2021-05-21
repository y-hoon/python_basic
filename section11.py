# Section11
# 파이쎤 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)

    # next => 첫번째 행을 통과 : 컬럼명(header)을 제외할 때
    next(reader)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    print()
    print()

    for c in reader:
        print(c)


# 예제2 - 구분자 지정 (delimiter)
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))

    print()
    print()

    for c in reader:
        print(c)


# 예제3 (Dict 변환) - header와 칼럼명을 딕셔너리로 만들어줌
# {'번호': '1', '이름': '김정수', '가입일시': '2017-01-19 11:30:00', '나이': '25'}
# {'번호': '2', '이름': '박민구', '가입일시': '2017-02-07 10:22:00', '나이': '35'}

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    # for c in reader:
    #     print(c)

    # 딕셔너리 출력
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-------------------')


# 예제4 ==> 파일에 쓸 때 newline이 2번 될때 1번만 되도록 옵션으로 처리 - newline=''
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


# 예제5 : 한번에 쓸때
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)


# XSL, XSLX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# 엑셀처리 library : openpyxl, xlsxwriter, xlrd, clwt, xlutils
# pandas 를 주로 사용 (openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname='시트명' 또는 숫자, header=숫자, skiprow=숫자 (skiprow는 해당 행은 제거하고 받는다.)
xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인 (5개)
print(xlsx.head())

# 하위 데이터 확인 (5개)
print(xlsx.tail())

# 데이터 확인, 행, 열
# (20, 7)
print(xlsx.shape)

# 엑셀  or CSV 다시 쓰기, index 옵션 => True (첫 열을 순번처리), False(첫 열을 순번처리안함)
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
