from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_num: str) -> str:
    """Функция возвращает тип карты и ее маску"""
    if "Счет" in card_type_num:
        return f"Счет {get_mask_account(card_type_num)}"
    else:
        separation = card_type_num.split()
        is_digit = ""
        is_alpha = ""
        name_card = " ".join(separation[:-1])
        for i in separation:
            if i.isalpha():
                is_alpha += i
            else:
                is_digit += i
                return f"{name_card} {get_mask_card_number(is_digit)}"


print(mask_account_card("Visa Union 8990922113665229"))


def get_date(date: str) -> str:
    """Возвращает дату в привычном для человека виде"""
    new_date = date[0:10]
    new_date_1 = new_date.split(sep="-")
    day = new_date_1[-1]
    months = new_date_1[-2]
    year = new_date_1[0]

    return f"{day}.{months}.{year}"


print(get_date("2024-03-11T02:26:18.671407"))
