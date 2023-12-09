"""advent of code Day1 part 2

cytat zadania:

...some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

W poniższym kodzie brakuje JEDNEGO znaku.
"""
from pathlib import Path
from typing import Optional


class DigitStrMap:
    def __init__(self, read_from_right: bool = False):
        self.fullmap = self._create_digit_str_map(read_from_right=read_from_right)
        self.current_sequences: list[str] = []

    def get_digit_for_matched_sequence(self, char: str) -> Optional[int]:
        """Example: if calls of this method were done in the following sequence:
        get_digit_for_matched_sequence("e") -> returns None
        get_digit_for_matched_sequence("i") -> returns None
        get_digit_for_matched_sequence("g") -> returns None
        get_digit_for_matched_sequence("h") -> returns None
        get_digit_for_matched_sequence("t") -> returns 8
        Calling this method with non-matching character will 'restart' the sequence.
        """
        matched_digit = None
        sequences_to_clear = []
        for index, sequence in enumerate(self.current_sequences):
            sequence_subdict = self._get_sequence_subdict(sequence)
            if isinstance(sequence_subdict.get(char), int):
                sequences_to_clear.append(sequence)
                matched_digit = sequence_subdict[char]
            elif isinstance(sequence_subdict.get(char), dict):
                self.current_sequences[index] += char
            else:
                sequences_to_clear.append(sequence)
        for sequence in sequences_to_clear:
            self.current_sequences.remove(sequence)
        if char in self.fullmap:
            self.current_sequences.append(char)
        return matched_digit

    def _get_sequence_subdict(self, sequence: str) -> dict:
        """
        For example if current sequence is equal to "t" this method returns:
        {
        "w": {
            "o": 2
        },
        "h": {
            "r": {
                "e": {
                    "e": 3
                    }
                }
            }
        }
        Or, if current sequence is equal to "sev" this method will return:
        {
        "e": {
            "n": 7
            }
        }
        """
        current_pointer = self.fullmap[sequence[0]]
        for matched_char in sequence[1]:
            current_pointer = current_pointer[matched_char]
        return current_pointer

    @staticmethod
    def _create_digit_str_map(read_from_right: bool = False) -> dict:
        digits_as_words = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }
        digit_str_map = {}

        for number, word in digits_as_words.items():
            if read_from_right:
                word = word[::-1]

            nested = digit_str_map.setdefault(word[0], {})
            for char in word[1:-1]:
                nested = nested.setdefault(char, {})
            nested[word[-1]] = number
        return digit_str_map


def get_digit(string: str, from_right: bool = False):
    if from_right:
        string = reversed(string)
    digit_map = DigitStrMap(read_from_right=from_right)
    for char in string:
        if (digit_from_str := digit_map.get_digit_for_matched_sequence(char)) is not None:
            return str(digit_from_str)
        if char.isdigit():
            return char
    raise ValueError("Digit not found!!!")


def get_2_digit_number(string: str) -> int:
    left_digit = get_digit(string)
    right_digit = get_digit(string, from_right=True)
    print(string, [left_digit, right_digit], int(left_digit + right_digit))
    return int(left_digit + right_digit)


def main():
    with open(Path(__file__).parent.parent / "1_Sobota_gr2_Michal" / "advent_1.txt") as file:
        lines = file.readlines()
    result = sum(map(get_2_digit_number, lines))
    print(result)
    assert result == 55291


if __name__ == '__main__':
    main()
