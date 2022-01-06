# for num in range(1, 10):
#     print(num)

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration


first_range = MyRange(14, 30)
for number in first_range:
    print(number)

