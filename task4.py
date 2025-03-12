class family:
    def parent(self):
        print("This is the Parent class")


class Child1(family):
    def see_info(self):
        print("This is the Child1")


class Child2(Child1):
    def see_info1(self):
        print("This is the Child2")


obj1 = Child1()
obj2 = Child2()


obj1.parent()      
obj1.see_info()  

obj2.parent()      
obj2.see_info1() 
