# A fuction call in inner fuction


count=0
def alpha():
    print("your computer is hacked")
    global count
    count +=1
    alpha()
    print(count)
alpha()



def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))    
    
    