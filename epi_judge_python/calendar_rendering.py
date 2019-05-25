import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

def find_max_simultaneous_events(A):
    # TODO - you fill in here.
    E = []
    for start, finish in A:
    	E.append((start, True))
    	E.append((finish, False))
    E.sort(key=lambda e: (e[0], not e[1]))
    local_max = global_max = 0
    for e in E:
    	if e[1]:
    		local_max += 1
    		global_max = max(global_max, local_max)
    	else:
    		local_max -= 1
    return global_max


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
