# #replacing a string
# #.replace(old string,new string)
s="Learning python is very difficult from ashish sir"
s1=s.replace("difficult","easy")
print(s1)

# #immutable:-changes cannot be done but in the same memory
# #mutable:- Changes can be done in the same memory

# #immutability in string
a=10
print(a)
print(id(a))
b=10
print(b)
print(id(b)) #here id will be same as variable is different 

# #.split()
s="Learning python is very difficult from ashish sir"
l=s.split()
print(l)
for x in l:
    print(x)




#ip="hello world"
#op="0lleh dlrow"
s=input("enter:")
l=s.split()
print(l)
rev=""
for i in l:
    rev=rev+i[::-1]+" "
print(rev)

#wap to remove duplicate characyters from a string
#ip="ABCDABCDABCD"
#op="ABCD"

s=input("enter a string")
l=[]
for i in s:               
    if i not in l:
        l.append(i) 
        output=''.join(l)
print(output)


# #list creation
l=[]
print(type(l))
ls=list() 
print(ls)
lst=eval(input()) 
print(lst)    


# #Traversing ttechniques in list
n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(0):
    print(n[i])      
    i=i+1


#insert()in list
s=[1,2,3]
s2=[4,5,6]
s.insert(3,"krrr")
print(s)
s.extend(s2)
print(s) 

# #.remove() and.pop() and .reverse()
n=[1,2,3,4,5]
n.remove(1) #1 is the number not index
n.pop()  #pop or removes the no. from end
print(n)
n.reverse()

# #.sort()
n=[0,5,3,7,88]
n2=['t','h','s','v']
n3=["dog","cat","banana"]
n.sort()
n2.sort()
print(n,n2,n3)

# #nested list
n=[2,4,[3,445,6],6]
print(n[0])
print(n[2])
print(n[2][2])
for x in n:
    print(x)

# #nested list as a matrix
n=[[10,20,30],[30,40,50,80],[78,90,87]]
# print(n)
# for x in n:
#     print(x)  prints but not in mattrix
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=" ")
    print()    


#list and string functions
#1.find the max element in the list withpout using max()

s=eval(input("enter list"))
max=s[0]
for x in range(1,len(s)):
    if max<s[x]:
        max=s[x]
print(max)

#2.Remove duplicates from a list 
lst=eval(input("enter list:"))
d=[]
for x in range(len(lst)):
    if lst[x] not in d:      #here dont put if x  not in d. put lst[x]
        d.append(lst[x])
print(d)   



#3.check for palindromic list
#hint:-ompare the list with its reverse
lst=eval(input("enter list:"))
rev=[]
for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])       #lst[i] should not be there in for loop..
print(rev) 
if rev==lst:
    print("palindrome")
else:
    print("not palindrome")   


#4.sum of list elements
n=list(map(int,input().split())) 
sum=0   
for i in n:
    sum=sum+i
print(sum)


#5.remove an Element from a list by value without .remove()
#eg ip[1,2,3,4,5] and element=3
#op[1 2 4 5]
n=list(map(int,input().split())) 
x=int(input("enter thr no to be removed"))
lst=[]
for i in n:
    if x!=i:
        lst.append(i)
    else:
        continue    
print(lst)    

#6.Anagram checker ..if anagram print yes, if not, print no
str1=input("enter string:").lower()
str2=input("enter string:").lower()
a=sorted(str1)
b=sorted(str2)                                   
print(a,b)
if a==b:
    print("Anagram")
else:
    print("not anagram")    

#count vowels and consonants in the string
string=input("Enter string:")
lst=list(string.lower())
v=0
c=0
for i in lst:
    if i in 'aeiou':
        v=v+1
    else:
        c=c+1    
print("vowel count",v)
print("consonent count",c)        


