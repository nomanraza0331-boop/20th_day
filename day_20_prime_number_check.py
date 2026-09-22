'''
n=(int(input("enter your number: ")))
for d in range(2,(n//2)):
    if n%d==0:
        print(f"{n} is not prime because it is divisible by{d}")
        break
else:
        print(f"is prime")
'''
# check prime number



# n=int(input("Enter a number: "))

primes=[]
for n in range(1,101):
    if n==1:
        pass
    else:
        for d in range(2,(n//2)+1):

            if n%d==0:
                break
        else:
            primes.append(n)
print(primes)
