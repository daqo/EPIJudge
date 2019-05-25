from test_framework import generic_test

import math
def find_salary_cap(target_payroll, current_salaries):
    # TODO - you fill in here.
    def is_good_candidate(candidate_cap):
    	running_sum = 0
    	for salary in current_salaries:
    		running_sum += min(salary, candidate_cap)
    	return running_sum <= target_payroll

    if target_payroll > sum(current_salaries):
    	return -1

    max_salary = max(current_salaries)
    max_cap = candidate_cap = 1
    left = candidate_cap
    right = max_salary
    while not math.isclose(left, right):
    	mid = (left + right) * 0.5
    	if is_good_candidate(mid):
    		max_cap = max(mid, max_cap)
    		left = mid
    	else:
    		right = mid
    return max_cap


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("find_salary_threshold.py",
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))