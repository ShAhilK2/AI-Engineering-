

file = open("notes.txt","r")

print(file.readline())
file.close()

file = open("notes.txt","a")


file.write("\n Hello Python \n")


file.close()



# "r" => read
# "w" => write
# "a" => append
# "x" => create
# "rb" => read binary
# "wb" => write binary


#  for photo and videos 
# file = open("photo.png","rb")
# data= file.read()
# file.close()


# with statements automatically closes after the file use


with open("notes.txt","r",encoding="utf-8") as file:
    content = file.read()

print(content)



with open("notes.txt","w",encoding="utf-8") as file:
    file.write("Learning File I/O in python")



# Now read the file again to see the changes
with open("notes.txt","r",encoding="utf-8") as file:
    content = file.read()

print(content)


# os.path  =>  helps to work with file paths

import os

path="notes.txt"

print(os.path.exists(path))


print(os.path.abspath(path))



file_paths = os.path.join("data","notes.txt")
print(file_paths)

# pathlib => modern and cleaner way to work with file paths in python 
# it treats path like objects ,so the code becomes easier to understand
from pathlib import Path
path = Path("notes.txt")
print(path) 

print(path.exists())
print(path.absolute())
content = path.read_text(encoding="utf-8")
print(content)




# Standard Streams => Python has three standard streams that hadle input ,output and errors

# stdin => standard input stream
# stdout => standard output stream
# stderr => standard error stream


# name = input("Enter the name")
# print(name)


import sys
# data = sys.stdin.readlines()
# print(data)



#stdout
print("Hello World", file=sys.stdout)
sys.stdout.write("Hello World from stdout\n")

#stderr
sys.stderr.write("Hello World from stderr\n")



# Serialization => converting python data into a format that can be saved in a file or
# transferred over a network


import json

student = {
    "name": "shahil",
    "age": 25,
    "city": "Delhi"
}


# json => readable format for humans
# csv => comma separated values(excel format(tabular data))
# pickle => binary format for python objects

# Convert python object to json
json_data = json.dumps(student)
print(json_data)

# Convert json to python object
python_data = json.loads(json_data)
print(python_data)


with open("notes.json","w",encoding="utf-8") as file:
    json.dump(student,file)


with open("notes.json","r",encoding="utf-8") as file:
   data = json.load(file)
   print(data)


# csv
#name,age,city
#shahil,25,Delhi

import csv 

students = [
    ["name","age","city"],
    ["shahil",25,"Delhi"]
]


# newline="" => removes empty line between rows
with open("students.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file) # writer object means we can write rows
    writer.writerows(students) # write rows



with open("students.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file) # reader object means we can read rows
    for row in reader:
        print(row)


# dictwriter

#pickle

student = {
    "name" :"shahil",
    "age" : 25
}
import pickle
with open("notes.pkl","wb") as file:
    pickle.dump(student,file)

with open("notes.pkl","rb") as file:
    data = pickle.load(file)
    print(data)
