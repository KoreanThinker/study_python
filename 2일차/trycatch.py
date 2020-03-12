# pass 는 아무것도 안할때

while True:
    try:
        float(input("숫자좀"))
        break
    except:
        pass


list_nums = ["12", "124", 123, 'hello', 'hi', "12", 4]

answer = []

for i in list_nums:
    try:
        answer.append(int(i))
        pass
    except:
        pass

print(answer)


try:
    list_nums.index(55)
except:
    print("없습니다")
