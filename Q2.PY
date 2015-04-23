
x=0
def dotproduct(lis1):
    vec=0
    if len(lis1)== len(lis2):
        for i in range(0,len(lis1)):
            x=lis1[i]*lis2[i]
            vec=x+vec
    else:
        print("Not same size vectors")
        vec=-1
    return vec
lis1=[1,2,3]
lis2=[4,5,6]
