a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

# Initialize HCF
HCF = 1

if a == b:
    print("The numbers are the same, so the HCF is", a)
else:
    if a > b:
        small = b
    else:
        small = a
    
#Find HCF 
for i in range(2, small + 1):
    if a % i == 0 and b % i == 0:
        HCF = i

#Find LCM
LCM = (a*b)//HCF

print("")
print("•••The HCF of", a, "and", b, "is:", HCF)
print("•••The LCM of", a, "and", b, "is:", LCM)
print("\033[0m")