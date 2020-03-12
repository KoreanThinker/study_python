class Student:
    def __init__(self, val):
        self.__val = val
        print("객체생성")

    def __del__(self):
        print(self.__val)

    def __str__(self):
        return self.__val

    @property
    def val(self):
        print("val 호출")
        return self.val2

    @val.setter
    def val(self, val):
        print("val 변경")
        if val < 0:
            raise Exception("음수 X")
        self.__val = val


st = Student("안녕")
# st2 = Student(45)
# st2.__val = "5"
st.val = -100

# print(str(st))
# print(str(st2))
