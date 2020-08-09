a=0
b=1
f=0
n=int(input("Enter the no of terms required: "))
print("Fibonacci series:")
while(f<n):
    print(a)
    c=a+b
    a=b
    b=c
    f=f+1
