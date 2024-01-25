arr=[]
endp=-1
mx=int(input("Max elements: "))
while True:
    txt=input("Please write stop, push or pop: ")
    if endp==-1 and txt=="pop":
        print("Cannot pop stack is empty")
    elif endp==mx-1:
        print("Cannot push stack is full")
    elif txt=="push":
        endp+=1
        ps=int(input("Which element to push: "))
        arr.append(ps)
    elif txt=="stop":
        break
    elif(endp>-1 and txt=="pop"):
        print("Popping:",arr[endp])
        arr=arr[:-1]
        endp-=1    
    for i in range(endp,-1,-1):
        print(arr[i])
    print("_______________")
