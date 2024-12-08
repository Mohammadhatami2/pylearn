name=input("enter your frist name and your family:")
while True:
    math=float(input("enter your math status:"))
    sci=float(input("enter your Science status:"))
    other=float(input("enter your oher lesson stats:"))
    x=(math+sci+other)/3
    if math<=0 or sci<=0 or other<=0 or math>20 or sci>20 or other>20:
        print("please choice higher than 1  or lower than 20")
        continue
    else:
        if x>=17:
            print("your name is :",name,)
            print(" and your status is good")
            break
        elif 17>x>=12:
            print("your name is :",name,)
            print("you are normal ")
            break
        elif x<12:
            print("your name is :",name,)
            print("your are fail")  
            break  