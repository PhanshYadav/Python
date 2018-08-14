''' program to input series of no in a List    '''

def no():
         
    n=int(input("Enter No OF Elements"))
    arg=[]
    flag=0
    for i in range(n):
        a=int(input("Enter NO"))

        arg.append(a)
    b=int(input("ENter No u Want to search"))
    for i in range(len(arg)):
                   if(b==arg[i]):
                       flag=1
                       break

    if flag==1:
        print("No FOunded At",i,"Position")
    else:    
         print("No Not In List")




            
