# Author:   Christopher LeMoss
# Date:     February 7, 2021
# Description:
#   1. Calculates the volume of a cube.
#   2. Returns 'None' if invalid side length.

# Calculate volume of a cube
def volume(side_length):
    if is_number(side_length) and side_length > 0:
        return side_length * side_length * side_length
    else:
        return None


def is_number(value):
    if isinstance(value, int) or isinstance(value, float):
        return True
    else:
        return False
