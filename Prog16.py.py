a =input("Enter any word for checking palindrome or not:")
flag = 1
for i in range (2,a):
    if (a % i)==0:
        print(a, "is not a prime number")
        print(i, "times",a//i,"is",a)
        flag = 0
        break
if flag ==1:
   print(a," is a prime number")

    

    


        
