def sanitize(time_string):
    """
    replace splitter to '.'
    """
    if '-' in time_string:
        spliter = '-'
    elif ':' in time_string:
        spliter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(spliter)
    return mins + '.' + secs


def open_data(file):
    with open(file) as afile:
        line = afile.readline().strip()
        values = line.split(",")
        lst = [sanitize(item) for item in values]
    return lst


def deduplicate(lst):
    unique_values = []
    for item in lst:
        if item not in unique_values:
            unique_values.append(item)
    return unique_values


james = open_data("../../datasets/james.txt")
julie = open_data("../../datasets/julie.txt")
mikey = open_data("../../datasets/mikey.txt")
sarah = open_data("../../datasets/sarah.txt")

james.sort()
julie.sort()
mikey.sort()
sarah.sort()

james = deduplicate(james)
julie = deduplicate(julie)
mikey = deduplicate(mikey)
sarah = deduplicate(sarah)

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])
