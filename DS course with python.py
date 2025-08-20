# %%
def calculate_simple_interest(principal, rate, time):

  simple_interest = (principal * rate * time) / 100
  return simple_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period: "))

interest = calculate_simple_interest(principal, rate, time)
print(f"The simple interest is: {interest}")

# %%
n = int(input("Enter an integer: "))

if n % 2 != 0:
  print("weird")
elif n % 2 == 0 and 2 <= n <= 5:
  print("not weird")
elif n % 2 == 0 and 6 <= n <= 20:
  print("weird")
elif n % 2 == 0 and n > 20:
  print("not weird")

# %% [markdown]
# # Task
# Write a program that takes the lengths of the three sides of a triangle as input from the user, calculates the area of the triangle using Heron's formula, and prints the calculated area.

# %%
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

import math

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("The area of the triangle is:", area)

# %%
b = int(input("Enter the coefficient 'b': "))
a = int(input("Enter the coefficient 'a': "))
c = int(input("Enter the coefficient 'c': "))
import cmath
import math
delta = (b**2) - 4*(a*c)
if delta > 0:
  x1 = (-b - math.sqrt(delta)) / (2 * a)
  x2 = (-b + math.sqrt(delta)) / (2 * a)
  print(f"The roots are real and distinct: {x1} and {x2}")
elif delta == 0:
  x = -b / (2 * a)
  print(f"The roots are real and equal: {x}")
else:
  x1 = (-b - cmath.sqrt(delta)) / (2 * a)
  x2 = (-b + cmath.sqrt(delta)) / (2 * a)
  print(f"The roots are complex: {x1} and {x2}")


# %% [markdown]
# while loop
# 

# %%
joining_age = 25
while joining_age <= 60:
  print(joining_age)
  joining_age = joining_age + 1
else:
  print("Its time to retirement")

# %% [markdown]
# list

# %%
fruit = ["mango", "cherry", "apple", "banana"]
for fruit in fruit:
  print(fruit)
  if fruit == "cherry":
    print("Found cherry!")

# %%
s = "data"
s.title()

# %%
s = "data"
s.capitalize()

# %%
string = "arshan"

# %%
#first element of sting
print(string[0])

# %%
#last element of sting
print(string[-1])

# %%
#nth element
print(string[2])

# %%
from ast import Index
if length exceeds, then it will give index out of range as we are finding Index


# %% [markdown]
# #slicing

# %%
s = "ARSHAN"

# %%
s[0:1:]

# %%
s[0: :1]

# %%
#reverse
s[0:0:-1]

# %%
s[1:3]

# %%
s[:-3]

# %%
s[2:]

# %%
s[:-2]

# %% [markdown]
# s[::2]

# %%
len(s)

# %%
s.find('H')

# %%
print(s.split(' '))

# %%
print(s.split('u'))

# %%
print(s.swapcase())

# %%
print(s.upper())

# %%
print(s.lower())

# %%
print(s.title())

# %%
s.isdigit()

# %%
s.isspace()

# %%
s.endswith('N')

# %%
s.startswith('A')

# %%
a = "khanarshan6669gmailcom"

# %%
a.isalnum()

# %%
a.istitle()

# %%
a = "khanarshan6669gmailcom"
a = a.title()
a.istitle()

# %% [markdown]
# #wap to find sum of natural numbers

# %%
num_1 = int(input("Enter a natural number: "))

if num_1 < 0:
   print("Please enter a natural number")
else:
   sum_of_numbers = 0
   i = 1
   while i <= num_1:
       sum_of_numbers += i
       i += 1
   print("The sum is", sum_of_numbers)

# %% [markdown]
# #WAP to find numer of digits in a number

# %%
num_str = input("Enter an number: ")

num_digits = len(num_str)

print("The number of digits in the number is:", num_digits)

# %%
list = [4,5,6,85,41,52,65,63]

num_digits = len(list)

print("The number of digits in the list is:", num_digits)

# %% [markdown]
# #WAP TO FIND NO. OF OCCURANCE OF A CHARACTER IN A STRING

# %%
input_string = input("Enter a string: ")
search_character = input("Enter the character to count: ")

if len(search_character) != 1:
    print("Please enter only a single character to count.")
else:
    count = 0
    for char in input_string:
        if char == search_character:
            count += 1
    print(f"The number of occurrences of '{search_character}' in the string is: {count}")

# %%
list = [1,2,3,4,5,6,7,8]
even_sum = 0
odd_sum = 0

for number in list:
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print("Sum of even numbers: ",even_sum)
print("Sum of odd numbers: ",odd_sum)

# %% [markdown]
# #print +ve no. from the list
# 
# 

# %%
number = [-2,-1,0,1,2,3,4]

positive_numbers = [num for num in number if num > 0]
print(positive_numbers)

# %% [markdown]
# square of no.

# %%
number = [-2,-1,0,1,2,3,4]
[num**2 for num in list]

# %% [markdown]
# #create a list of only the first letters of words in a list

# %%
words = ["apple", "banana", "cherry", "date"]
a = [word[0] for word in words]
print(a)

# %% [markdown]
# #convert a list of temp. from celsious to fahrenheit using kist comprehensive

# %%
celc_temp = [0,10.1,20,30,40,50]
fahr_temp = [(temp * 9/5) + 32 for temp in celc_temp]
print(fahr_temp)

# %% [markdown]
# #flatten a list of list into single list

# %%
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in lists for item in sublist]
print(flattened_list)

# %% [markdown]
# #create a list of only the prime numbers from a given list

# %%
list = [1,2,3,4,5,6,7,8,9,10]
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in list if is_prime(num)]
print(prime_numbers)

# %% [markdown]
# #get the largest element from the list

# %%
list = [58, 60, 77, 69, 88, 1]
a = max(list)
print(a)

# %% [markdown]
# #remove duplicates from the list

# %%
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)

# %% [markdown]
# #to convert list of multiple integers into a single integer

# %%
x = [11, 33, 50]
y = int("".join(map(str, x)))
print(y)

# %% [markdown]
# #Tuple

# %%
t = ()

# %%
type(t)

# %%
t1 = (1,2,3,4,5,6,45+7j, "yoo", True)

# %%
type(t1)

# %%
t1

# %%
t1.count(4)

# %%
for i in t1 :
  print(i, (type(i)))

# %%
t2 = (1,2,3,4,5)

# %%
t2

# %%
t2*3

# %%
min(t2)

# %%
max(t2)

# %%
t3 = (t1+t2)

# %%
t3

# %%
len(t3)

# %% [markdown]
# #check wether an elemont exist within a tuple

# %%
a = int(input("enter a number: "))
t = (1,2,3,4,5,6, "a")

if a in t:
  print("is in the tuple.", {a})
else:
  print("is not in the tuple.", {a})

# %% [markdown]
# #find index of an item in a tuple

# %%
t = (1,2,3,4,5,6, "a")

index = t.index(4)
print("The index is:", {index})

# %% [markdown]
# #remove empty touple(s) from a list of tuples

# %%
s = [(), (), (''), ('a','b'), ('a','b', 'c'), ('d')]

t = [t for t in s if t]

print(t)

# %%
s = [(), (), ('',), ('a','b'), ('a','b', 'c'), ('d')]
new_list = []

for item in s:
  if item:
    new_list.append(item)

print(new_list)

# %% [markdown]
# #dictionry

# %%
d = {}

# %%
type(d)

# %%
d1 = {"name": "arshan", "branch": "DS", "sem": "5th"}

# %%
d1

# %%
d2 = {123 : "abc"}

# %%
d2

# %%
d2 = {123.3 : "abc"}
d2

# %%
d2 = {True : "abc"}
d2

# %%
d2 = {@ : "abc"}
d2

# %%
d2 = {[123.3] : "abc"}
d2

# %%
d2 = {(123.3) : "abc"}
d2

# %%
d2 = {{"key":123.3} : "abc"}
d2

# %%
d12 = {"cource name": ["python", "stats", "machine learning", "deep learning"]}
d12

# %%
d12["key"] = "abc"
d12

# %%
del d12['key']

# %%
d12.clear()

# %%
d12

# %%
len(d12)

# %%
d13 = {"name": "arshan", "branch": "DS", "sem": "5th"}

# %%
d13.keys()

# %%
list(d13.items())

# %% [markdown]
# #create an intersection of sets
# 

# %%
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

a = set()

for item in set1:
    if item in set2:
        a.add(item)

print("The intersection of the two sets is:", a)

# %% [markdown]
# #wap to check if a set is a subset of another set

# %%
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

is_subset = True
for item in a:
    if item not in b:
        is_subset = False

if is_subset:
    print("a is a subset of b")
else:
    print("a is not a subset of b")

# %% [markdown]
# #check if a set is superset of another set

# %%
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

is_superset = True
for item in b:
    if item not in a:
        is_superset = False
else:
  is_superset:
  print("b is a superset of a")

# %% [markdown]
# #find max and min value of set
# 
# 

# %%
a = {58, 60, 77, 69, 88, 1}

max = max(a)
min = min(a)

print("The maximum value in the set is:", max)
print("The minimum value in the set is:", min)

# %%
a = {58, 60, 77, 69, 88, 1}

max = None
min = None

for item in a:
    if max is None or item > max:
        max = item
    if min is None or item < min:
        min = item

print("The maximum value in the set is:", max)
print("The minimum value in the set is:", min)

# %% [markdown]
# #find element in a set not in another

# %%
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

a = set()

for item in set1:
    if item not in set2:
        a.add(item)

print("Elements in set1 but not in set2:", a)