from {{cookiecutter.project_slug}}.example_function import add_two_values


def test_add_two_values() -> None:
    assert add_two_values(2, 3) == 5
