"""Tests for the example_function module."""

from {{cookiecutter.project_slug}}.example_function import add_two_values


EXPECTED_RESULT = 5


def test_add_two_values() -> None:
    """Test the add_two_values function."""
    assert add_two_values(2, 3) == EXPECTED_RESULT
