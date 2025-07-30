@staticmethod
def count_words(file_content: str) -> int:
    words = file_content.split()
    num_words = len(words)
    return num_words



@staticmethod
def count_chars(file_content: str) -> dict[str,int]:
    char_count = {}
    char_list = list(file_content.lower().replace(" ", ""))
    for char in char_list:
        if not char in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]

@staticmethod
def sort_count_chars(count_chars: dict[str, int]) -> list:
    char_list = []
    for key, value in count_chars.items():
        if key.isalpha():
            char_list.append({"char": key, "num": value})
    char_list.sort(reverse=True, key=sort_on)
    return char_list