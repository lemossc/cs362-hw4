# Author:   Christopher LeMoss
# Date:     February 7, 2021
# Description:
#   Returns a full name when given a first and last name.


def get_full_name(first_name, last_name):
    if isinstance(first_name, str) and isinstance(last_name, str) and \
            len(first_name) > 0 and len(last_name):
        return first_name + " " + last_name
    else:
        return None
