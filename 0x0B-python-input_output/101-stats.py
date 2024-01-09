#!/usr/bin/python3

"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def output_stats(size, stat_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(stat_codes):
        print("{}: {}".format(key, stat_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    stat_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                output_stats(size, stat_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if stat_codes.get(line[-2], -1) == -1:
                        stat_codes[line[-2]] = 1
                    else:
                        stat_codes[line[-2]] += 1
            except IndexError:
                pass

        output_stats(size, stat_codes)

    except KeyboardInterrupt:
        output_stats(size, stat_codes)
        raise
