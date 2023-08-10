from get_data import GetData
from Data_analysis import TranslateToHours



p = GetData('test')

res = p.get_data()
anal_data = TranslateToHours(res).translate_from_hours()


print(anal_data)







        