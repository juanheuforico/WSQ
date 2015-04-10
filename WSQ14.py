#Juan Antonio Olvera Robles
def calculate_e(precision):
    e=1
    count=0
    x=0
    acum=1
    while (count<=precision):
        count=count+1
        x=1/(count*acum)
        e=e+x
        acum=count*acum
    e=str(e)
    awn=e[:e.find(".")+precision]
    return awn




precision = int(input("give me the number of decimals do you want "))
print ("The value of e is:",calculate_e(precision))
