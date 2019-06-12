import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    task_durations.sort()
    res = []
    for i in range(len(task_durations) // 2):
        res.append((task_durations[i], task_durations[len(task_durations) - 1 - i]))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))
