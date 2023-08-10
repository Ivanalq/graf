
class GetData:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
    
    def get_data(self):
        with open(self.path_to_file) as data:
            COUNT_LINES = sum(1 for line in data)

            count = 0
            times = []
            days = []


            print(data.readline())


p = GetData('test.txt')
p.get_data()






        