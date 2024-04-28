class TimeMap(object):

    def __init__(self):
        self.values_dict = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.values_dict:
            self.values_dict[key] = []
        self.values_dict[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        values = self.values_dict.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
                res = values[mid][1]
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("fo1", "v1", 1)
obj.set("fo1", "v2", 2)
print(obj.get("fo1", 1))
