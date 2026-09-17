# Object Oriented Programming 

# is way to organising code around onjects
# An Object represents a real world entity that has 
# Attritubtes => data/properties => store data about an object
# Methods => behaviour/actions => function defined inside the class



class Student:
    pass

student1 = Student()


# Classes => is a blueprint 
# An Object is an acyual instance of created from that blueprint(class)

class Student:

# Constructor => Special method that is called when an object is created

#__init__ => special method that is called when an object is created(automatically called)
    def __init__(self,name,age):
        self.name =name
        self.age=age

    def set_name(self,name):
        self.name = name
    
    def introduce(self):
        print(f"Hello,I am {self.name} and I am {self.age} years old!")

student1 = Student("John",25)
student1.set_name("Jane") # Student.set_name("student1","Jane")
print(student1.name) 
student1.introduce()


#self => reference to the current instance of the class
#used to access variables and methods belong to the class
#not a keyword, you can call it whatever you like, but it has to be the first parameter of any function in the class
#used to access variables and methods belong to the class
#not a keyword, you can call it whatever you like, but it has to be the first parameter of any function in the class


# Instance Attribute vs Class Attribute

# Instance Attribute => belongs to the specific instance of the class
# Class Attribute => belongs to the class itself


class Student:
    # Class Attribute
    school="St Xavier"
    
    def __init__(self,name,age):
        # Instance Attribute
        self.name=name
        self.age=age
    

student1 = Student("John",25)
student2 = Student("Jane",23)

print(student1.name)
print(student2.name)
print(student1.school)
print(student2.school)
print(Student.school)



# Method Overiding 
# => means a class inherits methods from a parent class and you want to provide a specific implementation of that method in the child class.



class Animal:
    def sound(self):
        print("Animal make a sound")

# Access this from child class
    def legs(self):
        print("Animal has 4 legs")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()
# Calling parent class method
dog.legs()


# super() => used to access methods from parent class

class Person():
    def __init__(self,name):
        self.name = name

class Student(Person):

    def __str__(self):
        return f"Student Calling From Dunder method {self.name}"
        
    def __len__(self):
        return len(self.name)
        
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade


student1 = Student("John", "A")
print(student1.name)
print(student1.grade)
print(len(student1))
print(("Shahil Kataria from magic method"))


# Encapsulation => data and method implementation hidden from the user
# Implementation details hidden from the user
# Only the interface is visible to the user

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
      
    def get_balance(self):
        return self.__balance   
    


# name, _name,__name => 
# name => public
# _name => protected
# __name => private
account = BankAccount(1000)
print(account.get_balance())


# DUNDER.MAGIC METHODS

#special methods that start and end with double underscores 

#init
#__str__
#__len__
#__eq__
#__add__
#__add__


# Getter and setter 

class Student:

    def __init__(self,marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,value):

        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = value


student1 = Student(101)
print(student1.marks)
student1.marks = 95
print(student1.marks)   


student1.marks = 99




class Student:

    school = "Algocamp"
    def __init__(self,name):
        self.name = name
    
    @classmethod
    def change_school_name(cls,new_school_name):
        cls.school = new_school_name
        

Student.change_school_name("St Xavier")

student1 = Student("John")
print(student1.school)

# Static methods => utility methods inside a class for logical grouping

class MathUtils:

    @staticmethod
    def add(x,y):
        return x + y

print(MathUtils.add(1,2))

# class vs static method  vs __init__
# class method => first argument is class itself(  works with class attributes )
# static method => no special first argument (works with instance attributes)
#special method => __init__, __str__, __len__, etc. => called automatically (object data )

# __init__ => constructor, called when object is created
# __str__ => string representation of object, called when object is printed
# __len__ => length of object, called when len() is used
# __eq__ => equality comparison, called when == is used
# __add__ => addition, called when + is used


# DataClasses => help us to create classes mainly used for storing data 
from dataclasses import dataclass
# They reduce boilerplate code like writing ___init__ manually
@dataclass
class Person:
    name: str
    age: int
    country: str = "Gujarat"
    
person = Person("John", 25,"India")
person2 = Person("Jane", 25)
print(person)
print(person2)