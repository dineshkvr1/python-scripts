c = "test"
a="malayalam";
x = len(a)
y = len(c)
d =""
b= ""
for i in range(x-1,-1,-1):
    b=b+a[i] ;
print b;
if(a==b):
  print "given string is palindrome";
else:
  print "given string is  not palindrome";




for i in range(y-1,-1,-1):
    d=d+c[i];
print d;
if(d==c):
   print "given string is palindrome";
else:
   print "given string is not palindrome";
