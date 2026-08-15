from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Robot(Workable):
    def work(self):
        print("Robot can Work")


class Employee(Workable, Eatable):
    def work(self):
        print("Employee can work")

    def eat(self):
        print("Employee can eat")


e = Employee()
e.eat()
e.work()


r = Robot()
r.work() 