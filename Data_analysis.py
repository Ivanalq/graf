class TranslateToHours:
    """
    Класс, который должен преобразовать часы и минуты в формат обычного времени, то-беж из 60 ричной системы исчисления
    в 100 ричниую.
    """
    def __init__(self, DataTime):  # Получает на вход дату и время, и добавляет их в локальный экземпляр класса.
        self.DataTime = DataTime

    def translate_from_hours(self):  # Функция, которая переводит часы в правильный формат.
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
    def __init__(self, DataTime):
        self.datatime = DataTime
        self.UNIQ_MONTHS = [int(key.split('.')[1]) for key in self.datatime[1]]
        self.UNIQ_MONTHS = sorted(list(set(self.UNIQ_MONTHS)))
        self.AMOUNT_TIMES = [0] * len(self.UNIQ_MONTHS)

    def Month_analyse(self):
        for month in self.UNIQ_MONTHS:
            Index_month = 0
            for day in self.datatime[1]:
                if str(month) in day.split('.')[1]:
                    self.AMOUNT_TIMES[self.UNIQ_MONTHS.index(month)] += (self.datatime[0][Index_month])

                Index_month += 1
        return [self.AMOUNT_TIMES, self.UNIQ_MONTHS]

    def zero_days_analuze(self):
        for month in self.UNIQ_MONTHS:
            Index_month = 0
            for day in self.datatime[1]:
                if str(month) in day and self.datatime[0][Index_month] == 0:
                    self.AMOUNT_TIMES[self.UNIQ_MONTHS.index(month)] += 1
                Index_month += 1
        return [self.AMOUNT_TIMES, self.UNIQ_MONTHS]


class DataAnalysisView:
    def __init__(self, DataTime, Analysis_modes):
        self.datatime = DataTime
        self.analysis_mode = Analysis_modes
        self.output_data = list()

    def AnalyseView(self):
        if len(self.analysis_mode) > 0:
            for mod in self.analysis_mode:
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
