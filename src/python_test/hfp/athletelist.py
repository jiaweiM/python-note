class AthleteList(list):
    def __init__(self, name, dob=None, times=None):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return time_string
        (mins, secs) = time_string.split(splitter)
        return mins + "." + secs

    @property
    def top3(self):
        return sorted(set([self.sanitize(item) for item in self]))[0:3]

    @property
    def clean_data(self):
        return sorted(set([self.sanitize(item) for item in self]))

    def add_time(self, time):
        self.append(time)

    def add_times(self, times):
        self.extend(times)
