# -*- coding: utf-8 -*-

class Lattice:
    def __init__(self, n = 2, m = 2):
        self._m = m
        self._n = n
        return

    """
    n行 m列の格子の、左上から右下へ至る経路の個数を数える関数
    2*3 の場合、
    lattice = [
        [1,1,1,1], // 0行目
        [1,2,3,4], // 1行目
        [1,3,6,10] // 2行目
    ]
    の右下 (10) を返す
    """
    def count_lattice_paths(self,):
        """
        >>> L = Lattice(2, 3)
        >>> L.count_lattice_paths()
        10
        """
        self.initialize_lattice()
        self.increment_lattice()
        return self._lattice_paths[self._n][self._m]

    """
    2*3 の場合、
    lattice = [
        [1,1,1,1], // 0行目
        [1,], // 1行目
        [1,] // 2行目
    ]
    """
    def initialize_lattice(self,):
        """
        >>> L = Lattice(2, 3)
        >>> L.initialize_lattice()
        [[1, 1, 1, 1], [1], [1]]
        """
        # 0行目を 1 で初期化
        self._lattice_paths = []
        zeroth_row = [1,] * (self._m + 1) # [1,1,...]
        self._lattice_paths.append( zeroth_row )
        # 各行の0列目を 1 で初期化
        for i in range(1, self._n + 1): # i行目
            ith_row = [1,]
            self._lattice_paths.append(ith_row)
        return self._lattice_paths

    def increment_lattice(self,):
        """
        >>> L1 = Lattice(2, 3)
        >>> L1.initialize_lattice()
        [[1, 1, 1, 1], [1], [1]]
        >>> L1.increment_lattice()
        [[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10]]

        >>> L2 = Lattice(2, 2)
        >>> L2._lattice_paths = [[2, 2, 2], [2], [2]] # initialize with 2
        >>> L2.increment_lattice()
        [[2, 2, 2], [2, 4, 6], [2, 6, 12]]
        """
        for j in range(1, self._m + 1): # j列目の
            for i in range(1, self._n + 1): # i行目
                #print grid
                try:
                    # lattice[i][j] を追加
                    self._lattice_paths[i].append( self._lattice_paths[i-1][j] + self._lattice_paths[i][j-1] )
                except IndexError:
                    sys.stderr.write("There is something wrong in this algorithm!\n")
                    sys.stderr.write("Out of index: n:%d, m:%d\n" %(self._n, self._m))
                    sys.exit(1)
        return self._lattice_paths

if __name__ == "__main__":
    import doctest
    doctest.testmod()

