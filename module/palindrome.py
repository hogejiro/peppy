# -*- coding: utf-8 -*-

class Palindrome:
    def _is_palindrome(self, integer):
        return str(integer) == str(integer)[::-1]

    # 与えられた桁数の 2 つの数の積のうち、最大の回文数を求める
    def get_largest_palindrome_product_of_two_numbers_by_keta(self, keta):
        """
        normal pattern
        >>> P = Palindrome()
        >>> P.get_largest_palindrome_product_of_two_numbers_by_keta(2)
        9009

        abnormal pattern
        >>> P.get_largest_palindrome_product_of_two_numbers_by_keta(-1)
        this method needs number >= 1
        0
        """
        if keta < 1:
            print "this method needs number >= 1"
            return 0
        max = 0
        low  = pow(10, keta - 1)
        high = pow(10, keta) - 1
        for first in range(high + 1, low, -1): # [high, high-1, high-2, ... low]
            for second in range(high + 1, low, -1):
                if first * second < max:
                    break
                tmp_max = first * second
                if self._is_palindrome(tmp_max) and max < tmp_max:
                    max = tmp_max
        return max

if __name__ == "__main__":
    import doctest
    doctest.testmod()
