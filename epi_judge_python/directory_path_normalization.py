from test_framework import generic_test


def shortest_equivalent_path(path):
		# TODO - you fill in here.
		s = []
		absolute_path = True if path[0] == '/' else False
		path_list = path.split('/')

		for item in path_list:
			if item in ('', '.'): continue
			elif (item == '..' and (len(s) == 0 or s[-1] == '..')) or item.isalnum():
				s.append(item)
			elif (item == '..' and len(s) != 0 ):
				s.pop()
		res = '/'.join(s)
		if res == '':
			return '/'
		if absolute_path:
			return '/' + res
		return res


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("directory_path_normalization.py",
																			 'directory_path_normalization.tsv',
																			 shortest_equivalent_path))
