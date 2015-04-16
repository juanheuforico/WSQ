#Juan Antonio Olvera Robles
def triangulo(n):
    for i in range(1,n+1):
        print("t"*i)
    for i in range(n,0,-1):
        print("t"*i)
n=int(input("give me the size of the triangle: "))
triangulo(n)
