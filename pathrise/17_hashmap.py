class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        # If bucket is empty
        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            return True
        # If key is there
        for k, v in self.map[key_hash]:
            if k == key:
                v = value
                return True
        # If key is not there
        self.map[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return None
        
        for k, v in self.map[key_hash]:
            if k == key:
                return v

        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return
        
        for i, (k, v) in enumerate(self.map[key_hash]):
            if k == key:
                self.map.pop(i)
                return

    def _get_hash(self, key):
        return len(key)%self.size

if __name__ == "__main__":
    d = HashMap()
    d.add('Adnan', 1)
    d.add('Zulfikar', 2)
    d.add('Jumana', 3)
    d.add('Zulfukar', 4)
    for v in d.map:
        print(v)
    print(d.get("Zulfukar"))