# Type hints
# Type hints allows us to maintain the expected type of variables, function parameters, and return values

# Python is still dynamically types,so type hints do not enforce types of runtime by default


def greet(name: str) -> str:
    return f"hello, {name}"

message = greet("Shahil")
print(message)

name: str ="Shahil"
age : int = 23
height : float = 5.9
is_student : bool = True


marks: int = "ninety"


def add(a:int,b:int)->int:
    return a+b

result = add(10,20)
print(result)


def print_message(message:str)->None:
    print(f"Hello, World {message}")

print_message("Shahil") 


# The Typing module

#provides many useful types for wriing better type hints

from typing import Optional,Union,Any,TypedDict

# Generics : list[T]

# Generics allows us to maintain what type of data a collection contains

numbers : list[int] = [1,2,3,4,5]
names : list[str] = ["Alice","Bob","Charlie"]


def total_cars(number : list[int]) -> int:
    return sum(number)

print(total_cars([10,20,30]))



# Generics : dict[k,v]

user: dict[str,str] = {"name":"Shahil","age":"23"}


marks: dict[str,int] = {"maths" : 40,"science" : 40}


coordinates : tuple[int,int] = (10,20)
unique_numbers : set[int] = {1,2,3,4,5}


def print_scores(scores : dict[str,int]) -> None:
    for subject, score in scores.items():
        print(f"{subject}: {score}")


print_scores(marks)


# Optional is used when a value can either be of a specific type or None
from typing import Optional

def find_user(user_id:int)->Optional[str]:
    if user_id ==1:
        return "Shahil"
    return None

def find_user(user_id:int)-> str | None:
    if user_id ==1:
        return "Shahil"
    return None


print(find_user(1))
print(find_user(2))



# Union is used when a value can .be one of the multiple types

from typing import Union 
def format_id(user_id: Union[int,str])->str:
    return f"User ID: {user_id}"
def format_id(user_id: int | str)->str:
    return f"User ID: {user_id}"

print(format_id(123))
print(format_id("abc"))


# Any means value can be of any type 
from typing import Any

def print_value(value :any)->None:
    print(value)


data : Any = "Python"
print_value(data)
print_value(123)


# TypedDict : is used to define the expected structure of a dictionary 

from typing import TypedDict

class Student(TypedDict):
    name: str
    age : int
    city : str

student : Student = {
    "name" : "Shahil",
    "age" : 23,
    "city" : "Delhi"
}


def print_student(student: Student)->None:
    print(student["name"])
    print(student["age"])
    print(student["city"])

print_student(student)


# Protocol is used to define the expected behaviour insisted of exact class inheritance
from typing import Protocol 

class Drawable(Protocol):
    def draw(self) -> None:
        ...


class Circle():
    def draw(self) -> None:
       print("Drawing Circle")


class Square():
    def draw(self) -> None:
        print("Drawing Square")
 

  
# can i pass Drawable Class as parameter? Yes
def render(shape:Drawable)->None:
    shape.draw()    

render(Circle())
render(Square())

