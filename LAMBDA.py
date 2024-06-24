# LAMBDA
#USE: The power of lambda is better shown  when you use them as an anonymous  function inside another function.

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



#EXAMPLE:
x = lambda a : a + 10
print(x(5))

#EXAMPLE:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
