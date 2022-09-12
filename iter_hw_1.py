class FlatIterator:

    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.cursor = 0
        self.cursor_2 = - 1
        return self

    def __next__(self):
        self.cursor_2 += 1
        if self.cursor_2 >= len(self.some_list[self.cursor]):
            self.cursor += 1
            self.cursor_2 = 0
            if self.cursor >= len(self.some_list):
                raise StopIteration
        return self.some_list[self.cursor][self.cursor_2]


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
for item in FlatIterator(nested_list):
    print(item)

# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)
