from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])

print d

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print od

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3

print od.keys()

class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last = False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

