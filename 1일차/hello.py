# 모르던 문법들


# 가변 매개변수
def func(a, b, c=5, *d):
    print(a, b)
    print(c)
    print(d)


# func(1, 2, 3, 4, 7, 8, 9, 1, 2, 3)
# func(1, 2, 3)
# func(1, 2)
# func(1, 3, d='asdf') 오류
# func(1, 2, 3, 4, a=122, b=244) 오류


# global
value = 0


def fibo(n):
    global value
    value += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# print(fibo(10))


# tuple
a, b = divmod(15, 4)
# print(a, b)
# print(type(a))
di = {
    (0, 0): 14,
    (2, 2): 15
}
# print(di[2, 2])


# file

# file = open("test2.txt", "w", encoding="utf8")
file = open("test.txt", "a", encoding="utf8")
file.write("안녕1")
file.close()

file = open('test.txt', "r", encoding="utf8")
# print(file.read())
file.close()

with open("test.txt", "a") as file:
    file.write("asd2424f")


def func():
    print("a")
    yield 123
    print("b")
    yield 2
    print("c")
    yield 3


# next(func())
# next(func())
# next(func())
# next(func())

gen = func()
# next(gen)
# next(gen)
# next(gen)
# next(gen)

for i in gen:
    print(i)
