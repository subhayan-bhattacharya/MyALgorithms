#!/usr/bin/python3

# Testing for a decimal string

# Potentially infinite loop until user gets the answer right!

while True:
    age = input("Enter your age: ")
    if age.isdecimal():
        break
    print("age should be an integer, try again!")

print(age)

