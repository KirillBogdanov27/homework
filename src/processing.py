def filter_by_state(list_of_state:list, state='EXECUTED') -> list:
    new_list = []
    for key in list_of_state:
        if key['state'] == state:
            new_list.append(key)
    return new_list




