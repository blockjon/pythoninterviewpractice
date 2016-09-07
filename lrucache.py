from collections import OrderedDict


class LRUCache(object):

    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = OrderedDict()

    def set(self, key, value):
        self.cache.pop(key, None)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.pop(self.cache.keys()[0])

    def get(self, key):
        if key not in self.cache:
            raise ValueError("Key {} not found".format(key))
        value = self.cache.pop(key, None)
        self.cache[key] = value
        return value


if __name__ == "__main__":
    cache = LRUCache(max_size=3)
    cache.set('a', 'apple')
    cache.set('b', 'banana')
    cache.set('c', 'carrot')

    cache.get('b')
    cache.get('a')
    cache.get('c')

    cache.set('d', 'dairy')

    assert cache.get('a') == 'apple'
    assert cache.get('c') == 'carrot'
    assert cache.get('d') == 'dairy'
    value_error_found = False
    try:
        cache.get('b')
    except ValueError:
        value_error_found = True
    assert value_error_found
    print "Done"
