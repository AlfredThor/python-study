# 冒泡排序
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[ j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# class Sort:
#     def __init__(self,lists,left=None,right=None):
#         self.lists = lists

# 交换类排序
def swap(lists,i,j):
    lists[i], lists[j] = lists[j], lists[i]

def partition(list, left, right):
    povot = left
    index = povot+1
    i = index
    while i <= right:
        if list[i] < lists[povot]:
            swap(list, i, index)
            index+=1
        i+=1
    swap(list,povot,index-1)
    return index-1

def quickSort(lists, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(lists)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partion = partition(lists, left, right)
        quickSort(lists, left, partion-1)
        quickSort(lists, partion+1, right)
    return lists


if __name__ == '__main__':
    lists = [1, 4, 63, 79, 75, 324, 76576, 23, 9, 80, 37, 56]
    resu = bubbleSort(lists)
    res = quickSort(lists=lists)

    print(res)