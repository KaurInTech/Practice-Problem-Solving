class TimeMap:

    def __init__(self):
        self.mapping = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = []
        self.mapping[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.mapping:
            values = self.mapping[key]
        else:
            return ""
        l = 0
        r = len(values)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res
        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)