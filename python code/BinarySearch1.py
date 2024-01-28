List = [10,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]
Found = False
SearchFailed = False
First = 0
Last = len(List) - 1
Middle = 0
SearchItem = int(input("Enter the number to search for: "))

while Found == False and SearchFailed == False:

    #the next three lines help us see the reduced list
    for i in range(First, Last + 1):
        print(List[i], end=" ")
    print()

    #searching and adjusting the region of search
    Middle = (First + Last) // 2

    print("First = ", First, "Last = ", Last, "Middle = ", Middle)
        
    if List[Middle] == SearchItem:
        Found = True
    else:
        if First >= Last: 
            SearchFailed = True
        else:
            if List[Middle] > SearchItem:
                Last = Middle - 1
            else:
                First = Middle + 1
#ENDWHILE

if Found == True:
    print("Found at the index: ", Middle)
else:
    print("Item not present in the array!")
