"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    year = int(input("year"))
    month = int(input("month"))
    if month == 2:
        if year % 4 == 0 and year % 400 == 0 : #윤년
             print(29)
        elif year % 4 == 0 and year % 100 != 0 : #윤년
             print(29)
        else:
             print(28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
         print(30)
    else:
         print(31)
    return


if __name__ == '__main__':
    main()
