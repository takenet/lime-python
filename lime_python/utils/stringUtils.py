# String Utility
# Gabriel R Santos (@chr0m1ng)


class StringUtils():
    """Helper class to handle strings"""

    def IsNoneOrEmpty(string):
        """ Check if string is None or Empty."""
        return string is None or string.isspace()
