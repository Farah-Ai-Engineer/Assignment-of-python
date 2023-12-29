# 1.Write a program using a for loop to print the numbers from 1 to 10.
for i in range(1,11):
    print(i)
# 2.Create a program that uses a for loop to print the multiplication table of a user inputted number.  
user=int(input("Enter a Number: "))      
for i in range(1,11):
    print(f"{user}X{i}={user*i}")
# 3.Write a program using a while loop to find the sum of natural numbers up to a given number entered by the user.
user=int(input("Enter Number: "))
sum=0
i=1
while i<=user:
    sum+=i
    i+=1    
print("The Sum is",sum)    
# 4.Create a program that uses a for loop to iterate through a list of names and prints each name.
name=["Amna","Hira","Saliha","Faiza"]
for name in name:
    print(name)
# 5.Write a program using a while loop to find the factorial of a user-inputted number.    
user=int(input("Enter Number: "))
multiply=1
i=1
while i<=user:
    multiply*=i
    i+=1
print("The Factorial of",user,"is",multiply)
# 6.Create a program using a for loop to print the Fibonacci series up to a specified number of terms entered by the user.
user=int(input("Enter Number: "))
x=0
y=1
print(x)
print(y)
i=1
while i<=(user-2):
    sum=x+y
    print(sum)
    x=y
    y=sum 
    i+=1        
# 7.Write a program using a while loop to reverse a number the user enters.
user=input("Enter Number: ")
sum=0
i=0
while i<len(user):
    x=user[i]
    sum+=int(x)
    i+=1
print("The sum of digit is",sum)    
# 8.Create a program that uses a for loop to iterate through a string and count the number of vowels.
user=input("Enter Name: ")
add=0
for user in user:
    if user=="a" or user=="e" or user=="i" or user=="o" or user=="u" or user=="A" or user=="E" or user=="I" or user=="O" or user=="U":
        add+=1
print(add)        
# 9.Write a program using a while loop to check if a user-inputted number is a palindrome.
user=input("Enter Name: ")
i=0
j=-1
while i<len(user) and j<len(user):
    if user[i]!=user[j]:
        print("Not Palindrome")
        break
    i+=1
    j-=1
else:
    print("Palindrome")    
# 10.Create a program using a for loop to calculate and print the sum of the squares of the numbers from 1 to 5.
x=0    
for i in range(1,6):
    x+=(i**2)
print("The sum of square from 1 to 5 is",x)    



    








