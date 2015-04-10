#Juan Antonio Olvera Robles
def sqr(num):
    est=(num+1.0)/2.0
    nest=(est+num/est)/2.0
    return nest
num=int(input("give me a number to get it squart root"))
print(sqr(num))
