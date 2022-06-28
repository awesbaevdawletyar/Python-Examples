import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

p=(a+b+c)/2
s=math.sqrt(p*(abs(p-a)*abs(p-b)*abs(p-c)))

print(s)