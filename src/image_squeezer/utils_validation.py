def is_string_valid(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be string!")
    return text


def is_number_valid(number: int) -> int:
    try:
        if not number:
            raise ValueError("Provide an integer for the width")
        else:
            return int(number)
    except ValueError as exc:
        raise ValueError("Provide an integer for the width") from exc
