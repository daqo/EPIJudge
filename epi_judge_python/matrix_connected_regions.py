from test_framework import generic_test


def flip_color(x, y, image):
    # TODO - you fill in here.
    def dfs(x, y):
    	if not (0 <= x < n and 0 <= y < n and image[x][y] == orig_color):
    		return
    	image[x][y] = 1 - orig_color
    	for next_x, next_y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
    		dfs(next_x, next_y)

    n = len(image)
    m = len(image[0])
    orig_color = image[x][y]
    dfs(x, y)




def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
