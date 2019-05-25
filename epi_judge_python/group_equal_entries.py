import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))

import collections
def group_by_age(people):
    # TODO - you fill in here.
    h = collections.defaultdict(int)
    for i, person in enumerate(people):
        h[person.age] += 1
    offset = collections.defaultdict(collections.deque)

    i = 0
    for k, v in h.items():
        offset[k].extend(list(range(i, i + v)))
        i += v

    j = 0
    while j < len(people):
        person = people[j]
        if offset[person.age]:            
            ind = offset[person.age].popleft()
            if ind == j:
                j += 1
            else:
                people[j], people[ind] = people[ind], people[j]
        else:
            j += 1

@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0]

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("group_equal_entries.py",
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
