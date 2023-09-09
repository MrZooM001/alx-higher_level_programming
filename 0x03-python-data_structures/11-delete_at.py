def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    new_list = my_list
    new_list[idx:idx + 1] = []
    return new_list
