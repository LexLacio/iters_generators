def flat_generator(some_list):
    start_1 = 0
    while start_1 < len(some_list):
        start_2 = 0
        while start_2 < len(some_list[start_1]):
            yield some_list[start_1][start_2]
            start_2 += 1
        start_1 += 1


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
for item in flat_generator(nested_list):
    print(item)
