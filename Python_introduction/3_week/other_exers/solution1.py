class Matrix:
    def __init__(self, max_size=1000):
        if max_size < 1:
            raise ValueError("Size shoud be more than 0")
        self._size = 1
        self._data = [None]
        self._last_index = 0
        self._max_size = max_size
    
    def _empty(self):
        if self._size == 1 and self._last_index == 0:
            return True
        return False

    def _full(self):
        if self._size == self._max_size and self._last_index == self._size**2:
            return True
        else:
            return False
    
    def _pop_need_resize(self):
        if self._last_index == (self._size - 2) * (self._size - 1):
            if self._size > 1:
                return True
        return False

    def _pop_resize(self):
        self._size -= 1
        self._data = self._data[:self._size**2:]

    def _append_need_resize(self):
        if self._last_index == self._size * (self._size - 1):
            if self._size < self._max_size:
                return True
        return False
    
    def _append_resize(self):
        self._size += 1
        self._data.extend([None for _ in range(2 * self._size - 1)])


    def append(self, element=None):
        if element == None:
            return None
        if self._full():
            raise IndexError("Full matrix append")
        if self._append_need_resize():
            self._append_resize()
        self._data[self._last_index] = element
        self._last_index += 1


    def pop(self):
        if self._empty():
            raise IndexError("Empty matrix pop")
        self._last_index -= 1
        answer = self._data[self._last_index]
        self._data[self._last_index] = None
        if self._pop_need_resize():
            self._pop_resize()
        return answer


    def __str__(self):
        string = ""
        for i in range(self._size):
            if i:
                string += '\n'
            for j in range(self._size):
                if j:
                    string += ' '
                string += str(self._data[i*self._size + j])
        return string

    @classmethod
    def from_iter(cls, iter_obj, max_size=1000):
        obj = cls(max_size)
        for num in iter_obj:
            obj.append(num)
        return obj