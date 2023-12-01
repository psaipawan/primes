num = int(input("Enter an integer"))
cnt=0
for i in range(num):
    for j in range(1,num+1):
        if(i%j==0):
            cnt+=1;
    if(cnt==2):print(f"{i} is Prime Number")
    else:print(f"{i} is not a prime number")
    cnt=0;
