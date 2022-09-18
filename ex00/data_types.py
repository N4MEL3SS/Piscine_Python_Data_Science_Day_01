#!/usr/bin/env python3

def data_types():
    variables = [0, '', 0.0, False, [], dict(), (), set()]
    variables_type_list = [type(elem).__name__ for elem in variables]
    print(str(variables_type_list).replace("'", ""))


if __name__ == '__main__':
    data_types()

# Output:
# [int, str, float, bool, list, dict, tuple, set]
