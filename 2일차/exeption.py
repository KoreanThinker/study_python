try:
    number = int(input("정수"))
    print("{}".format(number))
except ValueError as e:
    print("값 오류")
except Exception as e:
    if type(e) == ValueError:
        print(type(e))  # 실행안됨
    else:
        print("알수없는 오류")


raise IndexError("인덱스에러")
raise ValueError("값오류")
