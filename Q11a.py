#juan Antonio Olvera Robles
#Quiz 11 awnser 1
import statistics
def readNumbersFromFile():

    lis=[]
    x=open('numbers.txt','r') #'r' = read 'w'= readwrite
    linias=0
    total=0

    for line in x:
        total+= int(line)
        linias +=1
        lis.append(int(line))

    std=statistics.stdev(lis)
    prom=total/linias

    print("The total is:",total)
    print("Number of lines:",linias)
    print("The average is:",prom)
    print("The standard deviation is:", std)

readNumbersFromFile()
