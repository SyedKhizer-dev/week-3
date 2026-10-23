from src.remove_duplicates import remove_duplicates


def test_remove_duplicates_preserves_order():
    numbers = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

    assert remove_duplicates(numbers) == [12, 24, 35, 88, 120, 155]


def test_remove_duplicates_with_empty_list():
    assert remove_duplicates([]) == []


def test_remove_duplicates_with_no_duplicates():
    numbers = [1, 2, 3]

    assert remove_duplicates(numbers) == [1, 2, 3]
