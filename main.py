#Activity 1
def printno(n):
    iteration=0
    print("Total number entered by user",n)
    iteration+=1
    print("Total iteration done by computer",iteration) 

printno(10)
printno(200)

#Activity 2
def ontime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("When'n'is",n,"Iterations",iteration)

ontime(50)
ontime(60)
ontime(70)

#Activity 3

def time(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iteration+=1

            print("")
            print(n,"iteration=",iteration)

time(5)
time(6)

#Activity 4