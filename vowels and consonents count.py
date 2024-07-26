a=eval(input("enter the string"))
b=len(a)
vowels="aeiouAEIOU"
consonents="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowels_count=0
consonents_count=0
for char in a:
    if char in vowels:
        vowels_count=vowels_count+1
    else:
        consonents_count=consonents_count+1
print("vowels count=",vowels_count)
print("consonents count=",consonents_count)
