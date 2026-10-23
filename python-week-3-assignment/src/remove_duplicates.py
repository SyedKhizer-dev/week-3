def remove_duplicates(numbers: list[int]) -> list[int]:
    """Remove duplicates while preserving the original order."""
    seen = set()
    result = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


if __name__ == "__main__":
    numbers = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    print(remove_duplicates(numbers))
