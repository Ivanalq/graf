class GetData:
    def __init__(self, path_to_file):
        self.times_list = list()
        self.days_list = list()
        self.path_to_file = path_to_file

    def get_data(self):
        with open(self.path_to_file) as data:
            COUNT_LINES = sum(1 for line in data)

        with open(self.path_to_file) as data2:
            COUNT = 0
            while COUNT < COUNT_LINES:
                COUNT += 1
                TimeDay = data2.readline().split()
                time, day = TimeDay[0], TimeDay[1]
                self.times_list.append(time)
                self.days_list.append(day)
            return [self.times_list, self.days_list]