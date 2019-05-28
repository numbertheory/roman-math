#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


class Error(Exception):
    """Base class for other exceptions"""
    pass


class NotIntegerError(Error):
    """Only integers may be converted to Roman numerals."""
    pass


class NotRomanNumeral(Error):
    """Not a valid Roman Numeral expression"""
    pass


class ConvertToArabicNumerals():
    def __init__(self):
        pass

    def convert(self, roman_numerals):
        roman_string = roman_numerals.upper()

        # Abort if any characters are not valid
        validate_string = [True for x in list(roman_string)
                           if x in ['M', 'D', 'C', 'L', 'X', 'V', 'I',
                                    '𝕍', '𝕏', '𝕃', 'ℂ', '𝔻', '𝕄']]

        if len(validate_string) != len(list(roman_string)):
            raise NotRomanNumeral

        # Find representational subtraction groups
        regex = r"(IX)|(IV)|(CM)|(CD)|(XL)|(XC)|(ℂ𝕄)|(ℂ𝔻)|(𝕏ℂ)|(𝕏𝕃)"
        hits = [[y for y in set(x) if y != ''][0]
                for x in
                re.findall(regex, roman_string)]
        if len(set(hits)) != len(hits):
            raise NotRomanNumeral
        else:
            grouped = [x for x in
                       re.compile(regex).split(roman_string)
                       if (x is not None and x != '')]

        groupings_table = {
            "M": 7,
            "D": 6,
            "C": 5,
            "L": 4,
            "X": 3,
            "V": 2,
            "I": 1,
            "𝕍": 8,
            "𝕏": 9,
            "𝕃": 10,
            "ℂ": 11,
            "𝔻": 12,
            "𝕄": 13
        }
        # Abort if groupings are out of order
        result = 0

        master_table = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
            "𝕍": 5000,
            "𝕏": 10000,
            "𝕃": 50000,
            "ℂ": 100000,
            "𝔻": 500000,
            "𝕄": 1000000,
            "IX": 9,
            "IV": 4,
            "CM": 900,
            "CD": 400,
            "XL": 40,
            "XC": 90,
            "ℂ𝕄": 900000,
            "ℂ𝔻": 400000,
            "𝕏ℂ": 90000,
            "𝕏𝕃": 40000
        }
        print(grouped)
        for numeral in grouped:
            if numeral in list(master_table.keys()):
                result += master_table[numeral]
            else:
                raise NotRomanNumeral

        return result


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
