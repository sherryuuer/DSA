# https://leetcode.com/problems/design-hashset/description/
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
class MyHashSet(object):

    def __init__(self):
        self.set = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.set:
            return
        self.set.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.set:
            self.set.remove(key)
        return

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.set:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# OR
class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashset else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
