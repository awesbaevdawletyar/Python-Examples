# if ---> eger
#else -----> 

belgi=input("belgi: ") # str

san1=int(input("san1=")) # int
san2=int(input("san2="))  #int

if belgi == "+":
    sum=san1+san2
    print("sum=",sum)
elif belgi == "-":
    aliw=san1-san2
    print("aliw=",aliw)
elif belgi == "*":  #true
    kob=san1*san2
    print("kobeytiw=",kob)
elif belgi == "/":
    bol=san1/san2
    print("boliw=",bol)
elif belgi == "**":
      san1**=san2   #san1=san1**san2
      print("san1 din darjesi =",san1)
elif belgi=="%":
    qaldiq=san1%san2
    print("qaldiq=",qaldiq)
else:
    print("siz basqa belgi kiritdin'iz")

   