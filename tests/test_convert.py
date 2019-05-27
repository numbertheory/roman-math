# -*- coding: utf-8 -*-

from nose.tools import assert_equal, assert_true, assert_raises
from roman_math.convert import ConvertToRomanNumerals
from roman_math.convert import NotIntegerError


def test_convert():
    """ Tests the conversion to Roman numerals. """
    d = ConvertToRomanNumerals()
    assert_equal(d.convert(4), 'IV')
    assert_equal(d.convert(5), 'V')
    assert_equal(d.convert(7), 'VII')
    assert_equal(d.convert(400), 'CD')
    assert_equal(d.convert(800), 'DCCC')
    assert_equal(d.convert(900), 'CM')
    assert_equal(d.convert(9), 'IX')
    assert_equal(d.convert(40), 'XL')
    assert_equal(d.convert(49), 'XLIX')
    assert_equal(d.convert(1000), 'M')
    assert_equal(d.convert(1000000), '𝕄')


def test_handle_ordered_groups():
    """ Makes sure we always return a complete grouping dict. """
    d = ConvertToRomanNumerals()
    for group in ["M", "C", "D", "L", "X", "V"]:
        assert_true(group in d.handle_ordered_groups(7),
                    "{} not found.".format(group))


def test_special_exceptions():
    d = ConvertToRomanNumerals()
    assert_raises(NotIntegerError, d.convert, 'q')
