# -*- coding: utf-8 -*-

class Prime:
    def _generate_prime(self,):
        primes = [2]
        p_candidate = 1
        while True:
            p_candidate = p_candidate + 2
            is_prime = True
            # p_candidate を素数で割っていく
            for p in primes:
                if p_candidate < p * p:
                    break
                if p_candidate % p == 0:
                    is_prime = False
                    break
            if is_prime:
                yield primes[-1]
                primes.append(p_candidate)

    """
    素数をn個小さい順に取得する
    """
    def get_n_primes(self, n):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_n_primes(1)
        [2]
        >>> P.get_n_primes(25)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        abnormal pattern
        >>> P.get_n_primes(-1)
        this method needs number >= 1
        []
        """
        if int(n) < 1:
            print "this method needs number >= 1"
            return []
        ret = []
        prime = self._generate_prime()
        for i in range(n):
            next = prime.next()
            ret.append(next)
        return ret

    def get_primes_by_upper_limit(self, upper_limit):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_primes_by_upper_limit(2)
        [2]
        >>> P.get_primes_by_upper_limit(100)
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        abnormal pattern
        >>> P.get_primes_by_upper_limit(-1)
        this method needs number >= 2
        []
        """
        if int(upper_limit) < 2:
            print "this method needs number >= 2"
            return []
        ret = []
        prime = self._generate_prime()
        next = prime.next()
        while next <= upper_limit:
            ret.append(next)
            next = prime.next()
        return ret

    # 与えられた数を素因数分解し、連想配列の形で返す
    # 2 以上の整数 a, b (a != b) と、素数 p, q (p != q) があるとして
    # n = (a ** p) * (b ** q) のとき、get_prime_factors(n) = {a: p, b: q}
    def get_prime_factors(self, n):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_prime_factors(2)
        {2: 1}
        >>> P.get_prime_factors(100)
        {2: 2, 5: 2}

        abnormal pattern
        >>> P.get_prime_factors(-1)
        this method needs number >= 2
        {}
        """
        if int(n) < 2:
            print "this method needs number >= 2"
            return {}
        ret = {}
        import math
        # use math.sqrt for speedup
        if n >= 4:
            n_sqrt = math.sqrt(n)
        else:
            n_sqrt = 2
        primes = self.get_primes_by_upper_limit(n_sqrt)
        n_orig = n
        for p in primes:
            if n == 1:
                break
            while n % p == 0:
                n /= p
                if p in ret:
                    ret[p] += 1
                else:
                    ret[p]  = 1
        if n == n_orig:
            # in this case, n is prime
            ret[n_orig] = 1
        elif n != 1:
            ret[n] = 1
        return ret

    # 与えられた数の約数の個数を求める
    def get_count_of_divisors(self, n):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_count_of_divisors(2)
        2
        >>> P.get_count_of_divisors(100)
        9

        abnormal pattern
        >>> P.get_count_of_divisors(-1)
        this method needs number >= 1
        0
        """
        if int(n) < 1:
            print "this method needs number >= 1"
            return 0
        if int(n) == 1:
            return 1
        # n = (a ** p) * (b ** q) * (c ** r) のとき、
        # n の約数は (p + 1) * (q + 1) * (r + 1) で求められる
        factors = self.get_prime_factors(n)
        powers = [v + 1 for v in factors.values()] # [p+1, q+1, r+1, ...]
        return reduce(lambda x, y: x * y, powers)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
