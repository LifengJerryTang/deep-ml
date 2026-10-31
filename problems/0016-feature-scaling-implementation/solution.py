import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	n,d = data.shape

	row_mean = data.mean(axis=0, keepdims=True)
	row_std = data.std(axis=0, keepdims=True)

	standardized_data = (data - row_mean) / row_std

	row_min = data.min(axis=0, keepdims=True)
	row_max = data.max(axis=0, keepdims=True)
	
	normalized_data = (data - row_min) / (row_max - row_min)
	
	return standardized_data, normalized_data