from src.squares import get_squares


def test_get_squares_returns_20_values():
    assert len(get_squares()) == 20


def test_get_squares_starts_and_ends_correctly():
    squares = get_squares()

    assert squares[0] == 1
    assert squares[-1] == 400


def test_get_squares_returns_all_expected_values():
    expected = [number**2 for number in range(1, 21)]

    assert get_squares() == expected
