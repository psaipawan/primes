def checkPrime(num):
    cnt=0
    for j in range(1,num+1):
        if(i%j==0):
            cnt+=1;
    return cnt

num = int(input("Enter an integer"))
for i in range(num):
    if(checkPrime(i)==2):
        print(f"{i} is Prime Number")
    else:
        print(f"{i} is not a prime number")
