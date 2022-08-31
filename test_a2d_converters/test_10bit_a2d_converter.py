from current_sensors.a2d_10_bit_converter import A2D10Bit


def test_positive_is_input_range_valid():
    given_range = [0, 1022, 511]
    expected_result = True
    actual_result = A2D10Bit.is_input_range_valid(given_range)
    assert expected_result == actual_result


def test_negative_is_input_range_valid():
    given_range = [0, 1023, 511, 1025]
    expected_result = False
    actual_result = A2D10Bit.is_input_range_valid(given_range)
    assert expected_result == actual_result


def test_convert_a2d_12bit_range_to_amps():
    given_range = [0, 1022, 511]
    expected_result = [15, 15, 0]
    actual_result = A2D10Bit(given_range).convert_a2d_10bit_range_to_amps()
    assert expected_result == actual_result
