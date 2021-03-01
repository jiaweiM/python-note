def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs


class AthleteList(list):
    def __init__(self, name, dob=None, times=None):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(item) for item in self]))[0:3]

    def add_time(self, time):
        self.append(time)

    def add_times(self, times):
        self.extend(times)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            value = f.readline()
            values = value.strip().split(",")
            return AthleteList(values.pop(0), values.pop(0), values)
    except IOError as ioerror:
        print("File error: " + str(ioerror))
        return None


sarah = get_coach_data("../../datasets/sarah2.txt")
james = get_coach_data("../../datasets/james2.txt")
julie = get_coach_data("../../datasets/julie2.txt")
mikey = get_coach_data("../../datasets/mikey2.txt")

print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
