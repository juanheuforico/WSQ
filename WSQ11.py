yosoy=0
pal=0
nol=0
def conv(men):
 men=str(men)
 men=men[::-1]
 men=int(men)
 return(men)
rango=[]
soy=[]
print("dame dos numeros para hacer un rango")
men=int(input("dame un numero menor del rango "))
may=int(input("dame el numero mayor del rango "))
print("el rango es de ",men," a",may)

for i in range(may-men+1):
 rango.append(men)
 men=men+1


for x in rango:
 cam=conv(x)
 if x==cam:
  pal=pal+1
 else:
  act1=cam+x
  act2=conv(act1)
  for y in range(30):
   if act1==act2:
    nol=nol+1
    break
   else:
    act1=act1+act2
    act2=conv(act1)
    if (y==29):
     yosoy=yosoy+1
     soy.append(x)
if yosoy!=0:
 print("Los yo soy 196 encotrados son:")
 for i in soy:
     print(i)

print("en tu rango hay")
print(yosoy," numeros lychrels")
print(pal," numeros palindromos")
print(nol," numeros que no son lychrel")
