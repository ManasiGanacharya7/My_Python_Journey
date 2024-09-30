# Print * * *
#       *   *
#       * * *

n = 3
for i in range(n):
   
    for j in range(n):
        if i==1 or i==n :
            print("*"*n, end = "")
            i+=1
            j=i+1
           
        else:
             print(" ",end="")
           
    print("")