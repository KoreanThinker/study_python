try:
    # number = int(input("> 정수입력"))
    # print("{}".format(number))
    print("기본")
except:
    print("예외")
finally:
    print("무조건")


while True:
    file = open('test.txt', 'a')
    try:
        ans = int(input())
        file.write(str(ans))
    except:
        break
    finally:
        file.close()
