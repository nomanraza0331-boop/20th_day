#units=int(input("enter your number of units"))
#if units<=200:
#amount=units*5
#elif units>300 and units<*1:




# 3 subject phy chem and bio 

phy=int(input("enter yout marks :"))
chem=int(input("enter yout marks :"))
bio=int(input("enter yout marks :"))
total=phy+chem+bio


if total>550:
    print("you eligible for MBBS")
elif total<550 and total>=450:
    print("you eligible for BDS")
elif total<450 and total >=350:
    print("you elegible for BUMS")
elif total<350 and total>=200:
    print("you elegible for BAMS")
else:
    print("not elegible")

    
print(f"total={total}")