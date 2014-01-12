# -*- coding: utf-8 -*-

class Fibonacci:
    def _generate_fib(self,):
        fib = [1, 2]
        idx = 1
        next = fib[0] + fib[1]
        while True:
            fib.append(next)
            idx  = idx + 1
            next = next + fib[idx - 1]
            yield fib[idx]

    def get_fibs_by_limit_number(self, limit_number):
        """
        normal pattern
        >>> F = Fibonacci()
        >>> F.get_fibs_by_limit_number(2)
        [1, 2]
        >>> F.get_fibs_by_limit_number(100)
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        abnormal pattern
        >>> F.get_fibs_by_limit_number(-1)
        this method needs number exceeds 2
        []
        """
        if int(limit_number) < 2:
            print "this method needs number >= 2"
            return []
        ret = [1, 2]
        fib = self._generate_fib()
        while True:
            next = fib.next()
            if next <= limit_number:
                ret.append(next)
                continue
            break
        return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
