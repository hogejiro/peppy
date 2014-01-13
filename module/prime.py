# -*- coding: utf-8 -*-

class Prime:
    def _generate_prime(self,):
        primes = [2]
        num = 1
        while True:
            num = num + 2
            is_prime = True
            for p in primes:
                if num < p * p:
                    break
                if num % p == 0:
                    is_prime = False
                    break
            if is_prime:
                yield primes[-1]
                primes.append(num)

    def get_primes_by_index(self, index):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_primes_by_index(1)
        [2]
        >>> P.get_primes_by_index(25)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        abnormal pattern
        >>> P.get_primes_by_index(-1)
        this method needs number >= 1
        []
        """
        if int(index) < 1:
            print "this method needs number >= 1"
            return []
        ret = []
        prime = self._generate_prime()
        i = 0
        while i < index:
            next = prime.next()
            ret.append(next)
            i += 1
        return ret

    def get_primes_by_limit_number(self, limit_number):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_primes_by_limit_number(2)
        [2]
        >>> P.get_primes_by_limit_number(100)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        abnormal pattern
        >>> P.get_primes_by_limit_number(-1)
        this method needs number >= 2
        []
        """
        if int(limit_number) < 2:
            print "this method needs number >= 2"
            return []
        ret = []
        prime = self._generate_prime()
        next = prime.next()
        while next <= limit_number:
            ret.append(next)
            next = prime.next()
        return ret

    # 与えられた数を素因数分解し、連想配列の形で返す
    # 2 以上の整数 a, b (a != b) と、素数 p, q (p != q) があるとして
    # n = (a ** p) * (b ** q) のとき、get_prime_factors_by_number(n) = {a: p, b: q}
    def get_prime_factors_by_number(self, number):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_prime_factors_by_number(2)
        {2: 1}
        >>> P.get_prime_factors_by_number(100)
        {2: 2, 5: 2}

        abnormal pattern
        >>> P.get_prime_factors_by_number(-1)
        this method needs number >= 2
        {}
        """
        if int(number) < 2:
            print "this method needs number >= 2"
            return {}
        ret = {}
        import math
        # use math.sqrt for speedup
        if number >= 4:
            number_sqrt = math.sqrt(number)
        else:
            number_sqrt = 2
        primes = self.get_primes_by_limit_number(number_sqrt)
        num = number
        for p in primes:
            if num == 1:
                break
            while num % p == 0:
                num /= p
                if p in ret:
                    ret[p] = ret[p] + 1
                else:
                    ret[p] = 1
        if num == number:
            # in this case, number is prime
            ret[number] = 1
        elif num != 1:
            ret[num] = 1
        return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
