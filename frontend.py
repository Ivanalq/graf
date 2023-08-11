import dearpygui.dearpygui as dpg
from get_data import GetData
from Data_analysis import TranslateToHours, DataAnalysisView

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=900)


a = []
count = 0
def to_id(sender, app_data, user_data):

    if user_data not in a:
        a.append(user_data)
    else:
        a.remove(user_data)
    print(a)

def confirm(sender, user_data):
    global count
    p = GetData('test')
    res = p.get_data()
    anal_data = TranslateToHours(res).translate_from_hours()
    beta_finish_data = DataAnalysisView(anal_data, a).AnalyseView()

    for data in beta_finish_data:
        print(data)
        draw_stabdart_gratf(data, data.keys(), count)
        count += 1








with dpg.window(label='Group Buttns'):
    dpg.add_text('Choise mod')
    dpg.add_checkbox(label='Zero', user_data="Zero", callback=to_id)
    dpg.add_checkbox(label='Month', user_data="Month", callback=to_id)
    dpg.add_checkbox(label='Standart', user_data="Standart", callback=to_id)
    dpg.add_button(label='start', callback=confirm)





def draw_stabdart_gratf(arr, name, count):
    sindatax, sindatay = list(arr.values())[0][1], list(arr.values())[0][0]
    print(sindatay)
    with dpg.window(label="Tutorial"):
        # create plot
        with dpg.plot(label="Line Series", height=700, width=800, tracked=True):

            dpg.add_plot_legend()

            dpg.add_plot_axis(dpg.mvDatePickerLevel_Day, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag=str(count))
            print(dpg)
            dpg.add_line_series(sindatax, sindatay, label=name, parent=str(count))



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()