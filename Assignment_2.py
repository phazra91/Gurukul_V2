a=1
b=1.0
c='1'
print(a,type(a))
print(b,type(b))
print(c,type(c))

a=2
b=2.0
c='2'
print(a,type(a))
print(b,type(b))
print(c,type(c))

a=b=c=10
print("a-",a,"b-",b,"c-",c)

a=10
b=20
print(a+b)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)
print(fruits[1])
print(fruits[3])

numbers = [10, 20, 30, 40, 50]
numbers[2]=35
print(numbers)

colors = ("red", "green", "blue")
print(colors)

colors = ("red", "green", "blue", "yellow")
print(colors[0])
print(colors[-1])

colors = ("red", "green", "blue")
#colors[1]="orange"
#TypeError: 'tuple' object does not support item assignment

coordinates = (10, 20, 30)
x,y,z=coordinates
print(x,y,z)

colors = ("red", "green", "blue")
print("blue" in colors)

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(len(days))

students={"Alice": 85, "Bob": 90, "Charlie": 78}
print(students)
print(students['Bob'])
students['David']=92
print(students)
students.pop("Charlie")
print(students)
students['Bob']=95
print(students)
print('Alice' in students.keys())
print(len(students))

# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number:"))
# c = int(input("Enter Third Number:"))
# max = a if a > b and a > c else b if b > c else c
# if a > b and a > c:
#     max=a
# elif b > c:
#     max=b
# else:
#     max=c
# print("Maximum Value:", max)

# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number:"))
# if a > b:
#     print("biggest number is", a)
# else:
#     print("biggest nymber is", b)

# n = int(input("Enter Number:"))
# if n>=1 and n<=10:
#     print ("The Number ",n,"is between 1 to 10")
# else:
#     print("The Number ",n,"is not between 1 to 10")

# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number:"))
# Addition=a+b
# print("Addition-", Addition)
# Subtraction=a-b
# print("Subtraction-", Subtraction)
# Multiplication=a*b
# Subtraction=a-b
# print("Multiplication-", Multiplication)
# Division=a/b
# print("Division-", Division)
# Modulus=a%b
# print("Modulus-", Modulus)

# a = int(input("Enter Number:"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# a = int(input("Enter Number:"))
# if a==0:
#     print("zero")
# elif a>0:
#     print("positive")
# else:
#     print("negative")

# a = int(input("Student Marks:"))
# if a>=90:
#     print ('A')
# elif a>=80 and a<90:
#     print('B')
# elif a>=70 and a<80:
#     print('C')
# elif a>=60 and a<70:
#     print('D')
# else:
#     print('F')

# file = open("Sample.txt", "w")
# file.write("Hello, this is a sample file.")
# file.close()

# file = open("Sample.txt", "r")
# text=file.read()
# file.close()
# print (text)

# file = open("data.txt", "r")
# text=file.read()
# file.close()
# print (text)
# l=len(text.split(" "))
# print(l)

# for i in range(1,11):
#     print(i)

a = int(input("Enter Number:"))
for i in range(1,11):
    print(a*i)











