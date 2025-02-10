def filter_by_state(list_of_state: list[dict], state :str="EXECUTED") -> list:
    """Возвращает список по состоянию"""
    new_list = []
    for key in list_of_state:
        if key["state"] == state:
            new_list.append(key)
    return new_list


def sort_by_date(list_of_date: list[dict], descending: bool = True) -> list:
    """Функция возвращает список на убывание по дате"""
    return sorted(list_of_date, key=lambda x: x.get("date"), reverse=descending)
