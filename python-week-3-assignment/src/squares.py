def get_squares() -> list[int]:
    """Return squares of integers from 1 through 20."""
    return list(map(lambda number: number**2, range(1, 21)))  # noqa: C417


if __name__ == "__main__":
    print(get_squares())
