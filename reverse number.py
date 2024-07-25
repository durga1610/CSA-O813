num=1234
rev_num=0
while num!=0:
      r=num%10
      rev_num=rev_num*10+r
      num=num//10
print(rev_num)
