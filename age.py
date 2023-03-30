class Person:
    def age(a = 0):
        a = 60
        return a
class P1(Person):
    def age(z=0):
        z = 10
        return z
class P2(Person):
    def age(y=0):
        y = 20
        return y
def great(x1 , x2):
    if x1.age() < x2.age():
        print("Person one is smaller")
    else:
        print("Person two is smaller")
l = []
o1 = P1()
o2 = P2()
great(o1,o2)