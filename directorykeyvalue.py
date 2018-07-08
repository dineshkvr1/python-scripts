x = { "name" :"Dinesh" , "age" : "25" }
print x ;

for key, value in x.iteritems() :
    print key;
    print value;

x['address'] = 'Downtown';
x['country'] = 'USA' ;
x['age'] = 26
print x; 
y=x;
print y;
y['name'] = 'madhu';
print y ;
print x ;




del y['name'];
print y;
