# iterables => any  object can be looped over using a for loop
numbers = [1,2,3,4,5]
name ="Python"

student = {"name":"shahil","age":24}



for item in numbers:
    print(item)


# Exmples are
# list 
# tuple
# set
# dict
# string

# All of these are iterables

# iterables vs iterators 

# iterables are objects that can be looped over
# iterators are actual objects that can be iterated over using next() function


numbers = [1,2,4,5]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# ___iter__()= > return the iterator object itself
# __next__()= > return the next item from the iterator

numbers = [1,2,4,5]
iterator = iter(numbers)

print(iterator.__next__())
print(iterator.__next__())



# Stop iterators
# When the iterator is exhausted, it raises a StopIteration exception

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# iterables are converted to iterators using iter() function
# iterators are objects that can be iterated over using next() function

# iterator = iter(iterable)
# next(iterator)





