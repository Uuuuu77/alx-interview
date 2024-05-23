#!/usr/bin/env python3

""" UTF-8 Validation """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    def get_byte_count(first_byte):
        if first_byte & 0b11110000 == 0b11110000:
            return 4
        elif first_byte & 0b11100000 == 0b11100000:
            return 3
        elif first_byte & 0b11100000 == 0b11000000:
            return 2
        else:
            return 1

        x = 0
        n = len(data)

        while x < n:
            current_byte = data[x]

            # Number of bytes in the current UTF-8 character.
            span = get_byte_count(current_byte)

            if span == 1:
                # Single-byte character.
                if current_byte > 0x7F:
                    return False
            else:
                # Multi-byte character.
                if n - x < span:
                    return False

                for y in range(x + 1, x + span):
                    if not (0x80 <= data[y] <= 0xBF):
                        return False

                x += span - 1

            x += 1

        return True
