import dearpygui.dearpygui as dpg

dpg.create_context()

def create_callbeck(sender, app_data):

    print(app_data)



with dpg.file_dialog(directory_selector=False, show=False, callback=create_callbeck, file_count=3, tag='file-dilig-tag', width=700, height=400):
    dpg.add_file_extension("", color=(255, 150,150, 255))
    dpg.add_file_extension(".*")


    dpg.add_button(label="Fancy File dilog")
    with dpg.child_window(width=100):
        dpg.add_selectable(label="Bookr1")
        dpg.add_selectable(label="Bookr2")
        dpg.add_selectable(label="Bookr3")

with dpg.window(label="tt", width=800, height=300):
    dpg.add_button(label="file selector", callback=lambda: dpg.show_item("file-dilig-tag"))

dpg.create_viewport(title='Custom Title', width=800, height=900)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()