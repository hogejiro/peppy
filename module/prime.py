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
        while True:
            next = prime.next()
            if i >= index:
                break
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
        if int(limit_number) < 2:
            print "this method needs number >= 2"
            return {}
        ret = {}
        import math
        # use math.sqrt for speedup
        if limit_number >= 4:
            limit_number_sqrt = math.sqrt(limit_number)
        else:
            limit_number_sqrt = 2
        primes = self.get_primes_by_limit_number(limit_number_sqrt)
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
        elif num != 1:
            ret[num] = 1
        return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
