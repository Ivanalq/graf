from get_data import GetData
from Data_analysis import TranslateToHours, DataAnalysisView

anales_mode = ['Month']

p = GetData('/Users/ivanalejnikov/PycharmProjects/Построение графика учебы/test')

res = p.get_data()
anal_data = TranslateToHours(res).translate_from_hours()
beta_finish_data = DataAnalysisView(anal_data, anales_mode).AnalyseView()

print(beta_finish_data)








        