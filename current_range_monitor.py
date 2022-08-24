from itertools import groupby
from turtle import st


def sort_range_in_ascending(_range):
    return sorted(_range)


def get_continuous_ranges(_range):

    range_splits = []
    sorted_range = sort_range_in_ascending(_range)
    for range_start, range_end in get_range_intervals(_range):
        first_index = sorted_range.index(range_start)
        last_index = len(sorted_range) - 1 - sorted_range[::-1].index(range_end)
        range_splits.append(tuple(sorted_range[first_index : last_index + 1]))
    return range_splits


def get_range_intervals(_range):
    continuous_ranges = []
    for _, readings in groupby(enumerate(set(_range)), lambda a: a[1] - a[0]):
        readings = list(readings)
        continuous_ranges.append((readings[0][1], readings[-1][1]))
    return continuous_ranges


def convert_ranges_to_dict(_range):
    return [{"Range": f"{i[0]}-{i[-1]}", "Readings": len(i)} for i in _range]


def output_ranges_as_csv(stats, writer=print):
    writer(stats)


def print_as_csv_to_console(stats):
    print("Range, Readings")
    for stat in stats:
        print(f"{stat['Range']}, {stat['Readings']}")


def show_charging_statistics(measurements):
    continuous_range = get_continuous_ranges(measurements)
    output_ranges_as_csv(
        convert_ranges_to_dict(continuous_range), print_as_csv_to_console
    )

