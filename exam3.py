a=int(input("give me the a number"))
b=int(input("give me the a power that you want"))
x=a
def superpower(a,b):
    for i in range(1,b):
        a=a*x
    return a
print("the result is:")
print(superpower(a,b))
