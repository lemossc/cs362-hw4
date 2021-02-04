# Author:   Christopher LeMoss
# Date:     February 7, 2021
# Description:
#   1. Calculates the average of a list.
#   2. Returns 'None' if invalid side length.


def list_average(list):
    average = 0
    for element in list:
        if not is_number(element):
            return None
        else:
            average += element
    return average / len(list)


def is_number(value):
    if isinstance(value, int) or isinstance(value, float):
        return True
    else:
        return False
