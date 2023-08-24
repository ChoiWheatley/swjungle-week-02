class Bitset2D:
    bs: list[int]

    BUCKET_BITS = 32
    MAXN: int
    MAXM: int
    MAX_BUCKET_SIZE: int

    def __init__(self, MAXN: int, MAXM: int) -> None:
        self.MAXN = MAXN
        self.MAXM = MAXM
        self.MAX_BUCKET_SIZE: int = (MAXN * MAXM) // self.BUCKET_BITS + 1
        self.bs = [0 for _ in range(self.MAX_BUCKET_SIZE)]

    @classmethod
    def bucket_no(cls, idx: int) -> int:
        return idx // cls.BUCKET_BITS

    @classmethod
    def bucket_offset(cls, idx: int) -> int:
        return idx % cls.BUCKET_BITS

    def get(self, idx: int) -> bool:
        return self.bs[self.bucket_no(idx)] >> self.bucket_offset(idx) & 1 == 1

    def set(self, idx: int, to: bool = True):
        if to:
            self.bs[self.bucket_no(idx)] |= 1 << self.bucket_offset(idx)
        else:
            self.bs[self.bucket_no(idx)] ^= 1 << self.bucket_offset(idx)

    def get2d(self, row: int, col: int) -> bool:
        idx = row * self.MAXM + col
        return self.get(idx)

    def set2d(self, row: int, col: int, to: bool = True):
        idx = row * self.MAXM + col
        self.set(idx, to)
