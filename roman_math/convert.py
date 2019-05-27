#!/usr/bin/python
# -*- coding: utf-8 -*-


class Error(Exception):
    """Base class for other exceptions"""
    pass


class NotIntegerError(Error):
    """Only integers may be converted to Roman numerals."""
    pass


class ConvertToRomanNumerals():
    def __init__(self):
        pass

    def handle_groups(self, integer_input, number_group):
        if integer_input < 1:
            return ['', 0]
        grouping_arabic = {"M": 1000, "D": 500,
                           "C": 100, "L": 50,
                           "X": 10, "V": 5}
        remainder = integer_input % grouping_arabic[number_group]

        m_groups = int(integer_input / grouping_arabic[number_group])

        return [number_group * m_groups, remainder]

    def handle_ordered_groups(self, integer_input):
        groupings = dict()
        groupings['M'] = self.handle_groups(integer_input, 'M')
        groupings['D'] = self.handle_groups(groupings['M'][1], 'D')
        groupings['C'] = self.handle_groups(groupings['D'][1], 'C')
        groupings['L'] = self.handle_groups(groupings['C'][1], 'L')
        groupings['X'] = self.handle_groups(groupings['L'][1], 'X')
        groupings['V'] = self.handle_groups(groupings['X'][1], 'V')
        groupings['I'] = [groupings['V'][1] * 'I', 0]
        return groupings

    def stringify_groupings(self, groupings):
        result = str()
        for group in ['M', 'D', 'C', 'L', 'X', 'V', 'I']:
            result += groupings[group][0]
        return result

    def slim_down_result(self, roman_string):
        if roman_string.count("I") > 3:
            roman_string = roman_string.replace("IIII", "IV")
        if "VIV" in roman_string:
            roman_string = roman_string.replace("VIV", "IX")
        if roman_string.count("X") > 3:
            roman_string = roman_string.replace("XXXX", "XL")
        if "CCCC" in roman_string:
            roman_string = roman_string.replace("CCCC", "CD")
        if "LXL" in roman_string:
            roman_string = roman_string.replace("LXL", "XC")
        if "DCD" in roman_string:
            roman_string = roman_string.replace("DCD", "CM")
        if 1000 <= roman_string.count("M"):
            roman_string = roman_string.replace("".join('M'*1000), "𝕄")
        if 500 <= roman_string.count("M") < 1000:
            roman_string = roman_string.replace("".join('M'*500), "𝔻")
        if 100 <= roman_string.count("M") < 500:
            roman_string = roman_string.replace("".join('M'*100), "ℂ")
        if 50 <= roman_string.count("M") < 100:
            roman_string = roman_string.replace("".join('M'*50), "𝕃")
        if 10 <= roman_string.count("M") < 50:
            roman_string = roman_string.replace("".join('M'*10), "𝕏")
        if 4 < roman_string.count("M") < 10:
            roman_string = roman_string.replace("MMMMM", "𝕍")

        return roman_string

    def convert(self, integer_input):
        # Determine validity
        if not type(integer_input) is int:
            raise NotIntegerError

        groupings = self.handle_ordered_groups(integer_input)

        raw_roman_string = self.stringify_groupings(groupings)

        return self.slim_down_result(raw_roman_string)
