def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list:
    """
    Функция фильтрует список словарей по значению ключа 'state'.

    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(list_of_date: list[dict], descending: bool = True) -> list:
    """Функция возвращает список на убывание по дате"""
    return sorted(list_of_date, key=lambda x: x.get("date"), reverse=descending)
