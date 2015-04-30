#Juan Antonio Olvera Robles
#Quiz 11 Programa 2
def check_banana(file):
	txt=open("banana.txt","r")
	banana=0
	for i in txt:
		low=i.lower()
		x=low.find("banana")
		while x !=-1:
			banana= banana + 1
			x=low.find("banana",(x+1))
	return banana
	close("banana.txt")

total=check_banana("banana.txt")
print ("The number of times that the word banana was found is:",total)
