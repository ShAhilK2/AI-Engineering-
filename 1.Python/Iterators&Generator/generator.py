# Generators : are a simple way to create iterators

def count_upto(limit):
    current = 1

    while current <=limit:
        yield current
        current +=1

for num in count_upto(5):
    print(num)

def simple_generator():
    # yield means "produce" a value and pause execution after each yield what comes after yield will be executed when the generator is called again

    # memory efficient
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))


# Anoymoues function
square = lambda x: x * x
print(square(5))

# what is below called? List comprehension
numbers = [x*x for x in range(20)]
print(numbers)


# Generator are memory efficient and use yield instead of return
# They produce items one at a time and only when requested
# They are lazy evaluated
# They are used to generate a sequence of values
# They are used when you have a large dataset and you don't want to load all the data into memory
# They are used when you want to produce values on-demand
# They are used when you want to create an infinite sequence
def square_generator(n):
    for i in range(n):
        yield i * i

squares = square_generator(5)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# Generator Expressions 

sqaures = [x *x for x in range(20)]
print(sqaures)

squares_gen = (x *x for x in range(20))
print(squares_gen)
print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))

