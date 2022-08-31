from current_sensors.sensor import Sensor


class A2D12Bit(Sensor):
    BITS = 12

    def __init__(self, range) -> None:
        if not self.is_input_range_valid(range):
            raise ValueError("Invalid Input")
        self.range = range

    def convert_a2d_12bit_range_to_amps(self):
        return [round(10 * value / 4094) for value in self.range]

    def convert_to_amps(self):
        return self.convert_a2d_12bit_range_to_amps()
