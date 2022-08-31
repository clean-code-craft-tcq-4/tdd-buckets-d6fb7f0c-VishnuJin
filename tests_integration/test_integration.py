import pytest
from current_range_monitor import get_continuous_ranges, convert_ranges_to_dict
from current_sensors.a2d_12_bit_converter import A2D12Bit
from current_sensors.a2d_10_bit_converter import A2D10Bit


@pytest.mark.parametrize(
    "given_range, expected_result",
    [
        (
            [3, 4, 3, 5, 10, 11, 12],
            [
                {"Range": "3-5", "Readings": 4},
                {"Range": "10-12", "Readings": 3},
            ],
        ),
        (
            A2D12Bit([1000, 1100, 1500, 2000]),
            [
                {"Range": "2-5", "Readings": 4},
            ],
        ),
        (
            A2D10Bit([900, 920, 1000, 1022, 0]),
            [
                {"Range": "11-12", "Readings": 2},
                {"Range": "14-15", "Readings": 3},
            ],
        ),
    ],
)
def test_positive_convert_ranges_to_dict(given_range, expected_result):
    continuous_range = get_continuous_ranges(given_range)
    assert convert_ranges_to_dict(continuous_range) == expected_result
