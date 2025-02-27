def selection_sort(My_List):
    for i in range(len(My_List)-1):
        min_index = i
        for j in range(i+1, len(My_List)):
            if My_List[j]<My_List[min_index]:
                min_index = j
        My_List[i],My_List[min_index] = My_List[min_index], My_List[i]
