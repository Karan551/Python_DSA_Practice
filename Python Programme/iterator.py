# Create an iterator
class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.sequence):
            item = self.sequence[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


# We can get all items value for one item if we want to get item for second
# time this will empty, so we will get empty object.
iterable = Sequence([5, 13, 55, 80, 44, 23])
# print(tuple(iterable))
# for i in iterable:
#     print(i)
print('This is an iterable object:', tuple(iterable))
a = range(5)


# print(tuple(a))


class Show:
    def __init__(self, end=None, start=0, step=1):
        self.start = start
        self.end = end
        self.step = step

    def printObject(self):
        # while self.start < self.end:
        #     item = self.start
        #     print(item, end=' ')
        #     item += self.step
        #     self.start += 1
        print(self.start)
        print(self.end)
        print(self.step)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            item = self.start
            if self.start < self.end:
                # print(item, end=' ')
                item = item + self.step
                # item += self.step
                self.start += 1
                return item
        else:
            raise StopIteration


a = Show(5, 0, 2)
a.printObject()
print(tuple(a))
