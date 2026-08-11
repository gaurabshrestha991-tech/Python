class A:
    # Parent / Superclass
    def show(self):
        print("This is class A")

    def show2(self):
        print("This is class A")

    def show3(self):
        print("This is class A")


class B(A):
    # Child / Subclass
    pass


b_obj = B()

b_obj.show()
b_obj.show2()
b_obj.show3()


# Multiple Inheritance

class Fly:

    def fly(self):
        print("Player can fly")


class Jump:

    def jump(self):
        print("Player can jump")


class Swim:

    def swim(self):
        print("Player can swim")


class Player(Fly, Jump, Swim):
    pass


player = Player()

player.fly()
player.jump()
player.swim()
