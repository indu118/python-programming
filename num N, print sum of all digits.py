a=int(raw_input())
if(a<0):
  a=-a
b=0  
while(a!=0):
   c=a%10
   b+=c
   a=a/10
print b 
   
   
