# -*- coding: utf-8 -*-

class Palindrome:
    def _is_palindrome(self, integer):
        return str(integer) == str(integer)[::-1]

    def get_largest_palindrome_by_digit(self, digit):
        """
        normal pattern
        >>> P = Palindrome()
        >>> P.get_largest_palindrome_by_digit(2)
        9009

        abnormal pattern
        >>> P.get_largest_palindrome_by_digit(-1)
        this method needs number >= 1
        0
        """
        if digit < 1:
            print "this method needs number >= 1"
            return 0
        ret = 0
        low  = pow(10, digit - 1)
        high = pow(10, digit) - 1
        first  = high
        while low < first:
            second = high
            if first * second < ret:
                break
            while low < second:
                tmp_num = first * second
                if self._is_palindrome(tmp_num) and ret < tmp_num:
                    ret = tmp_num
                second -= 1
            first -= 1
        return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
