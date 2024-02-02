#Binary Tree implementation using parallel 1D arrays 
#This code is avaible in https://github.com/qmirzobek/ALevelCSCodeLists/
newNodePtr=0
MaxIndex=6
RootPointer=-1
nullPointer=-1
TurnedLeft=False
treeLeft=[None for i in range(MaxIndex)]
treeData=[None for i in range(MaxIndex)]
treeRight=[None for i in range(MaxIndex)]
def display(treeLeft, treeData, treeRight):
    for i in range(MaxIndex):
        print(i," | ", treeLeft[i]," | ",treeData[i]," | ",treeRight[i]," | ")
    print()
def initialise():
    global RootPointer, nullPointer, freePointer,previousNodePtr, newNodePtr,thisNodePtr, treeLeft, treeRight, treeData, TurnedLeft
    RootPointer=nullPointer
    freePointer=0
    for i in range(MaxIndex-1):
        treeLeft[i]=(i+1)
    treeLeft[MaxIndex-1]=(nullPointer)
initialise()
display(treeLeft, treeData, treeRight)
def insertNode(item):
    global RootPointer, nullPointer, freePointer,previousNodePtr, newNodePtr,thisNodePtr, treeLeft, treeRight, treeData, TurnedLeft
    if freePointer!=nullPointer:
        newNodePtr=freePointer
        freePointer=treeLeft[newNodePtr]
        treeData[newNodePtr]=item
        treeLeft[newNodePtr]=nullPointer
        treeRight[newNodePtr]=nullPointer
        if RootPointer==nullPointer:
            RootPointer=newNodePtr
        else:
            thisNodePtr=RootPointer
            while thisNodePtr!=nullPointer:
                previousNodePtr=thisNodePtr
                if treeData[thisNodePtr]>item:
                    TurnedLeft=True
                    thisNodePtr=treeLeft[thisNodePtr]
                else:
                    TurnedLeft=False
                    thisNodePtr=treeLeft[thisNodePtr]
            if TurnedLeft==True:
                treeLeft[previousNodePtr]=newNodePtr
            else:
                treeRight[previousNodePtr]=newNodePtr
    else:
        print("Tree is full")
def findNode(item):
    global thisNodePtr, RootPointer, nullPointer, treeLeft, treeRight, treeData
    thisNodePtr=RootPointer
    while thisNodePtr!=nullPointer and treeData[thisNodePtr]!=item:
        if treeData[thisNodePtr]>item:
            thisNodePtr=treeLeft[thisNodePtr]
        else:
            thisNodePtr=treeRight[thisNodePtr]
    return thisNodePtr
#values are used to insert to binary tree    
insertNode(5)
insertNode(8)
insertNode(3)
display(treeLeft, treeData, treeRight)
print(findNode(3))
