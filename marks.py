m=int(input("enter the mark of subject"))
if m>=90:
    grade='s'
elif m>=80 and m<90:
    grade='a'
elif m>=70 and m<80:
    grade='b'
elif m>=60 and m<70:
    grade='c'
elif m>=50 and m<60:
    grade='d'
else:
    grade='fail'
print(m,"grade=",grade)
