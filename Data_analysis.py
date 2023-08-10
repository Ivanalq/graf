class TranslateToHours:
    def __init__(self, DataTime):
        self.DataTime = DataTime

    def translate_from_hours(self):
        start_time = self.DataTime[0]
        final_time_list = []
        for el in start_time:
            hour, minute = str(el).split('.')
            final_time = round((int(hour)*60 + int(minute))/60, 2)
            final_time_list.append(final_time)
        self.DataTime = [final_time_list, self.DataTime[1]]
        return self.DataTime


class DataAnalesBack:
    def __init__(self, DataTime):
        self.datatime = DataTime
        self.UNIQ_MONTHS = [key.split('.')[1] for key in self.datatime[1]]
        self.UNIQ_MONTHS = sorted(list(set(self.UNIQ_MONTHS)))
        self.AMOUNT_TIMES = [0] * len(self.UNIQ_MONTHS)

    def Month_analyse(self):
        for month in self.UNIQ_MONTHS:
            Index_month = 0
            for day in self.datatime[1]:
                if month in day:
                    self.AMOUNT_TIMES[self.UNIQ_MONTHS.index(month)] += self.datatime[0][Index_month]
                Index_month += 1
        return [self.AMOUNT_TIMES, self.UNIQ_MONTHS]

    def zero_days_analuze(self):
        for month in self.UNIQ_MONTHS:
            Index_month = 0
            for day in self.datatime[1]:
                if month in day and self.datatime[0][Index_month] == 0:
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
                    res_anal = DataAnalesBack(self.datatime).Month_analyse()
                    self.output_data.append(res_anal)
                if mod == 'Zero':
                    res_anal = DataAnalesBack(self.datatime).zero_days_analuze()
                    self.output_data.append(res_anal)
                if mod == 'Standart':
                    self.output_data.append(self.datatime)

        else:
            raise TypeError("Вы должны выбрать режим обработки данных!")

        return self.output_data



print(DataAnalysisView([[0,2,3,4,5], ['1.08', '2.08', '3.08', '1.09', '2.09']], ['Standart', 'Zero', 'Month']).AnalyseView())