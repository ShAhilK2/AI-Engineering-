
# map()=> applies a function to every item in an iterable

numbers =[1,2,3,4,5]
def square(x):
    return x*x

result = map(square,numbers)
print(list(result))

# Using Lambda Function
sqaures = map(lambda x :x*x,numbers)
print(list(sqaures))


# Filter => it keeps only the items that return True from the function

numbers =[1,2,3,4,5,6,7,8,9,10]

def is_even(x):
    return x%2 == 0

even_numbers = filter(is_even,numbers)
print(list(even_numbers))

# Using Lambda Function
even_numbers = filter(lambda x : x%2 == 0,numbers)
print(list(even_numbers))


# reduce : combine the value at a single value
from functools import reduce

numbers =[1,2,3,4,5]

def add(x,y):
    return x+y

sum = reduce(add,numbers)
print(sum)

# Using Lambda Function
sum = reduce(lambda x,y : x+y,numbers)
produce = reduce(lambda x,y : x*y,numbers)
print("Sum ",sum)
print("Product ",produce)



# Functional Programmmming 
# functions can be 
# stored in variables 
# passed as arguments
#  returnes from another functions
#  used inside data transformations


def square(x):
    return x*x  

operation = square(3)
print(operation)



# HOF (Higher Order Functions)
# functions that take other functions as arguments
# or return functions as results


def apply_operation(func,value):
    return func(value)

def sq(x):
    return x*x


print(apply_operation(sq,5))
    


# Closures => A closure is when an inner function remembers and carries access to its outer function's variables even after the outer function has finished executing.


# First take factor as argument then number as argument
def multipler(factor):

    # inner function 
    def multiply(number):
        print("factor is ",factor)
        print("number is ",number)

        return number * factor
    
    # calling inner function or returning it
    return multiply


double = multipler(2)
print(double(5))

triple = multipler(3)
print(triple(5))



# functools provides tools for working  with functions 
# reduce,partial,lru_cache,wraps

from functools import partial, lru_cache
# partials lets us create a new function by fixing some arguments of an existing function 


def power(base,exponent):
    return base**exponent


# Create a new function that always uses 2 as the exponent
square = partial(power, exponent=2)
cube = partial(power,exponent=3)

print("Squares:",square(5))  # Output: 25
print("Squares:",square(6))  # Output: 36
print("Cubes:",cube(5))    # Output: 125




# itertools provides efficient tools for working with iterators
# chain()

# chain()=>combines multiple iterators into one sequence

from itertools import chain 
list1=[1,2,3]
list2=[4,5,6]
combined = chain(list1,list2)
print(list(combined))

# combinations()=> gives possible selections using repeating order 
from itertools import combinations
numbers=["A","B","C"]
combinations_result = combinations(numbers,2)
print(list(combinations_result))
