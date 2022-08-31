from current_sensors.sensor import Sensor


class A2D10Bit(Sensor):
    BITS = 10

    def __init__(self, range) -> None:
        if not self.is_input_range_valid(range):
            raise ValueError("Invalid Input")
        self.range = range

    def convert_a2d_10bit_range_to_amps(self):
        return [abs(round(((15 * value / 1022) - 7.5) * 2)) for value in self.range]

    def convert_to_amps(self):
        return self.convert_a2d_10bit_range_to_amps()
