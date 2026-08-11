class A:
    def show(self):
        print("This is class A")

    def show2(self):
        print("This is class A")

    def show3(self):
        print("This is class A")


class B(A):

    def show3(self):
        print("This is show 3 of class B")


b_obj = B()

b_obj.show()
b_obj.show2()
b_obj.show3()
