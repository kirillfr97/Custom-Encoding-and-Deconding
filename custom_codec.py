import re

from typing import List


class CustomCodec:
    def encode(self, text: str) -> str:
        tokens = re.split(r"(\W+)", text)
        encoded_words: List[str] = []
        for token in tokens:
            encoded_word = token
            if encoded_word.isalnum():
                encoded_word = self._substitution(encoded_word)
                encoded_word = self._rearrangement(encoded_word)
                encoded_word = self._index_based(encoded_word)
            encoded_words.append(encoded_word)
        encoded_text = "".join(encoded_words)
        encoded_text = self._add_special_symbol(encoded_text)
        encoded_text = self._multiply_numbers(encoded_text)
        return encoded_text

    def decode(self, encoded_text: str) -> str:
        encoded_text = self._divide_numbers(encoded_text)
        encoded_text = self._delete_special_symbol(encoded_text)
        tokens = re.split(r"(\W+)", encoded_text)
        words: List[str] = []
        for token in tokens:
            word = token
            if word.isalnum():
                word = self._reverse_index_based(word)
                word = self._reverse_rearrangement(word)
                word = self._reverse_substitution(word)
            words.append(word)
        return "".join(words)

    def _multiply_numbers(self, string: str) -> str:
        """
        Multiply numbers by 3 and reverse
        """
        idx = 0
        encoded_string = ""
        while idx < len(string):
            if not string[idx].isdigit():
                encoded_string += string[idx]
                idx += 1
                continue

            digits = self._get_digits_from_string(string, idx)
            new_digits = int(digits) * 3
            if new_digits != 0 and digits[0] == "0":
                new_digits = "0" + str(new_digits)
            encoded_string += str(new_digits)[::-1]
            idx += len(digits)

        return encoded_string

    def _divide_numbers(self, encoded_string: str) -> str:
        idx = 0
        string = ""
        while idx < len(encoded_string):
            if not encoded_string[idx].isdigit():
                string += encoded_string[idx]
                idx += 1
                continue

            digits = self._get_digits_from_string(encoded_string, idx)
            new_digits = int(digits[::-1]) // 3
            if new_digits != 0 and digits[-1] == "0":
                new_digits = "0" + str(new_digits)
            string += str(new_digits)
            idx += len(digits)

        return string

    @staticmethod
    def _add_special_symbol(string: str) -> str:
        """
        After every third character in the string, insert a #.
        """
        return "#".join(string[i:i+3] for i in range(0, len(string), 3))

    @staticmethod
    def _delete_special_symbol(encoded_string: str) -> str:
        return encoded_string.replace("#", "")

    @staticmethod
    def _index_based(string: str) -> str:
        """
        For each character in the string, add its index (starting from 0) to its ASCII value,
        and convert the new value back into a character.
        Example: For "abc", a (ASCII 97, index 0) stays as a, b (ASCII 98, index 1) becomes c, and c (ASCII 99, index 2) becomes e.
        """
        if string.isnumeric():
            return string

        encoded_string = ""
        for idx, char in enumerate(string):
            if not char.isalpha():
                encoded_string += char
                continue

            ascii_code = ord(char) + idx
            if not chr(ascii_code).isalpha():
                ascii_code -= 26
            encoded_string += chr(ascii_code)

        return encoded_string

    @staticmethod
    def _reverse_index_based(encoded_string: str) -> str:
        if encoded_string.isnumeric():
            return encoded_string

        string = ""
        for idx, char in enumerate(encoded_string):
            if not char.isalpha():
                string += char
                continue

            ascii_code = ord(char) - idx
            if not chr(ascii_code).isalpha():
                ascii_code += 26
            string += chr(ascii_code)

        return string

    @staticmethod
    def _rearrangement(string: str) -> str:
        """
        For words with more than 5 letters, split the word into two halves. Swap the positions of the two halves.
        If the word has an odd number of letters, include the middle letter in the first half.
        example: "Python" becomes "honPyt".
        """
        if len(string) < 5:
            return string

        middle: int = len(string) // 2 + len(string) % 2
        return string[middle:] + string[:middle]

    @staticmethod
    def _reverse_rearrangement(encoded_string: str) -> str:
        if len(encoded_string) < 5:
            return encoded_string

        middle: int = len(encoded_string) // 2
        return encoded_string[middle:] + encoded_string[:middle]

    @staticmethod
    def _substitution(string: str) -> str:
        """
        Replace all vowels (a, e, i, o, u) with their ASCII values.
        Replace all consonants with the next letter in the alphabet (e.g., b becomes c, z becomes a).
        """
        if string.isnumeric():
            return string

        encoded_string = ""
        for char in string:
            if char in "aeiouAEIOU":
                encoded_string += str(ord(char))
            elif char.isalpha():
                next_char = chr(ord(char) + 1) if char not in "zZ" else chr(ord(char) - 25)
                encoded_string += next_char
            else:
                encoded_string += char
        return encoded_string

    @staticmethod
    def _reverse_substitution(encoded_string: str) -> str:
        if encoded_string.isnumeric():
            return encoded_string

        def get_ascii_of_alpha(string: str, start: int) -> str:
            code, pos = "", start
            while pos < len(string) and string[pos].isdigit():
                code += string[pos]
                pos += 1
                if chr(int(code)).isalpha():
                    return code

        idx = 0
        decoded_string = ""
        while idx < len(encoded_string):
            char: str = encoded_string[idx]
            if char.isdigit():
                ascii_code = get_ascii_of_alpha(encoded_string, start=idx)
                decoded_string += chr(int(ascii_code))
                idx += len(ascii_code)
            elif char.isalpha():
                prev_char = chr(ord(char) - 1) if char not in "aA" else chr(ord(char) + 25)
                decoded_string += prev_char
                idx += 1
            else:
                decoded_string += char
                idx += 1

        return "".join(decoded_string)

    @staticmethod
    def _get_digits_from_string(string: str, start: int) -> str:
        i = start
        digits = ""
        while i < len(string) and string[i].isdigit():
            digits += string[i]
            i += 1
        return digits
