class Forest(object):
    def __init__(self):
        self.list = []

    def add_set(self, new_set):
        self.list.append(new_set)

    def merge_sets(self, set1, set2):
        new_set = set1+set2
        self.list.remove(set1)
        self.list.remove(set2)
        self.list.append(new_set)

    def set_in_forest(self, set):
        if set in self.list:
            return True
        else:
            return False

transformations = [[1, 2], [1, 3], [2, 7], [3, 1], [4, 5], [6, 8], [9, 6], [10, 5]]
F = Forest()

for t in transformations:
    
