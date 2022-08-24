def test_sort_range_in_ascending():
    given_range = [3, 3, 5, 4, 10, 11, 12]
    expected_range = [3, 3, 4, 5, 10, 11, 12]
    actual_output = sort_range_in_asscending(given_range)
    assert actual_output == expected_range


def test_get_continuous_ranges():
    given_range = [3, 3, 4, 5, 10, 11, 12]
    expected_range = [(3, 3, 4, 5), (10, 11, 12)]
    actual_output = get_continuous_ranges(given_range)
    assert actual_output == expected_range


def test_format_ranges_to_dict():
    given_range = [(3, 3, 4, 5), (10, 11, 12)]
    expected_output = [
        { "Range":"3-4", "Readings":4},
    { "Range":"10-12", "Readings":3}
    ]
    actual_output = format_ranges_to_dict(given_range)
    assert actual_output == expected_output
