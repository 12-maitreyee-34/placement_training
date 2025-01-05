# #find factorial of any number using for loop iteration
num=int(input("Enter number:"))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
print("factorial of the number is:",fact)    


#fibonacci series
num=int(input("Enter range:"))
f0=int(input("Enter fo:"))
f1=int(input("Enter f1:"))
print(f0,f1,end=" ")
for i in range(3,num+1):
    f2=f0+f1
    print("\t",f2,end=" ")
    f0=f1
    f1=f2


#find sum of the following series sum=1 +x/1 + x^2/2 + x^3/3 + ..... + x^n/n
n=int(input("Enter range:"))
x=int(input("Enter x:"))
sum=1
for i in range(1,n+1):
    sum=sum + (x**i)/i
print("Sum is:",sum)    


# # #find the sum of same series with factorial logic sum = 1 +x^1/[1!] + x^2/[2!] +...+ x^n/[n!]
n=int(input("Enter range:"))
x=int(input("Enter x:"))
sum=1
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum=sum + (x**i)/fact
print("Sum is:",sum)    

#find x*y without the use of '*' operator and use of + operator
x=int(input())
y=int(input())
sum=0
for i in range(1,y+1):
    sum=sum+x
print(sum)   


#break statement
for i in range(1,11):
    if i==5:
        break;
    print(i)
#continue statement
for i in range(1,11):
    if i==5:
        continue;
    print(i)


#represent the numbers in the following format..Skip the numbers 3 and 8:-
#1   10
#2   9
#4   7
#5   6
i=1
j=10
while i<j:
    if i==3 and j==8:
        continue;
        print(i,"\t",j)
        i=i+1
        j=j-1

# pattern problems
# print matrix  problem
# 1111
# 2222
# 3333
# 4444
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()   

# pattern problem
# ABCD
#EFGH
#IJKL
#MNOP
#use of ASCII value
n=65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n),end=" \t")
        n=n+1    #if this is not printed, it will print only A matrix
    print()    #bydefault next line will be printed

#pattern problem
n=1
for i in range(1,5):
    for j in range(1,5):
        print(n,end=" \t")
        n=n+1    #if this is not printed, it will print only A matrix
    print()    #bydefault next line will be printed  


#pattern problem
#1
#2 2
#3 3 3
#4 4 4 4
    
for i in range(1,5):
    for j in range(1,i):
        print(i,end=" \t")
    print()    

#pattern problem 

sp=5
for i in range(4,0,-1):
    for x in range(sp):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()     
    sp=sp+1


#string function 1. finding substring
s="Hello my name is xyx"
print(s.find("my"))
print(s.find("n"))
print(s.rfind("abb"))
print(s.count("l"))
print(s.count("my"))
print(s.count("l",0,9))   #how many times l will occur between o and 9       





    
          


    
    