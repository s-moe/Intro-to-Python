# MY_CONSTANT = 5

# my_variable = "Hello World"

# print(MY_CONSTANT)
# print(my_variable)

# user_input = input("Who are you?")

# print(f"Hey there {user_input}")

# if/else
# num = 5

# if (num > 3):
#   print("num is greater than 3")
# elif (num > 1):
#   print("num is greater than 1")
# else:
#   print("num is 1 or less")

# while loop 

# counter = 0

# while (counter < 10):
#   print(counter)
#   counter += 1

# collections: arrays and objects are lists and dictionaries

# my_list = [1, 2, 3]
# print(my_list)
# print(my_list[0])

# my_dictionary = { "cheese": "gouda", "bread": "rye"}
# print(my_dictionary)
# print(my_dictionary["cheese"])

# functions

# def add_nums (x, y):
#   return x + y

# print(add_nums(2,5))

# counter = 0

# while (counter < 11):
#   if (counter % 2 == 0):
#     print(f"{counter} it's even")
#   if (counter % 3 == 0):
#     print("meow")
#   counter += 1


# Create Class
# class Dog:
#   pass
# # Instantiate class
# sparky = Dog()

# print(sparky)

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def bark(self):
    print(f"{self.name} barks")

sparky = Dog("Sparky", 4)

print(sparky)