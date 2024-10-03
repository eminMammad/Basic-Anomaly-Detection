def calculate_mean(data):
    """
    Calculate the mean of a list of numbers.

    Parameters:
    - data: A list of numbers.

    Returns:
    - The mean of the numbers.
    """
    return sum(data) / len(data)

def calculate_standard_deviation(data):
    """
    Calculate the standard deviation of a list of numbers.

    Parameters:
    - data: A list of numbers.

    Returns:
    - The standard deviation of the numbers.
    """
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5