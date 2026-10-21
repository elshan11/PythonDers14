# for j in range(3):
#     for i in range(4):
#         print("j:",j,"i:",i)

# for i in range(3):
#     for j in range(3):
#         print("i:",i,"j:",j)
#     else:
#         print("Daxili dovr tamamlanndi")    

# else:
#     print("Xarici dovr tam bitdi")


# for i in range(1,4):
#     for j in range(1,4):
#         print(i,"+",j,"=",i+j)
#     print("---------")    

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    

n=5

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="") 
    print()    

