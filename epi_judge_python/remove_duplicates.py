import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name
    def __eq__(self, other):
        return self.first_name == other.first_name
    def __hash__(self):
        return hash(self.first_name)
    def __lt__(self, other):
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)


def eliminate_duplicate(A):
    # using sorting
    A.sort()
    write_idx = 1
    for i in range(1, len(A)):
        if A[i] != A[write_idx - 1]:
            A[write_idx] = A[i]
            write_idx += 1
    del A[write_idx:]
    
    # using sets
    # s = set(A)
    # write_idx = 0
    # for item in s:
    #     A[write_idx] = item
    #     write_idx += 1
    # del A[write_idx:]



@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([
        e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("remove_duplicates.py",
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
