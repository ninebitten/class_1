num = int(input("Enter "))
flag = True
if num < 2:
    
    print("non prime")
else:
    for i in range(2,num):
        if  num % i == 0:
            flag = False
            break
        if flag:
            print("prime")
        else:
            print("non prime")