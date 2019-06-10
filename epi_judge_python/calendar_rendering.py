import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A):
    # TODO - you fill in here.
    endpoints = []
    for start, finish in A:
        endpoints.append(Endpoint(start, True))
        endpoints.append(Endpoint(finish, False))
    endpoints.sort(key=lambda e: (e.time, not e.is_start))

    global_num_concurrent_events = num_concurrent_events = 0
    for endpoint in endpoints:
        if endpoint.is_start:
            num_concurrent_events += 1
            global_num_concurrent_events = max(global_num_concurrent_events, num_concurrent_events)
        else:
            num_concurrent_events -= 1
    return global_num_concurrent_events


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
