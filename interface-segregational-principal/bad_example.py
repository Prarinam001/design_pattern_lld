from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Worker(Employee):
    def work(self):
        print("Worker can work")

    def eat(self):
        print("Worker can eat")

class Robot(Employee):
    def work(self):
        print("Robot can work")

    def eat(self):
        raise Exception("Robot cannot eat")


robot = Robot()
robot.work()
robot.eat()  # This will raise an exception

