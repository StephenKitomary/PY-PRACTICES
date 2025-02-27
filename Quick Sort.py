def quick_sort(My_List, left, right):
    if left < right:
        pivot_index = pivot(My_List,left, right)
        quick_sort(My_List, left, pivot_index-1)
        quick_sort(My_List, pivot_index+1, right)
    return My_List

    

def pivot(My_List,pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if My_List[i]<My_List[pivot_index]:
            swap_index += 1
            swap(My_List,swap_index,i)
    swap(My_List, pivot_index, swap_index)
    return swap_index



def swap(My_List, index1, index2):
    My_List[index1], My_List[index2] = My_List[index2], My_List[index1]

List = [4,6,2,1,7,3,8,5]
print(quick_sort(List, 0, len(List)-1))
