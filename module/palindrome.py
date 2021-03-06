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
        ret = 0
        low  = pow(10, keta - 1)
        high = pow(10, keta) - 1
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
