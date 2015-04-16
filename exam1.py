#Juan Antonio Olvera Robles
x1=int(input("give me x1 "))
y1=int(input("give me y1 "))
x2=int(input("give me x2 "))
y2=int(input("give me y2 "))
def distancia(x1, y1, x2, y2):
    a=x2-x1
    b=y2-y1
    dis=(a**2 + b**2)**.5
    return dis
print("the distance is:")
print(distancia(x1, y1, x2, y2))
