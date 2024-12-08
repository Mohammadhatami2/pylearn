
import math

num1=float(input("enter the number:"))
inp=input("what do you want(+,-,/,,*,//,sqrt,cos,sin,cot,tan,factorial):")
if inp in("+","-","/","*"):
 num2=float(input("enter the second number:"))
if inp=="+":
   print(num1+num2)
elif inp=="-":
   print(num1-num2)
elif inp=="*":
   print(num1*num2) 
elif inp=="/":
   print(num1/num2)  
elif inp=="sqrt":
   print(math.sqrt(num1))   
elif inp=="cos":
   x1=(math.cos(num1))
   print(x1*math.pi/180)
elif inp=="sin":
   x2=(math.sin(num1))
   print(x2*math.pi/180)
elif inp=="tan":
   x3=(math.tan(num1))
   print(x3*math.pi/180)
elif inp=="factorial":
   print(math.factorial(num1)) 
elif inp=="cot":
  c1=math.cos(num1)/math.sin(num1)
  print(c1*math.pi/180)