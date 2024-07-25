p=eval(input("enter the price="))
r=eval(input("enter the rate="))
t=eval(input("enter the time="))
n=eval(input("enter the no.of times intrest is compounded="))
compound_intrest=p*(1+r/n)**n*t-p
print("compound intrest=",compound_intrest)
