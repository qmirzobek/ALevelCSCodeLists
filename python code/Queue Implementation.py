#==QUEUE==
#DECLARE i, frontPointer, endPointer, queueFull, queueLength, upperBound:INTEGER
def display(MyArray):
    for i in range(len(MyArray)):
        print(MyArray[i], end=" | ")
    print()
def queueStep(myArray):
    print("FrontPointer = ",frontPointer," | EndPointer = ", endPointer," | UpperBound = ", upperBound, " | QueueLength = ",queueLength," | QueueFull = ",queueFull," Item = ",item, end="\n")
    display(myArray)
    print()
queueLength=int(input("Enter queue length"))
queue=[]
for i in range(queueLength):
    queue.append(None)
display(queue)
frontPointer=0
endPointer=-1
upperBound=10
queueFull=queueLength
queueLength=0
def enqueue(item):
    global queueLength, queueFull, frontPointer, endPointer, upperBound, queue
    if queueLength<queueFull:
        if queueLength==0:
            frontPointer=0
        if endPointer<upperBound:
            endPointer=endPointer+1
        else:
            endPointer=0
        queueLength=queueLength+1
        queue[endPointer]=item
    else:
        print('Queue is full, cannot enqueue')
def dequeue():
    global queueLength, queueFull, frontPointer, endPointer, upperBound, queue, item
    if queueLength==0:
        print("Queue is empty, cannot dequeue")
    else:
        item=queue[frontPointer]
        queueLength=queueLength-1
        if queueLength==0:
            frontPointer=0
            endPointer=0
        else:
            if frontPointer==upperBound:
                frontPointer=0
            else:
                frontPointer==frontPointer+1
        queue[frontPointer]=None
while True:
    command=input("Command list(enqueue, dequeue or stop) \nEnter command:")
    if(command=="stop"):
        break
    elif(command=="enqueue"):
        item=int(input("Enter number to be enqueued: "))
        enqueue(item)
        queueStep(queue)
    elif(command=="dequeue"):
        dequeue()
        queueStep(queue)
    else:
        print("!!!!!Wrong command!!!!!")
    

