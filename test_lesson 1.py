from lettersnumber import count_letters, count_numbers


def test_count_letters_positiv():
    test_string = "Process finished with exit code 0"
    result = count_letters(test_string)
    assert result == 27, f"Expected 23 got '{result}' in {test_string}"


def test_count_letters_negativ():
    test_string = "!!!!###"
    result = count_letters(test_string)
    assert result == 0, f"Expected 0 got '{result}' in {test_string}"


if __name__ == "__main__":
    test_count_letters_positiv()
    test_count_letters_negativ()