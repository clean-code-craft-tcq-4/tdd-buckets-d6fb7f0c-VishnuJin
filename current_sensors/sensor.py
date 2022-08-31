from abc import ABC, abstractclassmethod


class Sensor(ABC):
    @abstractclassmethod
    def convert_to_amps(self):
        raise NotImplementedError

    @classmethod
    def is_input_range_valid(self, range):
        return not (min(range) < 0 or max(range) > (pow(2, self.BITS) - 2))
