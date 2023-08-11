class TranslateToHours:
    """
    Класс, который должен преобразовать часы и минуты в формат обычного времени, то-беж из 60 ричной системы исчисления
    в 100 ричниую. Сначала переданный объект инициализируется в экземпляре класса, затем с помощью функции translate_from_hours
    объект переводится в сто-ричную систему исчисления. И затем возвращается проанализированное дата и время.
    """
    def __init__(self, DataTime):  # Получает на вход дату и время, и добавляет их в локальный экземпляр класса.
        self.DataTime = DataTime

    def translate_from_hours(self):
        """
        Переводит время в 100 ричную систему исчисления.
        :return: Словарь время/дата
        """
        start_hour = self.DataTime[0]  # Получает всё время.
        final_hours = []
        for item in start_hour:  # Перебирает все время, и потом делит его на минуты и часы.
            hour, minute = str(item).split('.')
            final_hour = (int(hour)*60 + int(minute))/60  # Получаем финальное время.
            final_hour = round(final_hour, 2)  # Округляем его до двух знаков после запятой.
            final_hours.append(final_hour)
        self.DataTime = [final_hours, self.DataTime[1]]  # Обновляет параметр DataTime.
        return self.DataTime


class DataAnalesBack:
    """
    Класс, который анализарует данные. Сначала инициализируются атрибуты. Атрибут UNIQ_MONTHS это уникальные месяцы.
    Методы:

    Month_analyse - Метод, который считает, сколько часов в месяц пользователь занимался. Сначала он перебирает все
    уникальные месяцы, дальше мы перебираем все дни, и если месяцы совпадают, то мы увеличиваем время в этом месяце.
    Возвращает список из списков дат и времени.

    zero_days_analuze - метод, который считает сколько дней пользователь ничего не дела. Сначала он перебирает все
    уникальные месяцы, затем перебирает все дни, и если месяцы совпадают, то мы добавляем 1 к дням, в которых ничего
    не делалось. Возвращает список из списков дат и времени.
    """
    def __init__(self, DataTime):
        self.datatime = DataTime
        # Получает все месяцы, и затем выбирает уникальные, и сохраняет как атрибут класса.
        self.UNIQ_MONTHS = [int(key.split('.')[1]) for key in self.datatime[1]]
        self.UNIQ_MONTHS = sorted(list(set(self.UNIQ_MONTHS)))

        # Список, который соответствует количеству уникальных месяцов.
        self.AMOUNT_TIMES = [0] * len(self.UNIQ_MONTHS)

    def Month_analyse(self):
        """
        Метод, который считает, сколько времени в месяц человек занимался
        :return: Возвращает список из списков дат и времени.
        """
        # Перебирает месяцы.
        for month in self.UNIQ_MONTHS:
            Index_month = 0

            # Перебирает все дни.
            for day in self.datatime[1]:

                # Если в дне есть месяц, то мы увеличиваем значение времени в месяце.
                if str(month) in day.split('.')[1]:
                    self.AMOUNT_TIMES[self.UNIQ_MONTHS.index(month)] += (self.datatime[0][Index_month])

                Index_month += 1
        return [self.AMOUNT_TIMES, self.UNIQ_MONTHS]

    def zero_days_analuze(self):
        """
        Метод, который считает количество дней, в которые не было времени работы.
        :return: Возвращает список из списков дат и времени
        """
        # Перебирает месяцы.
        for month in self.UNIQ_MONTHS:
            Index_month = 0

            # Перебирает все дни.
            for day in self.datatime[1]:

                # Если в дне есть месяц, и значение в этот день равно нулю, то мы добавляем еденицу, в месяц.
                if str(month) in day and self.datatime[0][Index_month] == 0:
                    self.AMOUNT_TIMES[self.UNIQ_MONTHS.index(month)] += 1
                Index_month += 1
        return [self.AMOUNT_TIMES, self.UNIQ_MONTHS]


class DataAnalysisView:
    """
    Класс, который распределяет данные по категориям, и затем возвращает их обработанными.
    Сначала в экземпляре класса инициализируются переданные ему параметры, и так же дополнительный параметр output_data,
    который нужен для дальнейшего вывода информации. Затем идет метод AnalyseView, который проверяет то, пустой ли список
    режимов, затем он перебирает все режимы анализа данных, в этом цикле есть фильтр, отбирающий режимы, и если режим подходит
    под условие, то он запускает определённый метод в класса DataAnalesBack, отвечающего за анализ данных, и потом полученный
    результат добавляется в список output_data. Возвращается список output_data.

    Методы:
    AnalyseView - преобразует информацию, и режимы в список с координатами графиков, и названиями режимов пред этим списком.
    """
    def __init__(self, DataTime, Analysis_modes):
        self.datatime = DataTime
        self.analysis_mode = Analysis_modes
        self.output_data = list()

    def AnalyseView(self):
        """
        Преобразует информацию, и режимы в список с координатами графиков, и названиями режимов пред этим списком.
        :return: Список со списками координат и названия режимов.
        """
        if len(self.analysis_mode) > 0:
            for mod in self.analysis_mode:  # Перебирает все режимы.

                # Если режим попадает под фильт, то выполняется вызов функции другого класса, и результат вызова этой
                # функции добавляется в переменную output_data

                if mod == 'Month':
                    result_analyse = DataAnalesBack(self.datatime).Month_analyse()
                    self.output_data.append({'Month mod': result_analyse})

                if mod == 'Zero':
                    result_analyse = DataAnalesBack(self.datatime).zero_days_analuze()
                    self.output_data.append({'Zero mod': result_analyse})

                if mod == 'Standart':
                    result_analyse = [self.datatime[0], [item for item in range(1, len(self.datatime[1]))]]
                    self.output_data.append({'Standart mod': result_analyse})

        return self.output_data
