#Write a Python Program for Fibonacci numbers.

nterms=int(input("Enter the number of terms:"))
n1=0
n2=1
count=0
if nterms<=0:
    print("Enter a positive number.")
elif nterms==1:
    print(n1)
else:
    while count<nterms:
        print(n1,end=' ')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
