inp1=float(input("enter the frist number:"))
inp2=float(input("enter the second number:"))
inp3=float(input("enter the third number:"))
x1=inp2+inp3
x2=inp1+inp3
x3=inp1+inp2
if inp1==inp2 and inp1==inp3:
    print("its curect")
if inp1>inp2 and inp1>inp3:
    if x1>inp1:
     print("its curect")
    else:
       print("its not")
if inp2>inp1 and inp2>inp3:
    if x2>inp2:
     print("its curect")
    else:
       print("its not")
if inp3>inp2 and inp3>inp1:
    if x3>inp3:
     print("its curect")
    else:
       print("its not")