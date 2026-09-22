for i in range (1,11):
    print(i)

# display all odd numbers in the range given by user

for i in range(int(input("enter your first number: ")),int(input("enter your second number:"))+1):
    if i%2==1:
        print(i)


#display all numbers which are divisible by n in range given by the user

f,l=map(int,input("enter first and last number").split())
n=input("enter the number: ")

