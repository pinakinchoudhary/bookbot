from typing import TypedDict

class CharDict(TypedDict):
    char: str
    num: int

def get_book_text(filePath: str) -> str:
    with open(filePath) as f:
        return f.read()

def char_dict(file: str) -> dict[str, int]:
    from collections import Counter
    return dict(Counter(file))

def sorted_dict(charD: dict[str, int]) -> list[CharDict]:
    d_list: list[CharDict] = []
    for char, count in charD.items():
        if char.isalpha():
            tmp: CharDict = {"char":char, "num":count}
            d_list.append(tmp)

    d_list.sort(reverse=True, key=lambda x: x["num"])
    return d_list

