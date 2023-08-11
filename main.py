from get_data import GetData
from Data_analysis import TranslateToHours, DataAnalysisView

anales_mode = ['Zero']

p = GetData('test')

res = p.get_data()
anal_data = TranslateToHours(res).translate_from_hours()
finish_data = DataAnalysisView(anal_data, anales_mode).AnalyseView()


print(finish_data)







        