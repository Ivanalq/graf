import dearpygui.dearpygui as dpg
from get_data import GetData
from Data_analysis import TranslateToHours, DataAnalysisView


class App:
    COUNT = 0
    SELECTED_MODS = []
    PATH_TO_FILE = ''

    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title='Analuse Time', width=800, height=900)

        with dpg.window(label='Primary Window', width=800, height=900):
            dpg.add_text('Choise mod')
            dpg.add_checkbox(label='Zero', user_data="Zero", callback=self.add_to_mods)
            dpg.add_checkbox(label='Month', user_data="Month", callback=self.add_to_mods)
            dpg.add_checkbox(label='Standart', user_data="Standart", callback=self.add_to_mods)

            dpg.add_text('Choise file')

            with dpg.file_dialog(directory_selector=False, show=False, callback=self.select_file, file_count=3,
                                 tag='file-dilig-tag', width=700, height=400):
                dpg.add_file_extension("", color=(0, 150, 150, 255))
                dpg.add_file_extension(".*", color=(170, 0, 150, 255))
                dpg.add_button(label="Fancy File dilog")

            dpg.add_button(label="file selector", callback=lambda: dpg.show_item("file-dilig-tag"))

            dpg.add_button(label='Start Generation Grath', callback=self.confirm)

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def add_to_mods(self, sender, app_data, user_data):
        if user_data not in self.SELECTED_MODS:
            self.SELECTED_MODS.append(user_data)
        else:
            self.SELECTED_MODS.remove(user_data)

    def select_file(self, sender, app_data):
        # Получает переменную с данными, и затем извлекает из нее путь к выбранному файлу
        data = list(app_data.values())
        data = list(data[-1].values())
        self.PATH_TO_FILE = data[0]

    def confirm(self, sender, user_data):
        global count
        p = GetData(self.PATH_TO_FILE)
        res = p.get_data()
        anal_data = TranslateToHours(res).translate_from_hours()
        beta_finish_data = DataAnalysisView(anal_data, self.SELECTED_MODS).AnalyseView()

        for data in beta_finish_data:
            print(data)
            self.draw_a_graph(list(data.keys())[0], self.COUNT, )
            self.COUNT += 1

    @staticmethod
    def draw_a_graph(arr, name, count):
        sindatax, sindatay = list(arr.values())[0][1], list(arr.values())[0][0]
        with dpg.window(label="Tutorial"):
            with dpg.plot(label="Line Series", height=700, width=800):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvDatePickerLevel_Day, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", tag=str(count))
                print(dpg)
                dpg.add_line_series(sindatax, sindatay, label=name, parent=str(count))







p = App()
