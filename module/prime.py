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
                primes.append(num)
                yield num

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
        if int(limit_number) < 1:
            print "this method needs number >= 2"
            return []
        ret = [2]
        prime  = self._generate_prime()
        while True:
            next = prime.next()
            if next > limit_number:
                break
            ret.append(next)
        return ret

    def get_prime_factors_by_limit_number(self, limit_number):
        """
        normal pattern
        >>> P = Prime()
        >>> P.get_prime_factors_by_limit_number(2)
        {2: 1}
        >>> P.get_prime_factors_by_limit_number(100)
        {2: 2, 5: 2}

        abnormal pattern
        >>> P.get_prime_factors_by_limit_number(-1)
        this method needs number >= 2
        {}
        """
        if int(limit_number) < 1:
            print "this method needs number >= 2"
            return {}
        ret = {}
        import math
        # use math.sqrt for speedup
        primes = self.get_primes_by_limit_number(math.sqrt(limit_number))
        num = limit_number
        for p in primes:
            if num == 1:
                break
            while num % p == 0:
                num /= p
                if p in ret:
                    ret[p] = ret[p] + 1
                else:
                    ret[p] = 1
        if num == limit_number:
            # in this case, limit_number is prime
            ret[limit_number] = 1
        return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
