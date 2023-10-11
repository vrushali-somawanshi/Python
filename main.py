
print("Vrushali")

a = 9
print("The value of a is:" + str(a))
# a = 9
# print(a)

x = 9
y = "Jerry"
print(type(x))
print(type(y))

if 9 < 15:
    print("9 is less than 15!")

a = "Cherry"
print(a)

c = "Python"
print(c[1:5])

a = "World..."
print(a.upper())

b = "W3 School"
print(b.lower())

z = " Python is a high level language!....  "
print(z.strip())

y = "Cloud"
print(y.replace("C", "G"))

a = "Cloud Vmware"
print(a.split())

a = 10
b = 20
print(a+b)
# c= a+b
# print(c)

a = "Ocean"
b = "Test"
print(a + " " + b)

age = 25
txt = "My name is Cherry, and I am {} years old"
print(txt.format(age))

quantity = 9
itemno = 12345
price = 50.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

a = 9
b = 10
if a > 10:
    print("a is greater than b")
else:
    print("a is not greater than b")

languages = ["C", "C++", "Java", "Python", "C#"]  # list
print(languages)

languages = ["C", "C++", "Java", "Python", "C#"]  # list
print(languages[2:5])

languages = ["C", "C++", "Java", "Python", "C#"]  # list
print(languages[:2])

languages = ["C", "C++", "Java", "Python", "C#"]  # list
print(languages[3:])

languages = ["C", "C++", "Java", "Python", "C#"]  # list
languages[3] = "Testing"
print(languages)

fruit = ["apple", "banana", "cherry"]
for x in fruit:
    print(x)

fruit = ["apple", "banana", "cherry"]
fruit.remove("banana")
print(fruit)

fruit = ["apple", "banana", "cherry"]
fruit.pop(2)
print(fruit)

fruit = ["apple", "banana", "cherry", "Mango"]
fruit.pop()
print(fruit)

fruit = ["apple", "banana", "cherry", "Mango"]
del fruit

fruit = ["apple", "Banana", "Cherry"]
fruit.clear()
print(fruit)

b = 12.0
c = 390.8

print(int(b))   # convert float to integer
print(int(c))   # convert float to integer

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

fruits = ["Cherry", "Watermelon", "Grapes", "Mango"]

newlist = [x for x in fruits if "r" in x]

print(newlist)

fruits = ["Cherry", "Watermelon", "Grapes", "Mango"]
fruits.sort()
print(fruits)

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort(reverse=True)
print(fruits)

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
newlist = fruits.copy()
print(fruits)

list1 = ["v", "r", "u", "s", "h"]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ["s", "o", "m", "a", "w", "a",  "n", "s", "h", "i"]

list3 = list1 + list2
print(list3)

mytuple = ("John", "Jerry", "Merry")
print(mytuple)

mytuple = ("John", "Jerry", "Merry")
print(mytuple[1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

subject = {"Marathi", "History", "Math", "English"}
print(subject)

fruit = {"apple", "banana", "cherry"}
for x in fruit:
    print(x)

fruit = {"apple", "banana", "cherry"}
print("banana" in fruit)

dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1998
}
print(dictionary)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1998
}
x = car["model"]  # Access dictionary items
print(x)

i = 1
while i < 8:
    print(i)
    i += 1

i = 1
while i > 8:
    print(i)
    if i == 6:
        break
        i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
def my_fruit():       # function definition or function create
 print("Hello I'm from fruit function")

my_fruit()  # function calling

def add_numbers(num1, num2):  # pass num 1 and num2  parameters(variable) in function
    sum = num1 + num2
    print("Sum: ", sum)
    add_numbers(9, 9)         # pass arguments(values) in function


x = lambda a : a + 10   # add 10 to argument a (lambda function use)
print(x(5))

x = lambda a,b : a * b  # multiply argument a with argument b and return result
print(x(9,9))

Bike = ["Ninja", "KTM", "Hunter", "Activa"]  # Create Array
x = Bike[1]  # Access Array
print(x)
