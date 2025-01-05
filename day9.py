# 1,2,3,4,5 tuple creation
t = eval(input())
print(t, type(t))

#min max in tuple
t = (40,10,30,20)
print(sorted(t))
print(type(sorted(t)))
print(min(t))
print(max(t))

# cmp() function
# It compares the elements of both tuples.
# If both tuples are equal tehn returns 0
# If the first tuple is less than second tuple then it returns -1
# If the first tuple is greater than second tuple then it returns +1
# t1 = (10,20,30)
# t2 = (40,50,60)
# print(cmp(t1,t2))
# probably stopped working after Python3


t = 1,123,13,12,3,123
print(t)
print(type(t))
sum=0
for x in t:
  sum+=x

print(sum)
print((sum/len(t)))


# MergeSort Algorithm
# Question given by sir

# Merge two sorted lists
# Write a function to merge two sorted lists into a single sorted list.
# Logic = Use two pointers to iterate through the lists and merge them.
# Sample Input: [1,3,5] and [2,4,6]
# Expected Output: [1, 2, 3, 4, 5, 6]

# s1 = [1,3,5]
# s2 = [2,4,6]

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s1.sort()
s2.sort()
i = 0
j = 0
res = []
while i!=len(s1) or j!=len(s2):
  if i==len(s1) and j!=len(s2):
    res.append(s2[j])
    j+=1
  elif i!=len(s1) and j==len(s2):
    res.append(s1[i])
    i+=1
  else:
    if s1[i]<s2[j]:
      res.append(s1[i])
      i+=1
    elif s1[i]>s2[j]:
      res.append(s2[j])
      j+=1
    else:
      res.append(s1[i])
      i+=1

print(res)
    
# SET add function
s = {11,22,33,44,55}
print(s)
s.add(444)
print(s)
s.add('555')
print(s)
s.add('Raj')
print(s)
s1 = s.copy()
s2 = s
print(s1)
print(s2)
print(s.pop())


# Write a program to eliminate duplicates present in the list

l = list(map(int, input().split()))
print(list(set(l)))

# d = {}
# d = dict()
d = {101: 'ashish', 102: 'raj', 103: 'Rohit'}
print(d)
print(type(d))
print(d[101])

# Write a program to enter name and percentage marks in a dictionary and display information on the screen

rec = {}

n = int(input("Enter number of students: "))
i = 1
while i<=n:
  name = input("Enter Student Name: ")
  marks = input("Enter % of Marks of Student: ")
  rec[name] = int(marks)
  i+=1

for x in rec:
  print(x,"\t",rec[x])


# updating a dictionary
d = {'A': 99, 'B': 65, 'C': 78}
print(d)
d['D'] = 75
print(d)
d['B'] = 54
print(d)
d['A'] = [99,98]
print(d)


# del function
d = {'A': [99, 98], 'B': 54, 'C': 78, 'D': 75}
print(d)
del d['C']
print(d)
# del d
# deletes the whole dictionary


d = {100: 'ashish', 200: 'prashant', 300: 'sandip'}
print(d[100])
print(d.get(100))
print(d.get(400))
print(d.get(100,"Guest"))
print(d.get(400,"Guest"))
print()
print(d.keys())
for k in d.keys():
  print(k)
print()
print(d.values())
for k in d.values():
  print(k)

d = {100: 'ashish', 200: 'prashant', 300: 'sandip'}
for k,y in d.items():
  print(k,"-->",y)



# Write a program to take dictionary from the keyboard and print the sum of values

n = int(input("Enter number of employees: "))
d = {}
for _ in range(n):
  name = input("Enter the name of employee: ")
  salary = int(input("Enter the salary of {0}".format(name)))
  d[name] = salary
print(d)

sum = 0
for x in d.values():
  sum+=x
print(sum)


# Check if a key exists in a dictionary
# - Write a function to check if a key exists in a dictionary
# Logic: Use the in operator or the get() method
# Sample Input: Dictionary: {'name': 'Alice', 'age': 30}, Key: 'age'
# Expected Output: Key Exists

n = int(input())
d = {}
for _ in range(n):
  name = input()
  value = input()
  d[name] = value

key = input()
print(key in d.keys())


# Iterate over dictionary keys and values
n = int(input())
d = {}
for _ in range(n):
  name = input()
  value = input()
  d[name] = value

print()
for k,v in d.items():
  print(k,":",v)


#  Merge two Dictionaries

d1 = {'name': 'Alice'}
d2 = {'age': 64}

d1.update(d2)
print(d1)

# Find the key with the maximum value in a dictionary

d = {'A': 99, 'B': 65, 'C': 78, 'D': 75}
print(max(d.values()))


# Reverse a dictionary
# Create a new dictionary with reversed key-value pairs

d = {'A': 99, 'B': 65, 'C': 78, 'D': 75}
res = {}

for k,v in d.items():
  res[v] = k

print(res)


n = int(input("Enter no. of semester: "))
rec = []
ns = []
for i in range(n):
  ns.append(int(input("Enter no of subjects in semester {0}: ".format(i+1))))

for i in range(n):
  print("Marks obtained in semester {0}".format(i))
  myl = []
  n2 = ns[i]
  for j in range(n2):
    myl.append(int(input()))
  
  rec.append(max(myl))

for i in range(len(rec)):
  print("Maximum mark in {0} semester: {1}".format(i+1, rec[i]))


# Edit Distance
# Given two strings s and t. Return the minimum number of operations required to convert s to t.
# Example 1:
# Input:
# s = 'ycce', t = 'ycsce'
# Output: 1
# Explanation: One operation is required inserting 's' between two 'c's of s

# Example 2:
# Input:
# s = 'h4c', t = 'h4c'
# Output:
# 0
# Explaination: Both strings are same


# s,t = input().split()

# if s == t:
#   print(0)

# else:
#   i = 0
#   j = 0
#   count = 0
#   while i!=len(s) or j!=len(t):
#     if s[i] == t[j]:
#       i+=1
#       j+=1
#     else:
#       count+=1
#       j+=1

#   print(count)


s,t = input().split()

if s == t:
  print(0)

else:
  s1 = list(s)
  s2 = list(t)

  for i in s1:
    if i in s2:
      s2.remove(i)
  
  print(len(s2))


# Functions
# Function is a self contained block which is designed and run separately and returns the result to the main function

# Ways to reuse a code
# - Functions
# - Package
# - Inheritance

# function wihtout parameters and without return
def add():
  a = 30
  b = 40
  res = a+b
  print(res)

# function with parameter and without return
def subtract(a,b):
  res = a-b
  print(res)

# function with parameter and with return
def multiply(a,b):
  res = a*b
  return res

# main function
if __name__ == '__main__':
  add()
  print(subtract(40,30))


# Multiple values return function

def arithematic(x,y):
  res1 = x+y
  res2 = x-y
  res3 = x*y
  res4 = x//y

  return res1, res2, res3, res4

a = int(input())
b = int(input())

r1, r2, r3, r4 = arithematic(a,b)
print("Addition:",r1)
print("Subtraction:",r2)
print("Multiplication:",r3)
print("Division:",r4)


def add(a,b):
  print(a+b)

def subtract(a,b):
  print(a-b)

def multiply(a,b):
  print(a*b)

def division(a,b):
  print(a//b)

while True:
  a = int(input("Enter first value: "))
  b = int(input("Enter second value: "))
  print("1. Add\n2. Subtract\n3. Multiplication\n4. Division\n5. Exit")
  choice = int(input("Enter your choice: "))

  if choice == 1:
    add(a,b)
  elif choice == 2:
    subtract(a,b)
  elif choice == 3:
    multiply(a,b)
  elif choice == 4:
    division(a,b)
  elif choice == 5:
    break
  else:
    print("Enter valid choice")


# Create functions armstrong, reverse, palindrome and factorial with return values (menu driven program)

def reverse(a):
  res = str(a)
  return res[::-1]




def armstrong(num):
  n = num

  sum=0
  remain = []
  count=0

  while num!=0:
    remain.append(num%10)
    num=num//10
    count+=1

  for i in range(count):
    sum+=remain[i]**count

  if n == sum:
    return True
  else:
    return False




def palindrome(num):
  n=num
  rev = 0
  while num > 0:
    rem = num % 10
    rev = (rev*10)+rem
    num = num//10

  if n == rev:
    return True
  else:
    return False




def factorial(num):
  n = num
  fact = 1
  while num!=0:
    fact*=num
    num-=1
  return fact


if __name__ == '__main__':
  while True:
    a = int(input("Enter a number: "))
    print("1. Armstrong\n2. Palindrome\n3. Reverse\n4. Factorial\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      if armstrong(a):
        print(a,"is an amrstrong number")
      else:
        print(a,"is not an armstrong number")
    elif choice == 2:
      if palindrome(a):
        print(a,"is a palindrome")
      else:
        print(a,"is not a palindrome")
    elif choice == 3:
      print(a,"reverse is:",reverse(a))
    elif choice == 4:
      print("Factorial of {0} is {1}".format(a, factorial(a)))
    elif choice == 5:
      break
    else:
      print("Enter valid choice")


# Keyword Argument

def add(x,y):
  print("X =", x)
  print("Y =", y)
  print("Result: ", x+y)

add(x=10, y=20)
add(y=20, x=33)


# Default Argument

def add(x, y=55):
  print("X =", x)
  print("Y =", y)
  print("Result: ", x+y)

add(22)
add(44,1)

# Variable length argument
def add(*n):
  res = 0
  for i in n:
    res+=i
  return res

add(10,30,20,40)

#code
from itertools import permutations
x = [1,1,1]
res = permutations(x, 3)
print(list(res))

#Find the security key for a given number
num=int(input("Enter the number: "))
num_str=str(num)
count=0
lst=[]
for i in num_str:
    if i not in lst:
        lst.append(i)
    else:
        count+=1
print(count)            
