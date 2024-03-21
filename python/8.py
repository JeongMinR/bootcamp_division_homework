"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 이곳에 코드를 작성해주세요!
    number = int(input())
    s = 0
    total = 1
    for n in range(1,(number +1)):
      s += n
      total = total* n 
    print (s)
    print (total)

    return


if __name__ == '__main__':
    main()
