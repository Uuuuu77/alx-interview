#!/usr/bin/python3

""" Log parsing """

import sys


if __name__ == '__main__':

    Fsize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {x: 0 for x in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """ It print the stats """
        print("File size: {:d}".format(Fsize))
        for x, y in sorted(stats.items()):
            if y:
                print("{}: {}".format(x, y))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                statusCode = data[-2]
                if statusCode in stats:
                    stats[statusCode] += 1
            except BaseException:
                pass

            try:
                Fsize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, Fsize)
        print_stats(stats, Fsize)
    except KeyboardInterrupt:
        print_stats(stats, Fsize)
        raise
