from test_framework import generic_test


def evaluate(expression):
    # TODO - you fill in here.
    DELIMETER = ','
    OPERATORS = {
    	'+': lambda y, x: x + y,
    	'-': lambda y, x: x - y,
    	'*': lambda y, x: x * y,
    	'/': lambda y, x: int(x / y)
    }
    s = []
    for item in expression.split(DELIMETER):
    	if item in OPERATORS:
    		s.append(OPERATORS[item](s.pop(), s.pop()))
    	else: s.append(int(item))
    return s[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
