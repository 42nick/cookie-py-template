"""Example function module."""


def add_two_values(val1: float, val2: float) -> int | float:
    """Add two values.

    It is only here to show you that this text will be also found in the documentation.

    Args:
        val1 (Union[int, float]): First input argument.
        val2 (Union[int, float]): Second input argument.

    Returns:
        Union[int, float]: Sum of val1 and val2.
    """
    return val1 + val2
