import dearpygui.dearpygui as dpg
from get_data import GetData
from Data_analysis import TranslateToHours, DataAnalysisView


class App:
    """
    Класс, который является оболочкой всего приложения, внутри его расположены все компоненты, написанные ранее.
    Является главным звеном всего приложения.
    Вначале объявляются атрибуты класса для корректного взаимодействия с методами, и импортированными классами, затем
    происходит инициализация, в ней создается основной каркас приложения, в данном случае это кнопки выбора режимов
    анализа, кнопка выбора файла и запуск аналитики.

    Методы:
    add_to_mods - Метод, который при нажатии на Checkbox отсылал в переменную SELECTED_MODS информацию о том, что она
    нажата, или же, если она есть в списке SELECTED_MODS, то удалял этот mod из него.

    select_file - Метод, который парсит переданный, и получает путь к файлу, выбранному пользователем для анализа.

    draw_a_graph - Статический метод, который обособлен от всего класса, на вход его передаются параметры - Coord_List
    являющийся списком координат, NameMod - название типа анализа, Sequence_number_graf - уникальный тег графика.
    Потом из общего списка координат он получает координаты для оси х и у, и затем рисует график.

    start_draw_grath - Метод, который запускается после нажатия на кнопку 'Start Generation Grath', внутри него сначала
    получаются данные в нужном формате, затем они переводятся в другую систему исчисления из 60, в 100. Затем на основе
    этих данных мы создаем экземпляр класса DataAnalysisView, который анализирует данные исходя из переданных ему
    свойств, для запуска этого анализа вызван метод данного класса - AnalyseView.
    Затем перебираются полученные данные в цикле, где каждая итерация цикла равна одному созданному графику, в свою
    очередь количество итераций зависит от количества выбранных режимов анализа данных max=3, min=1, в конце каждой
    итерации к атрибуту класса COUNT прибавляется единица, которая в методе построения графика является тэгом, и он
    должен быть уникальным.
    """
    COUNT = 0
    SELECTED_MODS = []
    PATH_TO_FILE = ''

    def __init__(self):
        dpg.create_context()
        dpg.create_viewport(title='Analyse Time', width=800, height=900)  # Создаётся базовое окно.

        with dpg.window(label='Primary Window', width=800, height=900):  # Создаётся основное окно программы.
            # Добавляется текст, и кнопки выборов режимов анализа.

            dpg.add_text('Choice mod')
            dpg.add_text('Zero - When there were days without classes\n'
                         'Month - How many hours per month were engaged in total\n'
                         'Standart - Displays how many hours a day you were engaged in\n')

            dpg.add_checkbox(label='Zero', user_data="Zero", callback=self.add_to_mods)
            dpg.add_checkbox(label='Month', user_data="Month", callback=self.add_to_mods)
            dpg.add_checkbox(label='Standart', user_data="Standart", callback=self.add_to_mods)

            dpg.add_text('Choice file')

            # Окно выбора файла для анализа.
            with dpg.file_dialog(directory_selector=False, show=False, callback=self.select_file, file_count=3,
                                 tag='file-dialog-tag', width=700, height=400):
                dpg.add_file_extension("", color=(0, 150, 150, 255))
                dpg.add_file_extension(".*", color=(170, 0, 150, 255))
                dpg.add_button(label="Fancy File dialog")

            dpg.add_button(label="file selector", callback=lambda: dpg.show_item("file-dialog-tag"))  # Кнопка для выбора файла.
            dpg.add_button(label='Start Generation Grath', callback=self.start_draw_grath)  # Кнопка для запуска генерации.

        # Для запуска самого приложения.
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def add_to_mods(self, sender, app_data, user_data):
        """
        Получает информацию, о том какой checkbox выбран, и затем добавляет, или удаляет его из списка модов.
        :param sender: None
        :param app_data: None
        :param user_data: Режим анализа данных
        :return: SELECTED_MODS
        """
        if user_data not in self.SELECTED_MODS:
            self.SELECTED_MODS.append(user_data)
        else:
            self.SELECTED_MODS.remove(user_data)

    def select_file(self, sender, app_data):
        """
        Получает на вход массив с данными, из которого извлекает путь к выбранному файлу для анализа.
        :param sender: None
        :param app_data: Список из данных о выбранном файле
        :return: PATH_TO_FILE
        """
        Path_toFile = list(app_data.values())

        # Из списка получает словарь, из него извлекает value, и затем преобразует в список для дальнейшего удобства работы.
        Path_toFile = list(Path_toFile[-1].values())
        self.PATH_TO_FILE = Path_toFile[0]

    @staticmethod
    def draw_a_graph(Coord_List, NameMod, Sequence_number_graf):
        """
        Графически выводит переданные данные.
        :param Coord_List: Список координат
        :param NameMod: Имя режима анализа
        :param Sequence_number_graf: Уникальный тег графика
        :return: graf
        """
        # print(Coord_List) -> для того, что бы понимать в каком формате передаются координаты.
        X_axis = list(Coord_List.values())[0][1]  # Получает координаты для осей х и у.
        Y_axis = list(Coord_List.values())[0][0]

        # Создается новое окно внутри программы, и затем в нем рисуется график
        with dpg.window(label="Grath"):
            with dpg.plot(label="Line Series", height=700, width=800):
                dpg.add_plot_legend()  # Добавляет легенду к графику.

                # Создает оси координат.
                dpg.add_plot_axis(dpg.mvDatePickerLevel_Day, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", tag=str(Sequence_number_graf))

                # Генерирует график.
                dpg.add_line_series(X_axis, Y_axis, label=NameMod, parent=str(Sequence_number_graf))

    def start_draw_grath(self, sender, user_data):
        """
        Анализирует данные и генерирует график.
        :param sender: None
        :param user_data: None
        :return: graf
        """

        # Получает данные в нужном формате.
        DataTimes_no_analyse = GetData(self.PATH_TO_FILE)
        DataTimes_no_analyse = DataTimes_no_analyse.get_data()

        # Переводит из часовой системы исчисления в 100 систему исчисления.
        DataTimes_translated = TranslateToHours(DataTimes_no_analyse).translate_from_hours()

        # Анализирует данные и возвращает список, состоящий из координат графика.
        DataTimes = DataAnalysisView(DataTimes_translated, self.SELECTED_MODS).AnalyseView()

        # Перебирает графики, для того, что бы каждый вывести на экран.
        for DataTime in DataTimes:

            # Рисует график.
            self.draw_a_graph(Coord_List=DataTime, NameMod=list(DataTime.keys())[0], Sequence_number_graf=self.COUNT)
            self.COUNT += 1  # Увеличивает тэг каждого следующего графика, для того, что бы он был уникален.