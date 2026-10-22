#Iana Vasileva  CIS160 B65   M8P2    10/18/26
#Fibonacci sequence , start with 1, compute and display first 20 numbers

a=1
b=1
print(a)
for i in range(19):
    c=a+b
    print(c)
    a=b
    b=c
