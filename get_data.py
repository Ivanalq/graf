class GetData:
    """
    Получает путь к файлу, затем генерирует список, состоящий из списков координат осей х и у.
    Методы:
    get_data - Получает путь к файлу, и затем преобразует его в формат два списка - дата и время в этот день. Затем
    возвращает этот список
    """
    def __init__(self, path_to_file):
        """
        Инициализирует дополнительные переменные.
        :param path_to_file: Путь к файлу
        """
        self.times_list = list()
        self.days_list = list()
        self.path_to_file = path_to_file

    def get_data(self):
        """
        Узнает количество строк в документе, затем проходит его, читая строку, и разделяя её на время и дату, и затем
        добавляет их в списки координат.
        После проделанных манипуляций возвращает список с координатами родительского графика.
        :return: Координаты родительского графика
        """

        # Считает количество строк в документе.
        with open(self.path_to_file) as data:
            COUNT_LINES = sum(1 for _ in data)

        # Перебирает все строки и формирует два списка с координатами, затем их выводит.
        with open(self.path_to_file) as data2:
            COUNT = 0
            while COUNT < COUNT_LINES:
                COUNT += 1
                TimeDay = data2.readline().split()  # Получает строку, в которой находится дата и время.
                time, day = TimeDay[0], TimeDay[1]  # Из этой строки получает дату и время.
                self.times_list.append(time)
                self.days_list.append(day)
            return [self.times_list, self.days_list]  # Возвращает список координат родительского класса.
