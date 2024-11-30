# for i in range(0,5):
#     for j in range(0,i + 1):
#         print(j,end=" ")
#     print()

n =int(input())
for i in range(1,n + 1):
    for j in range(1,n + 1):
        if(i+j >= n+ 1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()  

    
                  