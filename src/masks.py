def get_mask_card_number(card_numbers: str) -> str:
    """Получение маски карты в формате XXXX XX** **** XXXX, где X — это цифра номера"""
    return f"{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}"


def get_mask_account(card_numbers: str) -> str:
    """Получение маски карты в формате **XXXX, где X — это цифра номера."""
    return f"**{card_numbers[-4:]}"
