from typing import List, Dict, ClassVar


class String:

    __REPLACE_CHARS: ClassVar[Dict[str, str]] = {
        "\xa0": ' '
    }

    @classmethod
    def decode(cls, string: str) -> str:
        for old_char, new_char in cls.__REPLACE_CHARS.items():
            string = string.replace(old_char, new_char)
        return string

    @classmethod
    def format(cls, string: str, max_length: int) -> str:
        output: str = ""

        words: List[str] = string.split(' ')
        count: int = 0
        is_first_word: bool = True

        word: str
        for word in words:

            if count + len(word) + 1 < max_length:
                if is_first_word:
                    output += word
                else:
                    output += f" {word}"
                count += len(word) + 1

            else:
                output += f"\n{word}"
                count = len(word) + 1

            is_first_word = False

        return output