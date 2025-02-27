def sort(My_List, Start, End):
    

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
3