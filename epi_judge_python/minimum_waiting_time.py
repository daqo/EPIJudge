from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    service_times.sort()
    waiting_time_for_ith_element = 0
    total_waiting_time = 0
    for i in range(1, len(service_times)):
        waiting_time_for_ith_element += service_times[i - 1]
        total_waiting_time += waiting_time_for_ith_element
    return total_waiting_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
