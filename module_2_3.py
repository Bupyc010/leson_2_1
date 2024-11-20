my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i_count = 0

while i_count < len(my_list):
    if(my_list[i_count] > 0):
        print(my_list[i_count])
    elif(my_list[i_count] < 0):
        break
    else:
        pass
    i_count += 1
