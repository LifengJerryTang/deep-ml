import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = l2_norm(gradient)
	direction = [num / magnitude if magnitude != 0 else 0 for num in gradient]
	descent_dir = [-num for num in direction]

	return {
		"magnitude": magnitude,
		"direction" : direction,
		"descent_direction": descent_dir
	}

def l2_norm(vec: list):
	squared_sum = 0

	for num in vec:
		squared_sum += pow(num, 2)

	return pow(squared_sum, 1/2)