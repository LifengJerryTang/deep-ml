import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n, d = data.shape

    random_indices = np.random.default_rng(seed).permutation(n)

    train_end = int(n * train_frac)

    validation_end = train_end + int(n * validation_frac)

    train_indices = random_indices[0:train_end]
    train_data = data[train_indices, :]

    validation_indices = random_indices[train_end: validation_end]
    validation_data = data[validation_indices, :]

    test_indices = random_indices[validation_end:]
    test_data = data[test_indices, :]

    return [train_data, validation_data, test_data]