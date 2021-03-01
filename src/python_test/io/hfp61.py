def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs


def get_coach_data(filename):
    try:
        with open(filename)as f:
            data = f.readline()
        values = data.strip().split(",")
        return {"Name": values.pop(), "DOB": values.pop(), "Times": values}
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return None


sarah = get_coach_data("../../datasets/sarah2.txt")
sarah_dict = {"Name": sarah.pop(0), "DOB": sarah.pop(0), "Times": sarah}

print(sarah_dict['Name'] + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in sarah_dict["Times"]]))[0:3]))
