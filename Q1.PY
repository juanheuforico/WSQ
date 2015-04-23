awn=1
lis=[]
def find_threes(lis):
    suma=0
    for i in range(0,len(lis)):
        if(lis[i]%3==0):
            suma+=lis[i]
    return suma
print(len(lis))
while(awn!='n'):
    ad=float(input("give me a number to put it in a list "))
    lis.append(ad)
    awn=str(input("do you want add another number? to no press(n) to yes any other key "))
print("here is your list")
print(lis)
print("here is the sum of all the numbers of your list")
print("that are divisibles by 3: ",find_threes(lis))
