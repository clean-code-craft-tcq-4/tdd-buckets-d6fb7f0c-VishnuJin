from current_sensors.a2d_12_bit_converter import A2D12Bit


def test_positive_is_input_range_valid():
    given_range = [0, 1000, 4000, 4094]
    expected_result = True
    actual_result = A2D12Bit.is_input_range_valid(given_range)
    assert expected_result == actual_result


def test_negative_is_input_range_valid():
    given_range = [0, 1000, 4000, 4095]
    expected_result = False
    actual_result = A2D12Bit.is_input_range_valid(given_range)
    assert expected_result == actual_result


def test_convert_a2d_12bit_range_to_amps():
    given_range = [1000, 1100, 1500, 2000]
    expected_result = [2, 3, 4, 5]
    actual_result = A2D12Bit(given_range).convert_a2d_12bit_range_to_amps()
    assert expected_result == actual_result
