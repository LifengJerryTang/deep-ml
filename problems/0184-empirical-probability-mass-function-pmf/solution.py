def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    n = len(samples)
    count_map = {}

    result = []

    for num in samples:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1

    for key, value in count_map.items():
        result.append((key, value / n))

    return result
