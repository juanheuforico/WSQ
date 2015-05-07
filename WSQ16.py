file=open("93.dat.txt","r")

car=0
mp=0
city=0
high=0
count=1
for line in file:
    if count%2==1:
        city=city+float(line[52:54])
        high=high+float(line[55:57])
        mp=mp+float(line[42:46])
        car=car+1
    count=count+1
x=round(city/car,5)
y=round(high/car,5)
z=round(mp/car,5)



print("City MPG " ,x)
print("Highway MPG " ,y)
print("midrange price " ,z)
