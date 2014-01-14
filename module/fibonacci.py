# -*- coding: utf-8 -*-

class Fibonacci:
    def _generate_fib(self,):
        fib = [1, 2]
        next = fib[-1] + fib[-2]
        while True:
            fib.append(next)
            next = fib[-1] + fib[-2]
            yield fib[-1]

    def get_fibs_by_upper_limit(self, upper_limit):
        """
        normal pattern
        >>> F = Fibonacci()
        >>> F.get_fibs_by_upper_limit(2)
        [1, 2]
        >>> F.get_fibs_by_upper_limit(100)
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        abnormal pattern
        >>> F.get_fibs_by_upper_limit(-1)
        this method needs number >= 2
        []
        """
        if int(upper_limit) < 2:
            print "this method needs number >= 2"
            return []
        ret = [1, 2]
        fib = self._generate_fib()
        next = fib.next()
        while next <= upper_limit:
            ret.append(next)
            next = fib.next()
        return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
