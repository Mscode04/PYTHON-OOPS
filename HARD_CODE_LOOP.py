# part 1


a=[]
for i in range(2,21,2):
    a.append(i)
print(a)


print([i for i in range(2,21,2)])






#part 2
l1=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


l2=[i*i for i in l1]
print(l2) 



l2={i:i*i for i in l1}
print(l2)


f=lambda a:a*a
x=[f(a) for a in l1]
print(x)