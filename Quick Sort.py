def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def swap(my_list,index_1, index_2):
   my_list[index_1], my_list[index_2] = my_list[index_2], my_list[index_1]

def quick_sort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left,right)
        quick_sort(my_list, left, pivot_index-1)
        quick_sort(my_list, pivot_index+1,right)
    return my_list
my_l = [8,9,1,7,3,5,2,6,4]
print(my_l)
quick_sort(my_l,0,len(my_l)-1)
print(my_l)
