#Juan Antonio Olvera Robles
a=int(input("give me a number "))
b=int(input("give me other number to get its gcd "))

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


print("the Greatest Common Divisor (GCD) of your numbers is:")
print(gcd(a,b))
