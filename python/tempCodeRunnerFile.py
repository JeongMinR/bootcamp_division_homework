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
