class DBUtils:
    def __init__(self):
        self.swaps = None
        self.base = None
        self.future = None
        self.pools = None

    def get_swaps(self):
        return self.swaps

    def get_pools(self):
        return self.pools

    def get_future(self):
        return self.future

    def set_tables(self, swaps, pools, future):
        self.swaps = swaps
        self.pools = pools
        self.future = future

    def set_base(self, base):
        self.base = base


db_utils = DBUtils()
