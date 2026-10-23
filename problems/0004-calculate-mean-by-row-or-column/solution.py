def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	res = []

	if mode == "column":
		for i in range(len(matrix[0])):
			col = get_col(matrix, i)
			res.append(mean_of_arr(col))

	else:
		for i in range(len(matrix)):
			res.append(mean_of_arr(matrix[i]))

	return res


def mean_of_arr(arr: list[float]):
	return sum(arr) / len(arr)

def get_col(matrix: list[list[float]], index):
	col = []

	for arr in matrix:
		col.append(arr[index])

	return col