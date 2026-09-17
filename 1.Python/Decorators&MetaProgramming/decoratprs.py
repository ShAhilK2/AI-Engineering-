

# First Class Function 
# Function are first class objects.

def greet():
    return "Hello"
message = greet()
print(message)



def shout(text):
    return text.upper()

def process(func,value):
    return func(value)


print(process(shout,"Hello"))


def outer():
    def inner():
        print("Inside Inner Function")

    return inner


# calling outer function
func = outer()

# calling inner function
func()




# Decoratpr => a decorator is a function that takes another function,add extra behaviour and 
# then return a new function 


def my_decorator(func):
    def wrapper(*args,**kwargs): # *args and **kwargs allow the wrapper to accept any number of positional and keyword arguments.
        print("Before calling that functions")
        result = func(*args,**kwargs)
        print("After calling that functions")
        return result
    return wrapper


@my_decorator
def add(a,b):
    return a+b


@my_decorator
def say_hello():
    print("Hello from function i am working")


# my_decorated_function = my_decorator(say_hello)
# my_decorated_function()


say_hello()
print(add(5,3))

def log_function(func):
    def wrapper(*args,**kwargs): # *args and **kwargs allow the wrapper to accept any number of positional and keyword arguments.
        print("Calling Function : ",func.__name__)
        result = func(*args,**kwargs)
        print("Finished Function : ",func.__name__)
        return result
    return wrapper


@log_function
def add(a,b):
    return a+b


print(add(5,3))



# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"Time taken by {func.__name__} is {end - start} seconds")
#         return result
#     return wrapper
        
# @timer
# def slow_function():
#     time.sleep(2)
#     print("Function completed")
#     return "Done"
    
# print(slow_function())




from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@my_decorator
def say_hello():
    '''This function greet the user'''
    print("Hello")
    
say_hello()

print(say_hello.__name__)
print(say_hello.__doc__)


# Class decorators is a function it takes a class ,modifies it and return it

def add_greeting(cls):
    cls.greet = lambda self: "Hello from decorated class"
    return cls


@add_greeting
class Student:
    def __init__(self,name):
        self.name = name



student = Student("Shahil")
print(student.name)
print(student.greet())


# Instrospection => inspecting objects at runtime 

# python allows  us to check what attributes and methods an object has


class Student:
    school ="Algocamp"

    def __init__(self,name):
        self.name = name

    def introduce(self):
         print(f"Hi I am {self.name} from {self.school}")

student = Student("Shahil")
student.introduce()

print(dir(student))
print(getattr(student,'name'))
print(getattr(student,'age',"age not found"))
print(setattr(student,'age',25))


print(student.age)

print(hasattr(student,'age'))
print(hasattr(student,'marks'))