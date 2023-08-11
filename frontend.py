import dearpygui.dearpygui as dpg
from math import sin

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)


i_b = []

def to_id(sender, app_data, user_data):
    if user_data not in i_b:
        i_b.append(user_data)
    else:
        i_b.remove(user_data)

def confirm(sender, user_data):
    print(i_b)


with dpg.window(label='Group Buttns'):
    dpg.add_text('Choise mod')
    dpg.add_checkbox(label='Zero', user_data="Zero", callback=to_id)
    dpg.add_checkbox(label='Month', user_data="Month", callback=to_id)
    dpg.add_checkbox(label='Standart', user_data="Standart", callback=to_id)
    dpg.add_button(label='start', callback=confirm)


sindatax = [1.08, 2,3,4,5,6,7]
sindatay = [12,32,34,234,234,234,33]


with dpg.window(label="Tutorial"):
    # create plot
    with dpg.plot(label="Line Series", height=400, width=400):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(sindatax, sindatay,parent="y_axis")




dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

