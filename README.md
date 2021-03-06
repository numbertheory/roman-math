# Roman Math

Read/translate Roman numerals. Do simple arithmetic with them. Work in progress.

## Definitions

Roman numerals are the numerals that are expressed using the Latin characters
I, V, X, C, L, and M, as seen in the table below.

| Character     | Arabic number  |
| ------------- |:--------------:|
| I             | 1              |
| V             | 5              |
| X             | 10             |
| L             | 50             |
| C             | 100            |
| D             | 500            |
| M             | 1000           |

Arabic numerals are the numbers that most modern people are very familiar with.
1, 2, 3, 4, etc.s


## Rules

1. This library does not cap out at 3,999. Some other libraries do this under the
assumption that Romans never used more than 3 of the same numerals in succession.
For this library, more than three numerals in succession is allowed if necessary.

2. The Romans would put an overline over a numeral to designate "multiply by 1000". So,
5000 would look something like: `⊽`

For this library, 1000 multipliers will be done with double-struck Unicode
characters, due to the inconsistencies of diacritical marks in most terminals.
"I" has no multiplier, as "M" by itself already represents 1000
times one.

| Character     | Arabic number  |
| ------------- |:--------------:|
| 𝕍             | 5000           |
| 𝕏             | 10000          |
| 𝕃             | 50000          |
| ℂ             | 100000         |
| 𝔻             | 500000         |
| 𝕄             | 1000000         |


# Representational Subtraction

Subtraction is used in Roman numerals to denote some numbers, like 9 (IX), or 900 (CM).
The general style is to group thousands, hundreds, tens, and ones together, which
is also enforced for representational subtraction, and so the subtraction should
only cross one grouping threshold.  Something like `IM` to denote 999 would not
be allowed as they belong to groupings that are not neighbors.  Additionally, V is not
used as a subtractor, so `VL` is not 45.


# Exceptions

Special exceptions need to be raised when working with Roman numerals to guard
against representing concepts never implemented in Roman numerals.

 - LessThanOne

   One is the lowest number in Roman numerals, and so any functions that would produce
   zero or a negative result will instead raise this exception. This exception is
   also raised during division, if the result is less than one (i.e. 1/2)

 - FloatingPointInput

   Raised when the input to this library is a floating point number. Only integers
   will be allowed.


# Division

To prevent exceptions from being raised all the time for division, remainders will
be used in answers when dividing numbers.  Remainders can be accessed using the
`remainder` method in the `.divide` function.

```
>>> roman_numerals.divide('7','2').value
'III'
>>> roman_numerals.divide('7','2').remainder
'I'
>>> roman_numerals.divide('7','2').value == roman_numerals.divide('6','2').value
False

```
