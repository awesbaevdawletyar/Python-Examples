import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

D=b*b-4*a*c
print("D=",D)

if D>0:
    print("Ten'leme eki sheshimge iye ham olari tomendegeshe:")
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print("x1=",x1)
    print("x2=",x2)
elif D==0:
    print("Ten'leme bir sheshimge iye boladi:")
    x=-b/(2*a)
    print("x=",x)
else:
    print("bos koplik")