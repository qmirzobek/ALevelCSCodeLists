myarray=[7,12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,87,92,99]
found=False
searchFailed=False
first=0
searchitem=int(input())
maxitems=len(myarray)
last=maxitems-1
while not(found) and not(searchFailed):
    middle=(first+last)//2
    if myarray[middle]==searchitem:
        found=True
    else:
        if first>=last:
            searchFailed=True
        else:
            if myarray[middle]>searchitem:
                last=middle-1
            else:
                first=middle+1
if found==True:
    print(middle)
else:
    print("Item not present in the list")
