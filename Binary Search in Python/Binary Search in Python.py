from turtle import left, right



#binary search algorithm

binary_list = [1,2,3,4,5,6,7,8,9,10]
search_item = -9

left = 0
right = len(binary_list) - 1

while (left <= right):
    middle = (left + right) // 2
    if(binary_list[middle] == search_item):
        print("Item found at index: ", middle)
        exit()

    elif(binary_list[middle] < search_item):
        left = middle + 1
    else:
        right = middle -1

print("Item not found")