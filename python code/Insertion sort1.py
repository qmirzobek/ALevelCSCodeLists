CardData = [57, 91, 25, 52, 33, 56, 11, 59, 12, 85]
ArraySize = 10

# Procedure to display the array elements
def Display():
    for Pointer in range(0, ArraySize):
        print(CardData[Pointer], end = " ")
    print()

print("Before Insertion sort")
Display()
print("\n")

for Pointer in range(1, ArraySize):

    ValueToInsert = CardData[Pointer]
    NextPosition = Pointer

    while NextPosition > 0 and CardData[NextPosition - 1] > ValueToInsert:
        CardData[NextPosition] = CardData[NextPosition - 1]
        NextPosition = NextPosition - 1

    CardData[NextPosition] = ValueToInsert

    #showing the changes happening for each step
    print("Pointer =", Pointer, "ValueToInsert =", ValueToInsert, "NextPosition =", NextPosition)
    Display()
    print()

# The final sorted array
print("\nAfter Insertion sort")
Display()

