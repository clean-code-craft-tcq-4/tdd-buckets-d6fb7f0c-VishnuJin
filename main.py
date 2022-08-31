from current_range_monitor import show_charging_statistics
from current_sensors.a2d_12_bit_converter import A2D12Bit
from current_sensors.a2d_10_bit_converter import A2D10Bit

# integration tests are available

show_charging_statistics([3, 3, 5, 4, 10, 11, 12])
show_charging_statistics(A2D12Bit([1000, 1100, 1500, 2000]))
show_charging_statistics(A2D10Bit([900, 920, 1000, 1022, 0]))
