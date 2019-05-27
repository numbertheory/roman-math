class Error(Exception):
   """Base class for other exceptions"""
   pass

class NotIntegerError(Error):
    """Only integers may be converted to Roman numerals."""
    pass

class ConvertToRomanNumerals():
    def __init__(self):
        pass

    def convert(self, integer_input):
        # Determine validity
        if not type(integer_input) is int:
            raise NotIntegerError
        # Find groups
        # Return Result

        if integer_input == (integer_input % 1000):
            pass
        return (integer_input)
