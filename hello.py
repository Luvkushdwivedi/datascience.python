# operators
# 
# x = 5
# print(x, type(x))
# x = "hello world"
# print(x, type(x))
# x = 20
# print(x, type(x))
# x = 20.5
# print(x, type(x))
# x = 1
# print(x, type(x))
# x = ("apple" "banana" "cherry")
# print(x, type(x))
# x = range(6)
# print(x, type(x))
# x = {"name": "john", "age": 36}
# print(x, type(x))
# x = {"apple" "banana" "cherry"}
# print(x, type(x))
# x = frozenset({"apple" "banana" "cherry"})
# print(x, type(x))
# x = True
# print(x, type(x))
# x = b"hello"
# print(x, type(x))
# x = bytearray(5)
# print(x, type(x))
# x = memoryview(bytes(5))
# print(x, type(x))
# x = None
# print(x, type(x))

# print("10 + 2=", 10 + 2)
# print("10 - 2=", 10 - 2)
# print("10 * 2=", 10 * 2)
# print("10 / 2=", 10 / 2)
# print("10 % 2=", 10 % 2)
# print("9  %  5=", 9 % 5)
# print("10 // 3=", 10 // 2)
# print("2** 3=", 2 ** 3)

# print("5 %  3=", 5 % 3)
# print("-5 %  -3=", -5 % -3)

# x = 5
# print(x)
# x += 3
# print(x)
# x -= 2
# print(x)
# x *= 3
# print(x)
# x /= 2
# print(x)
# x //= 3
# print(x)
# x **= 2
# print(x)
# x = 5
# x %= 3
# print(x)
# x |= 2
# print(x)
# x ^= 3
# print(x)

# a = 10
# b = 20

# print("a==b:", a==b)
# print("a== 10:", a == 10)

# print("a != b:", a != b)
# print("a != 10", a != 10)

# print("a>b:", a > b)
# print("a < b", a<b)

# print("a <= b:", a <= b)
# print("a >= b:", a >= b)
# print("a >= 10:", a >= 10)


# x = 3

# print(x < 5 and x < 10)
# print(x < 5 or x < 4)
# print(not(x < 5 and x < 10))

# y = 3 #4

# print(x is y)
# print(x is not y)

# x = ["Maruti", "BMW"]
# Y = ["Maruti", "BMW"]
# print (x is Y)

# print("maruti"in x)
# print("maruti" not in x )

# print("maruti" in x)
# print("maruti" not in x)

# x = 10
# y = 20

# print (x & y)
# print(x | y)
# print(x ^ y)
# print(~x)
# print(~y)
# print(x << 2)
# print(y << 2)
# print(x >> 2)
# print(y >> 2)

# name = input("Enter your name:")
# print("Hello", name)
# age = input("please enter your age :")
# print("Hello", name, "you are", age , "year old")
# phone = input("please enter your phone number:")
# print("contact number", phone)


# x = input(" enter first value for sum:")
# y = input("enter second value for sum:")
# z = int(x) * int(y)    #(typecasting)
#  print("sum:" , z)


# x =int(input(" enter first value for sum:"))   #int ploating is working AS A TYPECASTING
# y =int(input("enter second value for sum:"))    #int ploating is working AS A TYPECASTING
# z = x + y  
# print("sum:" , z)


# TRIGONOMETRIC FORMULA FOR FINDING HYPOTANEOUS

# B = 2
# P = 3

# P = input("enter value of P")
# B= input("enter value of B")

# Z = ((int(B) ** 2) + (int(P) ** 2)) ** (1/2)
# print("sum:",  Z)

# print("+-----------+")
# print("|           |")
# print("|           |")
# print("|           |")
# print("|           |")
# print("|           |")
# print("+-----------+")

# print("+"+ "-"* 10 + "+")
# print(("|"+" "*10+"|\n")*5, end="")
# print("+"+ "-"* 10 + "+")


# print("Hello How are you?", end="\n")
# print("i am good ")

# city = 'Bhopal'
# #        012345 = index positions
# #        -6-5-4-3-2-1  

# print(city[0])
# print(city[-6])

# var = 11
# if var == 11:
#   print("var is 11")
#   print("Hello")

# QUE. write a program that reads a sequence of numbers and counts how many numbers are even and how many are odd. the program terminates when zero is enterd?

# num = int(input("please enter a number:"))
# even_count = 0
# odd_count = 0
# while num != 0:
#   if num % 2 == 0:
#     even_count += 1
#   else:
#     odd_count += 1

#   num = int(input("please enter a number:"))

# print("even:", even_count)
# print("odd:", odd_count)

# counter = 5
# while counter != 0:
#   print("inside the loop.", counter)
#   counter -= 1
# print("outside the loop.", counter)

# counter = 5
# while counter:
#     print("inside the loop.", counter)
#     counter -= 1
# print("outside the loop.", counter)


# for counter in range(10):
#   print("counter:", counter)

# for counter in range(2,8):
#   print("counter:", counter)


# python control flow. Loop


# print("the braek instructions:")
# for counter in range(1, 6):
#   if counter ==3:
#     # break
#     continue
#   print("inside the loop", counter)
# print("outside the loop.")
  
# largest_number = -999999999
# counter = 0

# number = int(input("Enter a number or type -1 to end the program:"))
# while number != -1:
#   if number == -1:
#     continue
#   counter += 1
#   if number > largest_number:
#     largest_number = number

#   number = int(input("Enter a number or type -1 to end the program:"))

# if counter != 0:
#   print("the largest number is", largest_number)
# else:
#   print("you haven't enterd any number.")


#counter = 1
# while counter < 5:
#   print(counter)
#   counter += 1
# else:
#   print("else:", counter)

# counter = 5
# while counter < 5:
#   print(counter)
#   counter += 1
# else:
#   print("else:", counter)

# for counter in range(5):
#   print(counter)
# else:
#   print("else:", counter)

# counter = 111
# for counter in range(2,1):
#  print(counter)
# else:
#  print("else", counter)

# blocks= int(input("enter the number of blocks"))
# counter = 0
# while (blocks - counter > 0):
#   counter += 1
#   blocks = blocks - counter
# print(f'Hieght of the pyramid:{counter}')

# Commands of git
# 1. git add *
# 2. git commit -m "Explain the commit here"
# 3. 



# numbers = [10, 5, 7, 2, 1]

# print(numbers)
# print(type(numbers))
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])

# numbers[0] = 100
# print(numbers)








