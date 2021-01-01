def pigeonhole_func(list_a):
    min_value = min(list_a)
    max_value = max(list_a)

    hole = [0] * (len(list_a) - 1)      # num of holes is 1 less than num of elements

    for element in list_a:
        if hole[element-min_value] == 1:
            print ("Duplicate found ! It is element " + str(element))
        else:
            hole[element-min_value] +=1


elements = [1,2,3,4,5,8,6,7,9,10,8]     # 11 elements

pigeonhole_func(elements)
