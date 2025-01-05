# #find last digit of a number 
no=int(input("enter thr no:"))
result=no%10
print("The last digit of a no or the unit digit no of the given no is :",result)

# #sum of two digit no 45 is the no so sum of 4 and 5=9
no=int(input("enter the no:"))
no1=no%10
no2=no//10
res=no1+no2
print("The sum of two digit no:",res)

# #sum of 6digit no eg 123456
no=int(input("enter the no:"))
n1=no%10  #we will get 6 from 12345
no=no//10 #we will get the op or the op will be saved in no 12345
n2=no%10  # we will get 5 from the new saved no 12345 where 5 will be separarted from 1234
no=no//10 #we will get 1234 as the op will be saved in no
n3=no%10 #4 will be separated from 123
no=no//10  #123 is stored in no
n4=no%10  #3 is separated from 123
no =no//10  #12 is stored
n5=no%10  #2 is separated
no=no//10  #1 is stored
n6=no%10  #1 is the output
res=n1+n2+n3+n4+n5+n6
print("sum",res)


# #reverse of 3 digit no
no=int(input("enter the no:"))
n1=no%10  #we will get 3 from 123
no=no//10 #we will get the op or the op will be saved in no 12
n2=no%10  # we will get 2 from the new saved no 12 where 2 will be separarted from 1
no=no//10 #we will get 1 as the op will be saved in no
n3=no%10 #1 will be separated from 1
reverse=n1*100+n2*10+n3*1
print("reverse",reverse)


# #find the sum of 1st andm last digit (6 digit no) in 3 steps
no=int(input("enter the no:"))
n1=no%10                                         #Concept is not clear to me
n2=no//100000
res=n1+n2
print("sum of 1st and last digit",res)


#sum of 1st ad last digit of any digit number
num=input("enter number:")
first_digit=int(num[0])
last_digit=int(num[-1])
sum=first_digit+last_digit
print(sum)

# #complex datatypes
c=3
d=4
e1=complex(c,d)
print(e1)
print(complex(4,5))
print(complex(4,False))
print(complex(False,False))
print(complex(True,True))

# # #Identity operator
# #is and is not
a=10
b=10
print(a is not b)
print(a is b)
x=True
y=True
print(x is not y)
print(x is y )

# membership operator: it is case sensitive
# in and not in
xy="My name is maitreyee bhosale .I am python"
print('m' in xy)
print('S' in xy)
print('hello' in xy)
print('hello' not in xy)

# #eval(): can also be used to define an array(userdefined)
res=eval(input("enter the value:"))
print(res)

# Print() modification
s="ASHISH"
print(s)
print("hello"+"hello"+"world")
print("hello \nhello")
print("hello\thello")
print("hello"*4)
print(4*"hello")

# sep variable
a=10
b=24
c=45
print(a,b,c,sep=",")

# #end variable
print("hello",end=" ")
print("world",end=" ")
print("dear")

# formatted string %i and %d for int,%f for float
a=10
b=20
c=30
print(" a is the value of %i" %a)

# replacement operator{}
name="riya"
salary="600000"
company="TCS"
print("hello {0} your salary is {1} and company {2}".format(name,salary,company))
print("hello {x} your salary is {y} and company {z}".format(x=name,y=salary,z=company))

# Accept 5 numbers and find max no using simple if and no loop
n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter number:"))
n4=int(input("Enter number:"))
n5=int(input("Enter number:"))
max=n1
if max<n2:
    max=n2
if max<n3:
    max=n3
if max<n4:
    max=n4
if max<n5:
    max=n5
print(max)    


#find maximum and minimum number in a list 
#array/list in python isdefined by various ways:
#1. use map function and by using input()
#2. Use of loop for input:
num=input()  #while entering the number, dont use commas to separate the number use space instead
lst=list(map(int,num.split()))
print(min(lst))
print(max(lst))




# accept 5 paper marks .find total and percentage.Also accept gender..if gender is female and percentage>=82 then she can take admission 
# and if gender is male and percentage >=62 he can take admission

mk1=float(input())
mk2=float(input())
mk3=float(input())
mk4=float(input())
mk5=float(input())
gender=input("enter the gender:").lower()
# print(gender.lower()) #the lowercase() should be used immediately after the gender input 
# or else it will not check the if and elif loop
total_marks=mk1+mk2+mk3+mk4+mk5
percentage=(total_marks/500)*100
print(total_marks,"are the total marks")
print("percentage is:",percentage)
if percentage>=82 and gender=='female':
    print("She can take admission ")
elif percentage>=62 and gender=='male':
    print("He can take admission")
else:
    print("Cannot take admission")        
   


# WAP to check character is upper case,lower case,digit or special symbol USE OF ASCII function
ch=input("enter any character:")
ch=ord(ch) #ord function is used to convert the character in ascii character
if ch>=97 and ch<=122:
    print("lower case")
elif ch>=65 and ch<=90:
    print("upper case")
elif ch>=0 and ch<=57:
    print("digit")
else:
    print("special symbol")        


# WAP to check year is leap year or not..leap year are of 2 types ---> centuary leap year(400 years) and non centuary year(4 years)

year=int(input("enter thr year:"))
if year%400==0:
    print("It is a century leap year")
elif year%4==0:
    print("It s a leap year") 
else:
    print("It is neither a leap year nora century leap leaap year")       

# WAP to accept COSt price from user and ask wheather the user is a student or not.
# if the user is student and cost price >500, give discount of 10%else discount will be 5%
# If user is not a student and cost price is > 500 then give discount of 8% else discount will be 2%
# (take all inputs from user)            

cp=float(input("enter the cost price:"))
student=input("Are u a student or not?").lower()

if student=="yes":
    if cp>500:
        discount=(10/100)*cp
        print(discount)
    else:
        discount=(5/100)*cp
        print(discount)
else:
    if cp>500:
        discount=(8/100)*cp
        print(discount)
    else:
        discount=(2/100)*cp
        print(discount)    
net_cost=cp-discount  
print(net_cost)  

# reverse of a number using while loop
num=int(input("enter the number:"))
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("reverse is:",rev)    

# #count the no. of digits 
num=int(input())
count=0
while num>0:
    rem=num%10
    num=num//10
    count+=1
print(count)    

# #sum of digits
num=int(input("enter a number:"))
sum=0
while num!=0:
    n1=num%10
    num=num//10
    sum+=n1
print(sum) 

# #multiplication of digits
num=int(input("enter the number:"))
product=1
while num!=0:
    n1=num%10
    product=product*n1
    num=num//10
print(product)    


# #find factorial of a number
no=int(input("enter the number:"))
fact=1
while no>0:
    fact=fact*no
    no=no-1
print("factorial of the number is:",fact)    

# check if the no is armstrong no or not
no=int(input("enter the number:"))
sum=0
nsave=no
while no>0:
    rem=no%10
    sum=sum+(rem**3)
    no=no//10
    
if nsave==sum:
    print("the no is armstrong ")
else:
    print("the no is not an armstrong no")


# #armstrong no code for any digit
no=int(input("enter the number:"))
sum=0
count=0
nsave=no
while no>0:
    no=no//10
    count=count+1
no=nsave    
while no>0:
    rem=no%10
    sum=sum+(rem**count)
    no=no//10
    
if nsave==sum:
    print("the no is armstrong ")
else:
    print("the no is not an armstrong no")    


# find how many armstrong numbers are present between 1 to 10,000
for num in range(1,10001):
    sum=0
    count=0
    nsave=num
    while num>0:
        num=num//10
        count=count+1
    num=nsave  
       
    while num>0:
        rem=num%10
        sum=sum+(rem**count)
        num=num//10
    
    if nsave==sum:
        print(nsave,sum)


# #Find the palindrome
no=int(input("enter thr no:"))
rev=0
nsave=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
print("reverse is:",rev)   
if nsave==rev:
    print("armstrong")
else:
    print("not armstrong")     

#PETERSON NUMBER: sum of factorials of each digit is equal to the number
no=int(input("enter the num:"))
sum=0
nsave=no
while no>0:
    n1=no%10
    fact=1
    for i in range(1,n1+1):
        fact=fact*i
    sum+=fact
    no=no//10
print(sum)
if sum==nsave:
    print("Peterson number") 
else:
    print("Not a peterson number")           


# automorphic number:-natural Number whose square ends in the same digits as the number itself
no=int(input("Enter The number:"))
square=no**2
n1=square%10
num=no%10
print(square)
print(n1)
print(num)
if n1==num:
    print("The {0} is an automorphic number".format(no))
else:
    print("The {0} is not an automorphic number".format(no))     


#Tech number:-an even digit number that is equal to the square of sum of its two equal halves
num=int(input("Enter The number"))
nsave=num
num_str=str(num)
if len(num_str)%2!=0:
    print("The number not an Even number and cannot be split into halves")
else:
    mid=len(num_str)//2
    first_half=int(num_str[:mid])
    sec_half=int(num_str[mid:])
    sum=first_half+sec_half
    square=sum**2
    if square==nsave:
         print("Tech number")
    else:
         print("not a tech number")    

        
    








    





